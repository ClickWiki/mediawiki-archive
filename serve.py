#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# cd into the 'archive' directory and run this script.
#
# Taken from:
# https://gist.github.com/HaiyangXu/ec88cbdce3cdbac7b8d5

import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map={
    '.manifest': 'text/cache-manifest',
    '.html': 'text/html',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.svg': 'image/svg+xml',
    '.css': 'text/css',
    '.js': 'application/x-javascript',
    #'': 'application/octet-stream', # Default
    '': 'text/html'
}

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()

