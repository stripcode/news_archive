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
  return web.Response(text = "401")



async def showDefaultPage(request):
  return web.Response(text = "public")



@login_required
async def showPrivatePage(request):
  return web.Response(text = "private")