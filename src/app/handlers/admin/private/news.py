from app.handlers import login_required



@login_required
async def defaultNewsPage(request):
  """
  Страница по умолчанию для админского раздела новостей
  """
  return request.template("admin/private/news/defaultPage.tpl")