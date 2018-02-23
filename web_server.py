from flask import Flask


class WebServer:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        def teste():
            return 'foi!'
