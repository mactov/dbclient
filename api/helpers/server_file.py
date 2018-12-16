import configparser

class ServerFileHandler:

    def __init__(self, server_list_file):
        self.file = server_list_file
        self.config_parser = configparser.ConfigParser()

    def read_all_server_names(self):
        servers = []
        try:
            self.config_parser.read(self.file)
            for server in self.config_parser.sections():
                servers.append({"server": server})
        except Exception as e:
            print(str(e))
        finally:
            return servers

    def read_one_server_info(self, server_name):
        server = {}
        try:
            self.config_parser.read(self.file)
            if server_name in self.config_parser.sections():
                server['server'] = server_name
                for k, v in self.config_parser[server_name].items():
                    server[k] = v
            return server
        except Exception as e:
            print(str(e))


    def append_one_server(self, server_name, server_data):
        try:
            self.config_parser[server_name] = {} 
            for k, v in server_data.items():
                self.config_parser[server_name][k] = v
            with open(self.file, 'w') as configfile:
                self.config_parser.write(configfile)
            return f"Server {server_name} was successfully added"
        except Exception as e:
            print(str(e))
            return None