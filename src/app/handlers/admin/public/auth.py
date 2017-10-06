from aiohttp import web
from uuid import uuid4



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