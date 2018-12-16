import configparser

from flask import Flask, request
from flask_restplus import Resource, Api, fields

from setup import server_list_file


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
        config = configparser.ConfigParser()
        servers = []
        try:
            config.read(server_list_file())
            for server in config.sections():
                servers.append({"server": server})
        except Exception as e:
            print(str(e))
        finally:
            return servers, 200


@ns_server.route('/<string:server_name>')
class Server(Resource):
    @ns_server.doc()
    def get(self, server_name):
        config = configparser.ConfigParser()
        server = {}
        try:
            config.read(server_list_file())
            if server_name in config.sections():
                server['server'] = server_name
                for k, v in config[server_name].items():
                    server[k] = v
                return server, 200
            else:
                return server, 404
        except Exception as e:
            print(str(e))

    @ns_server.expect(server)
    @ns_server.doc()
    def put(self, server_name):
        config = configparser.ConfigParser()
        try:
            config.read(server_list_file())
            if server_name in config.sections():
                return "Server already exists", 403
            else:
                config[server_name] = {} 
                for k, v in api.payload.items():
                    config[server_name][k] = v
                with open(server_list_file(), 'w') as configfile:
                    config.write(configfile)
                return f"Server {server_name} was successfully added", 201
        except Exception as e:
            print(str(e))        


if __name__ == '__main__':
    app.run(debug=True)