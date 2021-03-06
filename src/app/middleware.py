from app.handlers.admin.public.auth import authPage



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



async def jinjaMiddleware(app, handler):
  async def middleware(request):
    def render(template, context = {}):
      return app.aiohttp_jinja2.render_template(template, request, context)
    request.template = render
    response = await handler(request)
    return response
  return middleware



async def authMiddleware(app, handler):
  async def middleware(request):
    if hasattr(handler, "login_required"):
      cookie = request.cookies.get("AIOHTTP_SESSION")
      user = await request.redis.get("session:{}".format(cookie))
      if user:
        request.user = user
      else:
        return await authPage(request)
    return await handler(request)
  return middleware