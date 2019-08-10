import aiohttp_jinja2
from aiohttp import web, WSMsgType

import aiopg
import asyncio

from aiohttp_session import get_session

from settings import log

from chat.models import Message

import random
from datetime import datetime
from dateutil.tz import tzutc

class GroupGeneral(web.View):
	@aiohttp_jinja2.template('groups/general.html')
	async def get(self):
		session = await get_session(self.request)
		uid = session.get('uid')

		message = Message()
		messages = await message.get_messages('group_general')
		log.debug(f'group_general messages: {messages}')
		for message in messages['messages']:
			if message.get('uid') != None:
				if message['uid'] == uid:
					message['own'] = "yes"
		return messages

class GroupInterns(web.View):
	@aiohttp_jinja2.template('groups/interns.html')
	async def get(self):
		session = await get_session(self.request)
		uid = session.get('uid')

		message = Message()
		messages = await message.get_messages('group_interns')
		log.debug(f'group_interns messages: {messages}')
		for message in messages['messages']:
			if message.get('uid') != None:
				if message['uid'] == uid:
					message['own'] = "yes"
		return messages

class WebSocketGeneral(web.View):
	async def get(self):
		message = Message()
		ws = web.WebSocketResponse()
		await ws.prepare(self.request)

		session = await get_session(self.request)
		uid = session.get('uid')

		#broadcast joining of new user
		join_msg = ('"%s has joined the chat"' % (uid)) #message
		for _ws in self.request.app['websockets_general']:
			await _ws.send_str(join_msg)
		self.request.app['websockets_general'].append(ws)

		#send client's id to this particular client for frontend
		await ws.send_str('{"myID": "%s"}' % (uid))

		async for msg in ws:
			if msg.type == WSMsgType.TEXT:
				if msg.data == 'exit-chat':
					await ws.close()
				else:
					t = datetime.now(tzutc())
					format_str = "%H:%M"
					t_string = t.strftime(format_str)

					json_message = '{{"from_user": "yes",\
									  "uid": "{0}",\
									  "msg": "{1}",\
									  "time": "{2}"}}'.format(uid, msg.data, t_string)
					log.debug(json_message)
					await message.send_message('group_general', json_message)

					for _ws in self.request.app['websockets_general']:
						await _ws.send_str('{"user": "%s", "msg": "%s", "time": "%s"}' % (uid, msg.data, t_string))
			elif msg.type == WSMsgType.ERROR:
				log.debug('ws connection closed with exception {0}'.format(ws.exception()))

		#broadcast leaving of the user
		self.request.app['websockets_general'].remove(ws)
		leave_msg = ('"%s has left the chat"' % (uid)) #message
		for _ws in self.request.app['websockets_general']:
			await _ws.send_str(leave_msg)

		return ws

class WebSocketInterns(web.View):
	async def get(self):
		message = Message()
		ws = web.WebSocketResponse()
		await ws.prepare(self.request)

		session = await get_session(self.request)
		uid = session.get('uid')

		#broadcast joining of new user
		join_msg = ('"%s has joined the chat"' % (uid)) #message
		for _ws in self.request.app['websockets_interns']:
			await _ws.send_str(join_msg)
		self.request.app['websockets_interns'].append(ws)

		#send client's id to this particular client for frontend
		await ws.send_str('{"myID": "%s"}' % (uid))

		async for msg in ws:
			if msg.type == WSMsgType.TEXT:
				if msg.data == 'exit-chat':
					await ws.close()
				else:
					t = datetime.now(tzutc())
					format_str = "%H:%M"
					t_string = t.strftime(format_str)

					json_message = '{{"from_user": "yes",\
									  "uid": "{0}",\
									  "msg": "{1}",\
									  "time": "{2}"}}'.format(uid, msg.data, t_string)
					log.debug(json_message)
					await message.send_message('group_interns', json_message)

					for _ws in self.request.app['websockets_interns']:
						await _ws.send_str('{"user": "%s", "msg": "%s", "time": "%s"}' % (uid, msg.data, t_string))
			elif msg.type == WSMsgType.ERROR:
				log.debug('ws connection closed with exception {0}'.format(ws.exception()))

		#broadcast leaving of the user
		self.request.app['websockets_interns'].remove(ws)
		leave_msg = ('"%s has left the chat"' % (uid)) #message
		for _ws in self.request.app['websockets_interns']:
			await _ws.send_str(leave_msg)

		return ws











