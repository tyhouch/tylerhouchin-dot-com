"""Build a password-locked video page for the static site.

The page holds only ciphertext. The YouTube embed (and its video ID) is encrypted with AES-256-GCM under a key
derived from the password (PBKDF2-SHA256, 600k rounds), and decrypted in the browser with WebCrypto when the
right password is typed. Without the password nothing in the page source reveals the video.
Usage: uv run -q --no-project --with cryptography python -I tools/private_video.py <slug> <title> <youtube_id> <password>
Writes static/private/<slug>/index.html.
"""
import base64
import html
import json
import os
import sys
from pathlib import Path

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ROUNDS = 600_000
slug, title, video_id, password = sys.argv[1:5]

inner = (f'<iframe src="https://www.youtube-nocookie.com/embed/{html.escape(video_id)}?rel=0&modestbranding=1&playsinline=1" '
         'title="video" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>')
salt, iv = os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ROUNDS).derive(password.encode())
blob = {k: base64.b64encode(v).decode() for k, v in
        {"salt": salt, "iv": iv, "ct": AESGCM(key).encrypt(iv, inner.encode(), None)}.items()}

page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>__TITLE__</title>
<style>
:root { --bg: #fafafa; --fg: #111; --muted: #777; --line: #ddd; }
@media (prefers-color-scheme: dark) { :root { --bg: #111; --fg: #eee; --muted: #888; --line: #333; } }
* { box-sizing: border-box; }
body { margin: 0; min-height: 100vh; background: var(--bg); color: var(--fg);
       font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; display: grid; place-items: center; }
main { width: min(100%, 1100px); padding: 24px 16px; }
h1 { font-size: 20px; font-weight: 600; margin: 0 0 16px; }
form { display: flex; gap: 8px; max-width: 360px; }
input, button { font: inherit; padding: 10px 12px; border-radius: 8px; border: 1px solid var(--line); background: transparent; color: var(--fg); }
input { flex: 1; min-width: 0; }
button { cursor: pointer; }
#err { color: #d33; min-height: 1.5em; margin: 8px 0 0; font-size: 14px; }
.video { position: relative; aspect-ratio: 16 / 9; width: 100%; background: #000; border-radius: 8px; overflow: hidden; }
.video iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
</style></head>
<body><main>
<h1>__TITLE__</h1>
<form id="f"><input id="p" type="password" placeholder="Password" autocomplete="current-password" autofocus><button>Watch</button></form>
<p id="err"></p>
<div id="out"></div>
</main>
<script>
const B = __BLOB__, ROUNDS = __ROUNDS__;
const b64 = s => Uint8Array.from(atob(s), c => c.charCodeAt(0));
document.getElementById("f").addEventListener("submit", async e => {
  e.preventDefault();
  const err = document.getElementById("err");
  err.textContent = "";
  try {
    const base = await crypto.subtle.importKey("raw", new TextEncoder().encode(document.getElementById("p").value), "PBKDF2", false, ["deriveKey"]);
    const key = await crypto.subtle.deriveKey({ name: "PBKDF2", salt: b64(B.salt), iterations: ROUNDS, hash: "SHA-256" },
      base, { name: "AES-GCM", length: 256 }, false, ["decrypt"]);
    const plain = await crypto.subtle.decrypt({ name: "AES-GCM", iv: b64(B.iv) }, key, b64(B.ct));
    document.getElementById("f").remove();
    document.getElementById("out").innerHTML = '<div class="video">' + new TextDecoder().decode(plain) + "</div>";
  } catch { err.textContent = "Wrong password."; }
});
</script>
</body></html>
"""
page = (page.replace("__TITLE__", html.escape(title)).replace("__BLOB__", json.dumps(blob))
        .replace("__ROUNDS__", str(ROUNDS)))
out = Path(__file__).resolve().parent.parent / "static" / "private" / slug / "index.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(page)
print(out)
