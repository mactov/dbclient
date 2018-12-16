from flask import Flask, request
from flask_restplus import Resource, Api, fields

from helpers.server_file import ServerFileHandler
from helpers.setup import server_list_file

app = Flask(__name__)
api = Api(app, version='0.1', title='DBView API', description='An API to connect to databases')

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
    @ns_server.doc()
    def get(self):
        sfh = ServerFileHandler(server_list_file())
        servers = sfh.read_all_server_names()
        if servers:
            return servers, 200
        else:
            return servers, 404


@ns_server.route('/<string:server_name>')
class Server(Resource):
    @ns_server.doc()
    def get(self, server_name):
        sfh = ServerFileHandler(server_list_file())
        server = sfh.read_one_server_info(server_name)
        if server:
            return server, 200
        else:
            return server, 404

    @ns_server.expect(server)
    @ns_server.doc()
    def put(self, server_name):
        sfh = ServerFileHandler(server_list_file())
        servers = sfh.read_all_server_names()
        if server_name in [serv['server'] for serv in servers]:
            return "Server already exists", 403
        else:
            msg = sfh.append_one_server(server_name, api.payload)
            if msg:
                return msg, 201
            else:
                return f"Could not save {server_name}", 500


if __name__ == '__main__':
    app.run(debug=True)