from helpers.server_file import ServerFileHandler
from helpers.setup import server_list_file


class ServerController():

    def get_list(self):
        sfh = ServerFileHandler(server_list_file())
        servers = sfh.read_all_server_names()
        if servers:
            return servers, 200
        else:
            return servers, 404

    def get(self, server_name):
        sfh = ServerFileHandler(server_list_file())
        server = sfh.read_one_server_info(server_name)
        if server:
            return server, 200
        else:
            return server, 404

    def put(self, server_name, payload):
        sfh = ServerFileHandler(server_list_file())
        servers = sfh.read_all_server_names()
        if server_name in [serv['server'] for serv in servers]:
            msg = sfh.update_one_server(server_name, payload)
            if msg:
                return msg, 204
            else:
                return f"Could not update {server_name}", 500
        else:
            msg = sfh.append_one_server(server_name, payload)
            if msg:
                return msg, 201
            else:
                return f"Could not save {server_name}", 500

    def delete(self, server_name):
        sfh = ServerFileHandler(server_list_file())
        servers = sfh.read_all_server_names()
        if server_name in [serv['server'] for serv in servers]:
            msg = sfh.delete_one_server(server_name)
            if msg:
                return msg, 204
            else:
                return f"Could not delete {server_name}", 500
        else:
            return f"Could not delete {server_name}", 404
