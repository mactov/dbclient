from flask import Flask, request
from flask_restplus import Resource, Api, fields

from controllers.server_controller import ServerController

app = Flask(__name__)
api = Api(app, version='0.1', title='DBView API', 
          description='An API to connect to databases')

ns_servers = api.namespace('servers', description='List all servers')
ns_server = api.namespace('server', description='Individual server operations')

server = api.model('Server', {
    'engine': fields.String(required=True, description=''),
    'host': fields.String(required=True, description=''),
    'port': fields.String(required=True, description=''),
    'user': fields.String(required=True, description=''),
    'password': fields.String(required=True, description=''),
})

@ns_servers.route('/')
class ServerList(Resource):
    @ns_servers.doc()
    def get(self):
        sc = ServerController()
        return sc.get_list()


@ns_server.route('/<string:server_name>')
class Server(Resource):
    @ns_server.doc()
    def get(self, server_name):
        sc = ServerController()
        return sc.get(server_name)

    @ns_server.expect(server)
    @ns_server.doc()
    def put(self, server_name):
        sc = ServerController()
        return sc.put(server_name, api.payload)

    @ns_server.expect(server)
    @ns_server.doc()
    def delete(self, server_name):
        sc = ServerController()
        return sc.delete(server_name)

if __name__ == '__main__':
    app.run(debug=True)