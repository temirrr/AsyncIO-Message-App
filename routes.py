from chat.views import ChatList, WebSocket

routes = [
	('GET', '/', ChatList, 'main'),
	('GET', '/ws', WebSocket, 'chat'),
]