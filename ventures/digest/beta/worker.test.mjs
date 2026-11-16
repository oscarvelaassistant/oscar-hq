// Tests for worker.js with a mock KV. Run: node worker.test.mjs (Node 18 or newer, no install).
import worker from "./worker.js";
import { readFileSync } from "node:fs";
import { createHash, randomBytes } from "node:crypto";

class MockKV {
  constructor() { this.m = new Map(); }
  async get(k, type) { const v = this.m.has(k) ? this.m.get(k) : null; return v !== null && type === "json" ? JSON.parse(v) : v; }
  async put(k, v) { this.m.set(k, String(v)); }
  async delete(k) { this.m.delete(k); }
}
const sha = (s) => createHash("sha256").update(s).digest("hex");
const b64url = (b) => b.toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");

const kv = new MockKV();
const runnerToken = b64url(randomBytes(32));
await kv.put("runner:" + sha(runnerToken), "1");
const env = { DIGEST_BETA: kv, FORM_HTML: readFileSync(new URL("./public/form.html", import.meta.url), "utf8") };

const base = "https://digest-preview.projetrefonte.com";
const call = (method, path, body, headers = {}) =>
  worker.fetch(new Request(base + path, { method, headers: Object.assign(body ? { "content-type": "application/json" } : {}, headers), body: body ? JSON.stringify(body) : undefined }), env);
const runner = { authorization: "Bearer " + runnerToken };
const browser = { "x-requested-with": "digest" };

let failed = 0;
async function check(name, cond) { if (cond) console.log("ok   " + name); else { failed++; console.log("FAIL " + name); } }

// health
let r = await call("GET", "/health");
await check("health 200", r.status === 200 && (await r.json()).ok === true);

// a wrong link shows the one plain line
const key = b64url(randomBytes(32));
r = await call("GET", "/s/" + key);
await check("unknown key is 404 with the plain line", r.status === 404 && (await r.text()).startsWith("This link is not one of ours."));
r = await call("GET", "/s/short");
await check("malformed key is 404", r.status === 404);

// runner registers oscar's link (new_link.sh sends only the hash)
r = await call("PUT", "/r/links/oscar", { hash: sha(key) });
await check("putLink without token is 401", r.status === 401);
r = await call("PUT", "/r/links/oscar", { hash: sha(key) }, runner);
await check("putLink registers", r.status === 200);

// the form is served with the empty profile and a nonce CSP
r = await call("GET", "/s/" + key);
let html = await r.text();
await check("form 200", r.status === 200);
await check("form carries noindex", r.headers.get("x-robots-tag").includes("noindex"));
await check("CSP has a nonce and no placeholder left", /script-src 'nonce-[A-Za-z0-9_-]+'/.test(r.headers.get("content-security-policy")) && !html.includes("{{NONCE}}") && !html.includes("{{PROFILE_JSON}}"));
await check("profile injected", html.includes('"tone":"straight"'));

// save without the header is refused; with it, saved
r = await call("PUT", "/s/" + key, { name: "Oscar", city: "Arenys de Mar", topics: "Robotics, shipyards, Catalan politics" });
await check("PUT without x-requested-with is 400", r.status === 400);
r = await call("PUT", "/s/" + key, { name: "Oscar", city: "Arenys de Mar", topics: "Robotics, shipyards, Catalan politics", urls: ["https://example.com/news", ""], tone: "analytical" }, browser);
let j = await r.json();
await check("save 200 and echoed", r.status === 200 && j.profile.name === "Oscar" && j.profile.urls.length === 1 && j.profile.tone === "analytical");
r = await call("PUT", "/s/" + key, { name: "Oscar", city: "x", topics: "y", urls: ["not a url"] }, browser);
await check("bad url is 400 with a message", r.status === 400 && (await r.json()).error.includes("not a web address"));
r = await call("PUT", "/s/" + key, { name: "Oscar", city: "x", topics: "y", tone: "shouty" }, browser);
await check("unknown tone falls back to straight", (await r.json()).profile.tone === "straight");

// the button: three a day, the fourth refused politely
r = await call("PUT", "/s/" + key, { name: "Oscar", city: "", topics: "y", make: true }, browser);
await check("make with a missing field is 400", r.status === 400);
for (let i = 1; i <= 3; i++) {
  r = await call("PUT", "/s/" + key, { name: "Oscar", city: "Arenys de Mar", topics: "Robotics", make: true }, browser);
  await check("make " + i + " accepted", r.status === 200 && (await r.json()).profile.requests_today === i);
}
r = await call("PUT", "/s/" + key, { name: "Oscar", city: "Arenys de Mar", topics: "Robotics", make: true }, browser);
await check("fourth make is 429 with the polite line", r.status === 429 && (await r.json()).error.startsWith("Three issues a day"));

// the runner reads everything in one request and sees the pending status
r = await call("GET", "/r/profiles");
await check("profiles without token is 401", r.status === 401);
r = await call("GET", "/r/profiles", null, runner);
j = await r.json();
await check("profiles lists oscar with being-made", j.profiles.length === 1 && j.profiles[0].id === "oscar" && j.profiles[0].status.state === "being-made" && j.profiles[0].profile.requests.length === 3);

// runner writes a status; the form shows it
r = await call("PUT", "/r/status/oscar", { state: "sent", at: new Date().toISOString(), at_local: "06:52" }, runner);
await check("status sent accepted", r.status === 200);
r = await call("PUT", "/r/status/oscar", { state: "exploded" }, runner);
await check("unknown state is 400", r.status === 400);
r = await call("GET", "/s/" + key);
html = await r.text();
await check("form carries the status", html.includes('"state":"sent"') && html.includes('"at_local":"06:52"'));

// a replaced link keeps the profile and kills the old key
const key2 = b64url(randomBytes(32));
r = await call("PUT", "/r/links/oscar", { hash: sha(key2) }, runner);
await check("replace link 200", r.status === 200 && (await r.json()).entries === 1);
r = await call("GET", "/s/" + key);
await check("old key is dead", r.status === 404);
r = await call("GET", "/s/" + key2);
await check("new key carries the profile", r.status === 200 && (await r.text()).includes('"name":"Oscar"'));

// injected JSON cannot close the script tag
r = await call("PUT", "/s/" + key2, { name: "</script><b>", city: "x", topics: "y" }, browser);
r = await call("GET", "/s/" + key2);
html = await r.text();
await check("profile JSON escapes <", !html.includes('"name":"</script>'));

// no em dash anywhere in the page or the worker
const src = readFileSync(new URL("./worker.js", import.meta.url), "utf8");
await check("no em dash in form.html or worker.js", !env.FORM_HTML.includes("\u2014") && !src.includes("\u2014"));

console.log(failed ? failed + " failed" : "all passed");
process.exit(failed ? 1 : 0);
