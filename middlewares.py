from aiohttp import web
from aiohttp.web import middleware
from aiohttp_session import get_session
from settings import log

@middleware
async def authorize(request, handler):
	session = await get_session(request)
	if (not session.get('uid')) and (not request.path.startswith('/login')):
		url = request.app.router['login'].url_for()
		log.debug('redirecting to {}'.format(str(url)))
		raise web.HTTPFound(url)

	response = await handler(request)
	return response
