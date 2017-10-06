import asyncio
import functools



def login_required(f):
  """
  Декоратор позволяет выставить флаг login_required хендлеру,
  которыей в свою очередь будет обрабатывать в middleare.
  """
  @asyncio.coroutine
  @functools.wraps(f)
  def wrapper(request):
    return f(request)
  wrapper.login_required = True # флаг для middleware
  return wrapper