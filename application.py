from rimbot.webserver.server import server
from rimbot.config import Config

server.config.from_object(Config)

if __name__ == "__main__":
    server.run(host='127.0.0.1',port='8090', debug=True)
