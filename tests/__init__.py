from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread

from webium.driver import close_driver

httpd = HTTPServer(('', 0), SimpleHTTPRequestHandler)
PORT = httpd.server_address[1]


def setup_package():
    print("serving at port " + str(PORT))
    thread = Thread(target=lambda: httpd.serve_forever())
    thread.daemon = True
    thread.start()


def teardown_package():
    close_driver()


def get_url(suffix=''):
    return 'http://localhost:{0}/tests/pages/{1}'.format(PORT, suffix)
