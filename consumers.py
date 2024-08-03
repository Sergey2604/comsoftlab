from channels.generic.websocket import WebsocketConsumer

class MyWebSocket(WebsocketConsumer):
    def connect(self):
        # Accept the connection
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        # Handle incoming message from client
        pass

    def disconnect(self, close_code):
        # Close the connection
        pass
