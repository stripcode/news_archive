from aiohttp import web
import asyncio
from .ext import initRedis, initMongo, initJinja
from .middleware import mongoMiddleware, redisMiddleware, jinjaMiddleware,  auth
import os
from configparser import ConfigParser
import app.handlers as handlers


def loadConfig(runConfig):
  config = ConfigParser()
  with open(os.path.join(os.path.dirname(__file__), 'default.config')) as defaultJsonConfig:
    config.read_file(defaultJsonConfig)
  if runConfig:
    config.read_file(runConfig)
  return config



def createMainApp(config = None):
  loop = asyncio.get_event_loop()
  app = web.Application(middlewares = [mongoMiddleware, redisMiddleware, jinjaMiddleware, auth], loop = loop)
  app["config"] = loadConfig(config)
  app.on_startup.append(initRedis)
  app.on_startup.append(initMongo)
  app.on_startup.append(initJinja)
  app.router.add_post("/", handlers.processAuthPage)

  # private
  app.router.add_get("/", handlers.showPrivatePage)
  app.router.add_get("/logout/", handlers.logout)
  return app