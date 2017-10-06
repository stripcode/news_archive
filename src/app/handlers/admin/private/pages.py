from aiohttp import web
from app.handlers import login_required



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