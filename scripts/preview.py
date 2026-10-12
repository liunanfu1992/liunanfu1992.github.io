"""Serve the static redesign on localhost, exposing only public site files.

Read source files on each request so a browser refresh shows saved edits.
No Ruby dependencies or generated Jekyll output are involved.
"""

import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = {
    "index.html", "404.html", "about.html", "about/index.html",
    "robots.txt", "sitemap.xml", "assets/css/style.css", "assets/js/main.js",
    "assets/img/favicon.svg",
}
PUBLIC_FOLDERS = {"images", "assets/fonts/homepage"}


class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_head(self):
        request_path = unquote(urlsplit(self.path).path)
        candidate = (ROOT / request_path.lstrip("/")).resolve()
        if candidate.is_dir():
            candidate /= "index.html"
        if not candidate.is_relative_to(ROOT):
            self.send_error(404)
            return None
        relative = candidate.relative_to(ROOT).as_posix()
        allowed = relative in PUBLIC_FILES or any(
            relative.startswith(folder + "/") for folder in PUBLIC_FOLDERS
        )
        if not allowed or not candidate.is_file():
            self.send_error(404)
            return None
        return super().send_head()

    def send_error(self, code, message=None, explain=None):
        if code != 404:
            return super().send_error(code, message, explain)
        content = (ROOT / "404.html").read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    with ThreadingHTTPServer(("127.0.0.1", args.port), PreviewHandler) as server:
        print(f"Preview: http://127.0.0.1:{args.port}", flush=True)
        print("Refresh your browser after saving changes. Ctrl-C to stop.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
