import aiohttp_jinja2
from aiohttp import web, WSMsgType

from settings import log

import random

uids = []

class ChatList(web.View):
	@aiohttp_jinja2.template('index.html')
	async def get(self):
		return {}


class WebSocket(web.View):
	async def get(self):
		ws = web.WebSocketResponse()
		await ws.prepare(self.request)

		#session might need to be instantiated here

		#id generation
		uid = 'user{0}'.format(random.randint(1, 1001))
		while uid in uids:
			uid = 'user{0}'.format(random.randint(1, 1001))

		#new response socket is added
		self.request.app['websockets'].append(ws)
		for _ws in self.request.app['websockets']:
			_ws.send_str('{0} has joined the chat'.format(uid))

		async for msg in ws:
			if msg.type == WSMsgType.TEXT:
				if msg.data == 'exit-chat':
					await ws.close()
				else:
					for _ws in self.request.app['websockets']:
						_ws.send_str('{"user": {0}, "msg": {1}}'.format(uid, msg.data))
			elif msg.type == WSMsgType.ERROR:
				log.debug('ws connection closed with exception {0}'.format(ws.exception()))

		self.request.app['websockets'].remove(ws)
		for _ws in self.request.app['websockets']:
			_ws.send_str('{0} has left the chat')
		log.debug('websocket connection closed')

		return ws











