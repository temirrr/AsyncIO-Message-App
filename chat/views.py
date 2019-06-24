import aiohttp_jinja2
from aiohttp import web, WSMsgType

from aiohttp_session import get_session

from settings import log

import random

class ChatList(web.View):
	@aiohttp_jinja2.template('index.html')
	async def get(self):
		return {}


class WebSocket(web.View):
	async def get(self):
		ws = web.WebSocketResponse()
		await ws.prepare(self.request)

		session = await get_session(self.request)

		#id generation
		uid = 'user{0}'.format(random.randint(1, 1001))
		uids = self.request.app['uids']
		while uid in uids:
			uid = 'user{0}'.format(random.randint(1, 1001))
		uids.append(uid)
		self.request.app['uids'] = uids

		#broadcast joining of new user
		for _ws in self.request.app['websockets']:
			await _ws.send_str('"%s" has joined the chat' % (uid))
			log.debug('"%s" has joined the chat' % (uid))
		self.request.app['websockets'].append(ws)

		#send client's id to this particular client for frontend
		log.debug('before sending UID')
		await ws.send_str('{"myID": "%s"}' % (uid))
		log.debug('after sending UID')

		async for msg in ws:
			if msg.type == WSMsgType.TEXT:
				if msg.data == 'exit-chat':
					await ws.close()
				else:
					for _ws in self.request.app['websockets']:
						await _ws.send_str('{"user": "%s", "msg": "%s"}' % (uid, msg.data))
			elif msg.type == WSMsgType.ERROR:
				log.debug('ws connection closed with exception {0}'.format(ws.exception()))

		self.request.app['websockets'].remove(ws)
		for _ws in self.request.app['websockets']:
			await _ws.send_str('"%s" has left the chat' % (uid))
		log.debug('websocket connection closed')

		return ws











