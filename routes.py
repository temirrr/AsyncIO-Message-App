from chat.views import GroupGeneral, GroupInterns, WebSocket
from auth.views import Login

routes = [
	('GET', '/', GroupGeneral, 'general'),
	('GET', '/interns', GroupInterns, 'interns'),
	('GET', '/ws', WebSocket, 'chat'),
	('GET', '/login', Login, 'login')
]