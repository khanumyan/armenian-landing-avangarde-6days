"""Local preview server for the VisitArmenia site.

Usage:  python3 serve.py        then open http://127.0.0.1:8767/

Sends no-cache headers so the browser always shows the latest files.
"""
import http.server
import os

PORT = 8767


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with http.server.ThreadingHTTPServer(('127.0.0.1', PORT), NoCacheHandler) as httpd:
        print(f'Serving on http://127.0.0.1:{PORT}/')
        httpd.serve_forever()
