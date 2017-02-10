#!/usr/bin/python

## Run the following command to generate your certificate file
# openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

# Create a symlink to the config json file
# mkdir -p ministryofjustice/cla_cait_intervention/master
# ln -s cla_cait_intervention_config.json ministryofjustice/cla_cait_intervention/master/.

# Add following line to hosts file (/etc/hosts)
# 127.0.0.1       raw.githubusercontent.com

# Flush cache
# sudo dscacheutil -flushcache

# Run as root
# sudo python https.py

import os
import BaseHTTPServer, SimpleHTTPServer
import ssl 
import sys 

cdir = os.getcwd()
os.chdir(cdir)

certFile = cdir + '/server.pem'

httpd = BaseHTTPServer.HTTPServer(('localhost', 443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile=certFile, server_side=True)
httpd.serve_forever()