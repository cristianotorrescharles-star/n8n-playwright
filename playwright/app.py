from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import asyncio
from playwright.async_api import async_playwright

PORT = 10000

async def run_script(data):
    acao = data.get("acao")
    titulo = data.get("titulo")
    descricao = data.get("descricao")
    prazo = data.get("prazo")
    fluxo = data.get("fluxo")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # LOGIN
        await page.goto("https://app2.artia.com/users/login")
        await page.fill('[data-test-id="userEmail"]', "SEU_EMAIL")
        await page.fill('[data-test-id="userPassword"]', "SUA_SENHA")
        await page.click('[data-test-id="sign-in"]')

        # EXEMPLO SIMPLES
        await page.goto("https://example.com")

        title = await page.title()

        await browser.close()

        return {"resultado": title, "acao": acao}

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        data = json.loads(body)

        result = asyncio.run(run_script(data))

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

print("API Playwright rodando...")

server = HTTPServer(("0.0.0.0", PORT), Handler)
server.serve_forever()
