from aiohttp import web
from app import createAdminApp

app = createAdminApp()
web.run_app(app, host = "0.0.0.0", port = 8000)