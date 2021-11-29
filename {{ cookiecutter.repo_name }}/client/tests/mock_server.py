"""Mock a server test client."""

from threading import Thread
from uuid import uuid4

import requests
from flask import Flask, jsonify, request


class MockServer(Thread):
    """Mock server."""

    def __init__(self, port=5000):
        """Get a new mock server."""
        super().__init__()
        self.port = port
        self.app = Flask(__name__)
        self.url = f"http://localhost:{self.port}"
        self.app.add_url_rule("/shutdown", view_func=self._shutdown_server)

    @staticmethod
    def _shutdown_server():
        """Shutdown the server."""
        if "werkzeug.server.shutdown" not in request.environ:
            raise RuntimeError("Not running the development server")
        request.environ["werkzeug.server.shutdown"]()
        return "Server shutting down..."

    def shutdown_server(self):
        """Shutdown the server."""
        requests.get(f"http://localhost:{self.port}/shutdown")
        self.join()

    def add_callback_response(self, url, callback, methods=("GET",)):
        """Add callback to url."""
        callback.__name__ = str(uuid4())
        self.app.add_url_rule(url, view_func=callback, methods=methods)

    def add_json_response(self, url, serializable, methods=("GET",)):
        """Add json response to url."""
        def callback():
            return jsonify(serializable)

        self.add_callback_response(url, callback, methods=methods)

    def run(self):
        """Run the server."""
        self.app.run(port=self.port)
