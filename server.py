import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_server():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    server = make_server()
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()