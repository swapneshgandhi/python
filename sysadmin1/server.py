#!/usr/bin/python 
""" creates a simple web server to serve contents of current directory

    since PORT is 80, you need root access to run this. Change PORT to something
    like 8000 to run as ordinary user
"""

import SimpleHTTPServer
import SocketServer

PORT = 80

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
