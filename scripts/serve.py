#!/usr/bin/env python3
"""Preview the static site with Python's standard-library HTTP server."""

from __future__ import annotations

import http.server
import socketserver
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs"
PORT = 8040


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)


with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as server:
    print(f"Previewing the atlas at http://127.0.0.1:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nPreview stopped.")
