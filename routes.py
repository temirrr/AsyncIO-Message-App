from chat.views import GroupGeneral, GroupInterns, WebSocket

routes = [
	('GET', '/', GroupGeneral, 'general'),
	('GET', '/interns', GroupInterns, 'interns'),
	('GET', '/ws', WebSocket, 'chat'),
]