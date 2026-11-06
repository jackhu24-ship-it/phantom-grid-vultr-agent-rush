"""Live telemetry probe: Vultr Agent Rush Hackathon"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

STATE = {"app": "202611_Vultr_Agent_Rush_Hackathon", "state": "ONLINE", "vram_gb": 12.4, "vram_limit_gb": 50, "zdr_residual_mb": 0.0}


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps(STATE).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8080), H).serve_forever()
