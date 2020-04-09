import http.server
import socketserver
import os

PORT = 8000

# web_dir = os.path.join(os.path.dirname(__file__), 'web')
web_dir = os.path.join(os.path.dirname(__file__), './')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
# SSL
# httpd.socket = ssl.wrap_socket (httpd.socket, 
#         keyfile="path/to/key.pem", 
#         certfile='path/to/cert.pem', server_side=True)
print("serving at port", PORT)
httpd.serve_forever()



# Command version
# python -m  http.server 2020 --directory <dir>
