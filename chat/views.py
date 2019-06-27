import aiohttp_jinja2
from aiohttp import web, WSMsgType

import aiopg
import asyncio

from aiohttp_session import get_session

from settings import log

from chat.models import Message

import random

class GroupGeneral(web.View):
	@aiohttp_jinja2.template('groups/general.html')
	async def get(self):
		message = Message()
		message_list = await message.get_messages('group_general')
		log.debug(f'messages are: {message_list}')
		messages = message_list
		return messages

class GroupInterns(web.View):
	@aiohttp_jinja2.template('groups/interns.html')
	async def get(self):
		return {}

class WebSocketGeneral(web.View):
	async def get(self):
		db_str = 'dbname=postgres user=postgres password=timkabro7 host=127.0.0.1 port=5002'

		ws = web.WebSocketResponse()
		await ws.prepare(self.request)

		session = await get_session(self.request)
		uid = session.get('uid')

		pool = await aiopg.create_pool(db_str)
		async with pool.acquire() as conn:
			async with conn.cursor() as cur:
				#broadcast joining of new user
				join = ('"%s has joined the chat"' % (uid))
				json_join = '{{"msg": {0}}}'.format(join)
				await cur.execute("INSERT INTO group_general (messages) VALUES ('{0}');".format(json_join))

				for _ws in self.request.app['websockets_general']:
					await _ws.send_str(join)
				self.request.app['websockets_general'].append(ws)

				#send client's id to this particular client for frontend
				log.debug('before sending UID')
				await ws.send_str('{"myID": "%s"}' % (uid))
				log.debug('after sending UID')

				async for msg in ws:
					if msg.type == WSMsgType.TEXT:
						if msg.data == 'exit-chat':
							await ws.close()
						else:
							for _ws in self.request.app['websockets_general']:
								await _ws.send_str('{"user": "%s", "msg": "%s"}' % (uid, msg.data))
					elif msg.type == WSMsgType.ERROR:
						log.debug('ws connection closed with exception {0}'.format(ws.exception()))

				self.request.app['websockets_general'].remove(ws)
				leave = ('"%s has left the chat"' % (uid))
				json_leave = '{{"from_user": "yes", "msg": {0}}}'.format(leave)
				await cur.execute("INSERT INTO group_general (messages) VALUES ('{0}');".format(json_leave))

				for _ws in self.request.app['websockets_general']:
					await _ws.send_str('"%s" has left the chat' % (uid))
				log.debug('websocket connection closed')

				return ws

class WebSocketInterns(web.View):
	async def get(self):
		ws = web.WebSocketResponse()
		await ws.prepare(self.request)

		session = await get_session(self.request)
		uid = session.get('uid')

		#broadcast joining of new user
		for _ws in self.request.app['websockets_interns']:
			await _ws.send_str('"%s" has joined the chat' % (uid))
			log.debug('"%s" has joined the chat' % (uid))
		self.request.app['websockets_interns'].append(ws)

		#send client's id to this particular client for frontend
		log.debug('before sending UID')
		await ws.send_str('{"myID": "%s"}' % (uid))
		log.debug('after sending UID')

		async for msg in ws:
			if msg.type == WSMsgType.TEXT:
				if msg.data == 'exit-chat':
					await ws.close()
				else:
					for _ws in self.request.app['websockets_interns']:
						await _ws.send_str('{"user": "%s", "msg": "%s"}' % (uid, msg.data))
			elif msg.type == WSMsgType.ERROR:
				log.debug('ws connection closed with exception {0}'.format(ws.exception()))

		self.request.app['websockets_interns'].remove(ws)
		for _ws in self.request.app['websockets_interns']:
			await _ws.send_str('"%s" has left the chat' % (uid))
		log.debug('websocket connection closed')

		return ws











