import os
import time
import signal
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer


class Handler(SimpleHTTPRequestHandler):

    def log_message(self, format, *args):
        return

    def do_GET(self):
        global last_request
        last_request = time.time()
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()


def itimer_handler(signum, frame):

    try:
        if time.time() - last_request > 5:  # 5 minutes have passed at least with no request
            # do stuff now to log, kill, restart, etc.
            exit()
    except NameError:
        signal.signal(signal.SIGALRM, itimer_handler)


signal.signal(signal.SIGALRM, itimer_handler)
# check for a timeout every 10 seconds
signal.setitimer(signal.ITIMER_REAL, 10, 10)

os.chdir("core/scan")
server_address = ('', 6969)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()
