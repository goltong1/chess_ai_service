import json
from channels.generic.websocket import WebsocketConsumer
from Chess_ai.chess_ai_best_find import *
#웹소켓 class instance를 만들어요
class ChatConsumer(WebsocketConsumer):
    #웹소켓에 연결, 혹은 연결 해제해요
    def connect(self):
        self.accept()
    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
    	#json으로 채팅 메시지를 받아요 
        text_data_json = json.loads(text_data)
        board = list(text_data_json['board'])
        turn= bool(text_data_json['turn'])
        n= int(text_data_json['n'])
	    #json 객체를 인코딩 해서 보내요
        bestindex=find_best_move(board,turn,n)
        message=json.dumps(bestindex)
        self.send(message)
