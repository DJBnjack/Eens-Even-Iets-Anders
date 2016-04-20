import tornado.ioloop
import tornado.web
import tornado.websocket

cl = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("wwwroot/index.html")

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")
        
def make_server():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/websocket', EchoWebSocket),
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': './wwwroot/'}),
    ])

if __name__ == "__main__":
    server = make_server()
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()