from argparse import ArgumentParser
from flask import Flask


app = Flask(__name__)


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + 'api.py' + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8080, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    arg_parser.add_argument('--host', default='0.0.0.0', help='ip')
    args = arg_parser.parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)

