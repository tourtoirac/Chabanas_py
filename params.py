server_host='127.0.0.1'
server_port=33333
user_email='chins@free.fr'
user_password='123456'
user_nickname='Chins'

class CH_Server:
    def __init__(self,host,port):
        self.HOST=host
        self.PORT=port
        
class CH_user:
    def __init__(self,email,password='',nickname=''):
        self.email=email
        self.password=password
        self.nickname=nickname

ch_user=CH_user(user_email, user_password, user_nickname)
ch_server=CH_Server(server_host,int(server_port))