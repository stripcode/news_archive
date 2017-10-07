from aiohttp import web
import asyncio
from .ext import initRedis, initMongo, initJinja
from .middleware import mongoMiddleware, redisMiddleware, jinjaMiddleware, authMiddleware
import os
from configparser import ConfigParser
import app.handlers.admin.public.auth as adminAuthHandlers
import app.handlers.admin.private.pages as adminPrivatePagesHandlers
import app.handlers.admin.private.news as adminPrivateNewsHandlers



def loadConfig(runConfig):
  config = ConfigParser()
  with open(os.path.join(os.path.dirname(__file__), 'default.config')) as defaultJsonConfig:
    config.read_file(defaultJsonConfig)
  if runConfig:
    config.read_file(runConfig)
  return config



def createAdminApp(pathToConfigFile = None):
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
  app.router.add_post("/", adminAuthHandlers.processAuthPage)

  # # Приватные роуты.
  app.router.add_get("/", adminPrivatePagesHandlers.showDefaultPrivatePage)
  app.router.add_get("/logout/", adminPrivatePagesHandlers.logout)

  # новости
  app.router.add_get("/news/", adminPrivateNewsHandlers.showDefaultPage)
  app.router.add_get("/news/create/", adminPrivateNewsHandlers.showCreateDialog)
  app.router.add_get("/news/{newsId}", adminPrivateNewsHandlers.showNewsPage)
  app.router.add_post("/news/create/", adminPrivateNewsHandlers.processCreateDialog)

  return app