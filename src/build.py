"""Builds index.html: a single self-contained deck with every image, video and logo inlined.

Usage:  python3 src/build.py            (writes index.html at the repo root)
"""
import base64, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
A = ROOT / "assets"
T = (ROOT / "src" / "template.html").read_text(encoding="utf-8")

def uri(path, mime):
    return "data:%s;base64,%s" % (mime, base64.b64encode(path.read_bytes()).decode())

T = T.replace("{{LOGO_FLAM}}", uri(A / "logos" / "flam.png", "image/png"))
T = T.replace("{{LOGO_MOE}}", uri(A / "logos" / "moe-white.png", "image/png"))
T = T.replace("{{URL_KIOSK}}", "https://ministry-of-education.lovable.app/")
T = T.replace("{{URL_VOICE}}", "https://app.talk.flamapp.ai/share?project_id=6af922481bce0dcfc34e72e5&amp;client_key=ak_nyhsc5ttq9hp8md")
T = T.replace("{{URL_FLICKS}}", "https://storage.googleapis.com/bucket-fi-development-apps-5b0640d5/app/abc/videos/ug867d5xx2b0xykctp70knhu.html")

cache = {}
def img(m):
    k = m.group(1)
    if k not in cache:
        cache[k] = uri(A / "images" / (k + ".jpg"), "image/jpeg")
    return cache[k]
T = re.sub(r"\{\{IMG_([a-z_]+)\}\}", img, T)
T = re.sub(r"\{\{VID_([a-z_]+)\}\}", lambda m: uri(A / "video" / (m.group(1) + ".mp4"), "video/mp4"), T)

left = re.findall(r"\{\{[A-Za-z_]+\}\}", T)
assert not left, "Unfilled placeholders: %s" % left
(ROOT / "index.html").write_text(T, encoding="utf-8")
print("index.html written, %d KB" % (len(T) // 1024))
