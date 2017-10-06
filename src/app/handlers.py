from aiohttp import web
import asyncio
import functools
from uuid import uuid4



def login_required(f):
  """
  Декоратор позволяет выставить флаг login_required хендлеру,
  которыей в свою очередь будет обрабатывать в middleare.
  """
  @asyncio.coroutine
  @functools.wraps(f)
  def wrapper(request):
    return f(request)
  wrapper.login_required = True # флаг для middleware
  return wrapper



async def authPage(request):
  """
  Страница отображает форму входа в административные раздел.
  """
  return request.template("auth.tpl", {"name": 123})



async def processAuthPage(request):
  """
  Обрабатывает данные логина и пароля из формы входа authPage.
  Если логин и пароль подходят создает сессию в редисе
  и редиректит на приватную часть showPrivatePage
  иначе вовзращает 404 код.
  """
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
async def showDefaultPrivatePage(request):
  """
  Страница по умолчанию приватной части.
  """
  return request.template("admin/private/defaultPage.tpl")



@login_required
async def logout(request):
  """
  Разлогинивает пользователя удаляя его сессию из redis.
  """
  cookie = request.cookies.get("AIOHTTP_SESSION")
  await request.redis.delete("session:{}".format(cookie))
  return web.HTTPFound('/')