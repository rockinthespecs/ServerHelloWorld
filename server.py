import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"
conf = {
         '/': {
                 'tools.sessions.on': True,
         },
         '/static': {
                 'tools.staticdir.on': True,
                 'tools.staticdir.dir': './public'
         },
        'global': {
                'server.socket_host': '0.0.0.0',
                'server.socket_port': 80,
                'server.thread_pool':10
        }
}
if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/', conf)


