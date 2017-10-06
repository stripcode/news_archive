from aiohttp import web
import asyncio
from .ext import initRedis, initMongo, initJinja
from .middleware import mongoMiddleware, redisMiddleware, jinjaMiddleware, authMiddleware
import os
from configparser import ConfigParser
import app.handlers.admin.public.auth as auth
import app.handlers.admin.private.pages as privatePagesHandlers
import app.handlers.admin.private.news as privateNewsHandlers



def loadConfig(runConfig):
  config = ConfigParser()
  with open(os.path.join(os.path.dirname(__file__), 'default.config')) as defaultJsonConfig:
    config.read_file(defaultJsonConfig)
  if runConfig:
    config.read_file(runConfig)
  return config



def createMainApp(pathToConfigFile = None):
  """
  Создает приложение для админской части.
  Параметр pathToConfigFile необходим для указания конфигурациионного файла в продакшене.
  """
  loop = asyncio.get_event_loop()
  config = loadConfig(pathToConfigFile)
  app = web.Application(middlewares = [mongoMiddleware, redisMiddleware, jinjaMiddleware, authMiddleware], loop = loop)
  app["config"] = config

  # Инициализация сторонних библиотек.
  app.on_startup.append(initRedis)
  app.on_startup.append(initMongo)
  app.on_startup.append(initJinja)

  # Публичные роуты.
  app.router.add_post("/", auth.processAuthPage)

  # # Приватные роуты.
  app.router.add_get("/", privatePagesHandlers.showDefaultPrivatePage)
  app.router.add_get("/logout/", privatePagesHandlers.logout)

  # новости
  app.router.add_get("/news/", privateNewsHandlers.defaultNewsPage)

  return app