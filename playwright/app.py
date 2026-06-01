
from http.server import BaseHTTPRequestHandler, HTTPServer
from playwright.sync_api import sync_playwright

PORT = 10000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://example.com")
            title = page.title()
            browser.close()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Título: {title}".encode())

print("API Playwright rodando...")

server = HTTPServer(("0.0.0.0", PORT), Handler)
server.serve_forever()
