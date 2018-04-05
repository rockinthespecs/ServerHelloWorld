import cherrypy

class ScoutServer(object):
    @cherrypy.expose
    def index(self):
        return '''
            <html>
                <head>
                    <title>{0}</title>
                </head>
            </html>'''.format("Hello World")
'''

conf = {
         '/': {
                 'tools.sessions.on': True,
                 'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/static': {
                 'tools.staticdir.on': True,
                 'tools.staticdir.dir': './public'
         },
        'global': {
                'server.socket_host': '0.0.0.0',
                'server.socket_port': 80
        }
}

cherrypy.quickstart(ScoutServer(), '/', conf)
'''