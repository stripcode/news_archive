from aiohttp import web
import asyncio
from .ext import initRedis, initMongo
from .middleware import mongoMiddleware, redisMiddleware, auth
import os
from configparser import ConfigParser
from .handlers import showDefaultPage, showPrivatePage



def loadConfig(runConfig):
  config = ConfigParser()
  with open(os.path.join(os.path.dirname(__file__), 'default.config')) as defaultJsonConfig:
    config.read_file(defaultJsonConfig)
  if runConfig:
    config.read_file(runConfig)
  return config



def createMainApp(config = None):
  loop = asyncio.get_event_loop()
  app = web.Application(middlewares = [mongoMiddleware, redisMiddleware, auth], loop = loop)
  app["config"] = loadConfig(config)
  app.on_startup.append(initRedis)
  app.on_startup.append(initMongo)
  app.router.add_get("/", showDefaultPage)
  app.router.add_get("/private/", showPrivatePage)
  return app