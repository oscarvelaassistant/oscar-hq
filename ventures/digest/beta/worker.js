// digest-beta: the six routes of beta-plan.md section 2. Draft written 2026-11-16 by the HQ evening run
// (task queue/2026-11-16-004). Not deployed. Session 3 on the box reviews it, runs worker.test.mjs, and
// deploys only on Oscar's typed yes.
//
// Bindings expected (wrangler.toml): KV namespace DIGEST_BETA, static assets ASSETS (public/).
// Key types in KV (four, as the plan says):
//   index                 -> { entries: [{ id, hash }] }        one per person, hash = sha256(key)
//   profile:<hash>        -> the profile JSON (section 5 of questions.md)
//   status:<id>           -> { state, at, at_local }            written by the runner
//   runner:<sha256(tok)>  -> "1"                                 the runner token, created on the box
//
// Routes:
//   GET  /s/<key>          the form, with the saved profile and status injected
//   PUT  /s/<key>          save the profile; body.make === true asks for an issue (3 a day per person)
//   GET  /r/profiles       runner token; every profile with its id, status and pending requests
//   PUT  /r/links/<id>     runner token; body { hash } registers a person (new_link.sh)
//   PUT  /r/status/<id>    runner token; body { state, at, at_local }
//   GET  /health

const LIMITS = { name: 40, city: 80, topics: 400, about: 600, urls: 5, url: 300, perDay: 3 };
const TONES = new Set(["straight", "analytical", "light"]);
const KEY_RE = /^[A-Za-z0-9_-]{32,64}$/;
const ID_RE = /^[a-z0-9][a-z0-9-]{0,31}$/;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;
    try {
      if (path === "/health" && method === "GET") return json({ ok: true }, 200);

      let m;
      if ((m = path.match(/^\/s\/([^/]+)$/))) {
        if (!KEY_RE.test(m[1])) return plain(notOurs(), 404);
        const hash = await sha256(m[1]);
        if (method === "GET") return serveForm(env, hash);
        if (method === "PUT") return saveProfile(request, env, hash);
        return plain("Method not allowed", 405);
      }

      if (path.startsWith("/r/")) {
        if (!(await runnerOk(request, env))) return json({ error: "unauthorized" }, 401);
        if (path === "/r/profiles" && method === "GET") return listProfiles(env);
        if ((m = path.match(/^\/r\/links\/([^/]+)$/)) && method === "PUT") return putLink(request, env, m[1]);
        if ((m = path.match(/^\/r\/status\/([^/]+)$/)) && method === "PUT") return putStatus(request, env, m[1]);
        return json({ error: "not found" }, 404);
      }

      // Static files (fonts) only; nothing else exists.
      if (method === "GET" && path.startsWith("/fonts/") && env.ASSETS) {
        const r = await env.ASSETS.fetch(request);
        return withHeaders(r, {});
      }
      return plain(notOurs(), 404);
    } catch (e) {
      return json({ error: "server error" }, 500);
    }
  }
};

function notOurs() { return "This link is not one of ours. Ask Oscar for a new one."; }

async function serveForm(env, hash) {
  const profile = await env.DIGEST_BETA.get("profile:" + hash, "json");
  if (!profile) return plain(notOurs(), 404);
  const entry = await findEntryByHash(env, hash);
  const status = entry ? await env.DIGEST_BETA.get("status:" + entry.id, "json") : null;
  const view = Object.assign({}, publicProfile(profile), { status: status || null });
  const nonce = base64url(crypto.getRandomValues(new Uint8Array(16)));
  let html = await formTemplate(env);
  html = html.replace("{{PROFILE_JSON}}", escapeJson(JSON.stringify(view))).replace("{{NONCE}}", nonce);
  return new Response(html, {
    status: 200,
    headers: securityHeaders({
      "content-type": "text/html; charset=utf-8",
      "content-security-policy": "default-src 'none'; script-src 'nonce-" + nonce + "'; style-src 'unsafe-inline'; font-src 'self'; img-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'self'",
      "cache-control": "no-store"
    })
  });
}

async function formTemplate(env) {
  if (env.FORM_HTML) return env.FORM_HTML; // tests inject the file
  const r = await env.ASSETS.fetch(new Request("https://assets.local/form.html"));
  return r.text();
}

async function saveProfile(request, env, hash) {
  if (request.headers.get("x-requested-with") !== "digest") return json({ error: "bad request" }, 400);
  const existing = await env.DIGEST_BETA.get("profile:" + hash, "json");
  if (!existing) return plain(notOurs(), 404);
  let body;
  try { body = await request.json(); } catch (e) { return json({ error: "bad json" }, 400); }
  const v = validate(body);
  if (v.error) return json({ error: v.error }, 400);

  const now = new Date();
  const profile = Object.assign({}, existing, v.profile, { updated_at: now.toISOString() });
  const today = madridDay(now);
  profile.requests = (existing.requests || []).filter((t) => madridDay(new Date(t)) === today);

  let code = 200;
  if (body.make === true) {
    if (profile.requests.length >= LIMITS.perDay) {
      await env.DIGEST_BETA.put("profile:" + hash, JSON.stringify(profile));
      return json({ error: "Three issues a day is the limit. Tomorrow's is on its way at 07:00.", profile: publicProfile(profile) }, 429);
    }
    profile.requests.push(now.toISOString());
    const entry = await findEntryByHash(env, hash);
    if (entry) await env.DIGEST_BETA.put("status:" + entry.id, JSON.stringify({ state: "being-made", at: now.toISOString() }));
  }
  await env.DIGEST_BETA.put("profile:" + hash, JSON.stringify(profile));
  return json({ ok: true, profile: publicProfile(profile) }, code);
}

function validate(b) {
  if (!b || typeof b !== "object") return { error: "bad request" };
  const s = (x, max) => (typeof x === "string" ? x.trim().slice(0, max) : "");
  const p = {
    name: s(b.name, LIMITS.name),
    city: s(b.city, LIMITS.city),
    topics: s(b.topics, LIMITS.topics),
    about: s(b.about, LIMITS.about),
    tone: TONES.has(b.tone) ? b.tone : "straight",
    urls: [],
    paused: b.paused === true
  };
  if (Array.isArray(b.urls)) {
    for (const u of b.urls.slice(0, LIMITS.urls)) {
      if (typeof u !== "string") continue;
      const t = u.trim().slice(0, LIMITS.url);
      if (!t) continue;
      try {
        const parsed = new URL(t);
        if (parsed.protocol !== "https:" && parsed.protocol !== "http:") return { error: "Links have to start with https://" };
        p.urls.push(parsed.toString());
      } catch (e) { return { error: "One of the links is not a web address: " + t }; }
    }
  }
  if (b.make === true && (!p.name || !p.city || !p.topics)) return { error: "Three fields are needed first: your name, your city and your topics." };
  return { profile: p };
}

async function runnerOk(request, env) {
  const auth = request.headers.get("authorization") || "";
  const m = auth.match(/^Bearer\s+([A-Za-z0-9_-]{32,128})$/);
  if (!m) return false;
  const v = await env.DIGEST_BETA.get("runner:" + (await sha256(m[1])));
  return v === "1";
}

async function listProfiles(env) {
  const index = (await env.DIGEST_BETA.get("index", "json")) || { entries: [] };
  const out = [];
  for (const e of index.entries) {
    const profile = await env.DIGEST_BETA.get("profile:" + e.hash, "json");
    const status = await env.DIGEST_BETA.get("status:" + e.id, "json");
    out.push({ id: e.id, profile: profile || null, status: status || null });
  }
  return json({ profiles: out }, 200);
}

async function putLink(request, env, id) {
  if (!ID_RE.test(id)) return json({ error: "bad id" }, 400);
  let body;
  try { body = await request.json(); } catch (e) { return json({ error: "bad json" }, 400); }
  if (typeof body.hash !== "string" || !/^[a-f0-9]{64}$/.test(body.hash)) return json({ error: "hash must be sha256 hex" }, 400);
  const index = (await env.DIGEST_BETA.get("index", "json")) || { entries: [] };
  const old = index.entries.find((e) => e.id === id);
  if (old && old.hash !== body.hash) {
    // A replaced link keeps the profile and retires the old key.
    const p = await env.DIGEST_BETA.get("profile:" + old.hash, "json");
    if (p) await env.DIGEST_BETA.put("profile:" + body.hash, JSON.stringify(p));
    await env.DIGEST_BETA.delete("profile:" + old.hash);
    old.hash = body.hash;
  } else if (!old) {
    index.entries.push({ id, hash: body.hash });
  }
  if (!(await env.DIGEST_BETA.get("profile:" + body.hash))) {
    await env.DIGEST_BETA.put("profile:" + body.hash, JSON.stringify({ name: "", city: "", topics: "", about: "", tone: "straight", urls: [], paused: false, requests: [] }));
  }
  await env.DIGEST_BETA.put("index", JSON.stringify(index));
  return json({ ok: true, id, entries: index.entries.length }, 200);
}

async function putStatus(request, env, id) {
  if (!ID_RE.test(id)) return json({ error: "bad id" }, 400);
  let body;
  try { body = await request.json(); } catch (e) { return json({ error: "bad json" }, 400); }
  const states = new Set(["being-made", "sent", "late", "saved"]);
  if (!states.has(body.state)) return json({ error: "state must be being-made, sent, late or saved" }, 400);
  const status = { state: body.state, at: typeof body.at === "string" ? body.at.slice(0, 40) : new Date().toISOString() };
  if (typeof body.at_local === "string") status.at_local = body.at_local.slice(0, 5);
  await env.DIGEST_BETA.put("status:" + id, JSON.stringify(status));
  return json({ ok: true }, 200);
}

async function findEntryByHash(env, hash) {
  const index = (await env.DIGEST_BETA.get("index", "json")) || { entries: [] };
  return index.entries.find((e) => e.hash === hash) || null;
}

function publicProfile(p) {
  const { name, city, topics, about, tone, urls, paused, updated_at } = p;
  return { name, city, topics, about, tone, urls: urls || [], paused: !!paused, updated_at: updated_at || null, requests_today: (p.requests || []).length };
}

function madridDay(d) {
  return new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Madrid", year: "numeric", month: "2-digit", day: "2-digit" }).format(d);
}

async function sha256(s) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return Array.from(new Uint8Array(buf)).map((b) => b.toString(16).padStart(2, "0")).join("");
}

function base64url(bytes) {
  let s = "";
  for (const b of bytes) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function escapeJson(s) { return s.replace(/</g, "\\u003c").replace(/\u2028/g, "\\u2028").replace(/\u2029/g, "\\u2029"); }

function securityHeaders(h) {
  return Object.assign({
    "x-robots-tag": "noindex, nofollow, noarchive",
    "referrer-policy": "no-referrer",
    "x-content-type-options": "nosniff",
    "x-frame-options": "DENY"
  }, h);
}
function withHeaders(r, extra) {
  const h = new Headers(r.headers);
  for (const [k, v] of Object.entries(securityHeaders(extra))) h.set(k, v);
  return new Response(r.body, { status: r.status, headers: h });
}
function json(obj, status) {
  return new Response(JSON.stringify(obj), { status, headers: securityHeaders({ "content-type": "application/json; charset=utf-8", "cache-control": "no-store" }) });
}
function plain(text, status) {
  return new Response(text + "\n", { status, headers: securityHeaders({ "content-type": "text/plain; charset=utf-8", "cache-control": "no-store" }) });
}
