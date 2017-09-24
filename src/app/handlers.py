from aiohttp import web
import asyncio
import functools
from uuid import uuid4



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
    uid = str(uuid4())
    await request.redis.set("session:{}".format(uid), uid)
    response = web.Response(text = "редирект", status = 302, headers = {'Location': '/'})
    response.set_cookie("AIOHTTP_SESSION", uid)
    return response
  return web.HTTPFound('/')



@login_required
async def showPrivatePage(request):
  return request.template("defaultPrivatePage.tpl")



@login_required
async def logout(request):
  cookie = request.cookies.get("AIOHTTP_SESSION")
  await request.redis.delete("session:{}".format(cookie))
  return web.HTTPFound('/')