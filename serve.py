#!/usr/bin/env python3
"""
RoomMuse Virtual Gallery — Local Dev Server

Usage:
    python serve.py          # starts on port 8000
    python serve.py 3000     # starts on port 3000

Opens your browser automatically.
"""

import http.server
import socketserver
import sys
import webbrowser
import os

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"\n  🎨  RoomMuse Virtual Gallery")
    print(f"  ────────────────────────────")
    print(f"  Running at:  {url}")
    print(f"  Press Ctrl+C to stop\n")
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.")
        httpd.server_close()
