import motor.motor_asyncio
import aioredis



async def initRedis(app):
  app.redisPool = await aioredis.create_pool((app["config"]["redis"]["host"], int(app["config"]["redis"]["port"])),
    minsize = int(app["config"]["redis"]["poolMinSize"]), maxsize = int(app["config"]["redis"]["poolMaxSize"]),
    loop = app.loop, encoding = "utf-8", db = int(app["config"]["redis"]["db"]))



def initMongo(app):
  client = motor.motor_asyncio.AsyncIOMotorClient(app["config"]["mongo"]["dsn"])
  app.mongoHandler = client[app["config"]["mongo"]["database"]]