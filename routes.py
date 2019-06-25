from chat.views import GroupGeneral, GroupInterns, WebSocketGeneral, WebSocketInterns
from auth.views import Login

routes = [
	('GET', '/', GroupGeneral, 'general'),
	('GET', '/interns', GroupInterns, 'interns'),
	('GET', '/wsgeneral', WebSocketGeneral, 'wsgeneral'),
	('GET', '/wsinterns', WebSocketInterns, 'wsinterns'),
	('GET', '/login', Login, 'login')
]