from .handlers import authPage



async def mongoMiddleware(app, handler):
  async def middleware(request):
    request.mongo = app.mongoHandler
    response = await handler(request)
    return response
  return middleware



async def redisMiddleware(app, handler):
  async def middleware(request):
    with await app.redisPool as redis:
      request.redis = redis
      response = await handler(request)
    return response
  return middleware



async def auth(app, handler):
  async def middleware(request):
    if hasattr(handler, "login_required"):
      user = await request.redis.get("session")
      if user:
        request.user = user
      else:
        return await authPage(request)
    return await handler(request)
  return middleware