import asyncio

from aiohttp import web
import aiohttp_debugtoolbar
import aiohttp_jinja2
import jinja2

from aiohttp_session import session_middleware
from aiohttp_session.redis_storage import RedisStorage
import hashlib

from routes import routes

from settings import log

async def on_shutdown(app):
	for ws in app['websockets']:
		await ws.close(message = 'Server Shutdown')

app = web.Application() #inherits from dict, dict-like object, but we can't copy it

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))

#TODO: add_route edit as needed
for route in routes:
	#add named routers for later retrieving them by app.router[name]
	app.router.add_route(route[0], route[1], route[2], name = route[3])
app['static_root_url'] = '/static'
app.router.add_static('/static', 'static', name = 'static')

'''
TODO (if needed):
1. Add database
2. Add ORM peewee
'''


#on_cleanup handler is called when Subscriber, i.e. user, disconnects
app.on_cleanup.append(on_shutdown)
app['websockets'] = []

log.debug('server start')
web.run_app(app)
log.debug('server end')




