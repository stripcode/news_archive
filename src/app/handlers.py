from aiohttp import web
import asyncio
import functools



def login_required(f):
  @asyncio.coroutine
  @functools.wraps(f)
  def wrapper(request):
    return f(request)
  wrapper.login_required = True
  return wrapper



async def authPage(request):
  return request.template("auth.tpl", {"name": 123})



async def processAuthPage(request):
  data = await request.post()
  login = data.get("login", None)
  password = data.get("password", None)
  if not all([login, password]):
    raise RuntimeError("Нет обязательных параметров")
  if login == "admin" and password == "Aa123456":
    await request.redis.set("session", 1)
  return web.HTTPFound('/')



@login_required
async def showPrivatePage(request):
  return request.template("defaultPrivatePage.tpl")



@login_required
async def logout(request):
  await request.redis.delete("session")
  return web.HTTPFound('/')