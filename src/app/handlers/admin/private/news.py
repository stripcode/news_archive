from app.handlers import login_required
from aiohttp import web
from bson.objectid import ObjectId
from time import time



@login_required
async def showDefaultPage(request):
  """
  Страница по умолчанию для админского раздела новостей
  """
  cursor = request.mongo.article.find({}, {"title": 1})
  articles = await cursor.to_list(100)
  return request.template("admin/private/news/defaultPage.tpl", {"articles": articles})



@login_required
async def showCreateDialog(request):
  """
  Страница создания новости
  """
  return request.template("admin/private/news/createDialog.tpl")



@login_required
async def processCreateDialog(request):
  """
  Обрабатываю данные из формы создания диалога
  и создаю новость
  """
  formData = await request.post()
  title = formData.get("title")
  content = formData.get("content")
  art = {
    "title": title,
    "content": content,
    "createTime": int(time())
  }
  result = await request.mongo.article.insert_one(art)
  return web.HTTPFound("/news/{}".format(result.inserted_id))



@login_required
async def showNewsPage(request):
  """
  Страница отображения одной новости
  """
  newsId = request.match_info.get('newsId')
  article = await request.mongo.article.find_one({"_id": ObjectId(newsId)})
  if not article:
    return web.HTTPNotFound()
  return request.template("admin/private/news/NewsPage.tpl", {"article": article})



@login_required
async def showEditNewsDialog(request):
  """
  Диалог редактирования новости
  """
  newsId = request.match_info.get('newsId')
  article = await request.mongo.article.find_one({"_id": ObjectId(newsId)})
  if not article:
    return web.HTTPNotFound()
  return request.template("admin/private/news/EditNewsDialog.tpl", {"article": article})



@login_required
async def processEditNewsDialog(request):
  """
  Обрабатыва диалог редактирования новости
  """
  newsId = request.match_info.get('newsId')
  formData = await request.post()
  title = formData.get("title")
  content = formData.get("content")
  art = {
    "title": title,
    "content": content
  }
  await request.mongo.article.update_one({"_id": ObjectId(newsId)}, {"$set": art})
  return web.HTTPFound("/news/{}".format(newsId))