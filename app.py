import asyncio

from aiohttp import web
import aiohttp_debugtoolbar
import aiohttp_jinja2
import jinja2

import aiohttp_session
from aiohttp_session.redis_storage import RedisStorage
import aioredis
from middlewares import authorize

from routes import routes

from settings import log

async def on_shutdown(app):
	for ws in app['websockets']:
		await ws.close(message = 'Server Shutdown')

async def init():
	app = web.Application()
	aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))
	redis = await aioredis.create_pool(('localhost', 6379))
	storage = aiohttp_session.redis_storage.RedisStorage(redis)
	aiohttp_session.setup(app, storage)
	app.middlewares.append(authorize)

	for route in routes:
		app.router.add_route(route[0], route[1], route[2], name = route[3])
	app['static_root_url'] = '/static'
	app.router.add_static('/static', 'static', name = 'static')

	app.on_cleanup.append(on_shutdown)
	app['websockets_general'] = []
	app['websockets_interns'] = []
	app['uids'] = [] # 'uid' stands for 'User ID'

	return app



'''
TODO (if needed):
1. Add database
2. Add ORM peewee
'''

log.debug('server start')
web.run_app(init())
log.debug('server end')




