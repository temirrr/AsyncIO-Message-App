from aiohttp import web
from aiohttp_session import get_session
import random
from settings import log

def redirect(request, router_name):
	url = request.app.router[router_name].url_for()
	log.debug('redirecting to {}'.format(url))
	raise web.HTTPFound(url)

'''middleware redirects to Login in case there is no 'uid' 
found in the request's session'''
class Login(web.View):
	async def get(self):
		session = await get_session(self.request)

		uid = 'user{0}'.format(random.randint(1, 1001))
		uids = self.request.app['uids']
		while uid in uids:
			uid = 'user{0}'.format(random.randint(1, 1001))
		uids.append(uid)
		self.request.app['uids'] = uids

		session['uid'] = uid
		log.debug(uid)

		redirect(self.request, 'general')