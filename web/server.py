import http.server
import socketserver
import os
from pathlib import Path

PORT = 8080
# Convert ~ to absolute path
DIRECTORY = str(Path("/home/aramjonghu/OvenPlayer/web/").resolve())

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/webserver.html'
        
        # Convert path to absolute filesystem path
        file_path = os.path.join(DIRECTORY, self.path.lstrip('/'))
        
        # Check if file exists
        if os.path.exists(file_path):
            self.send_response(200)
            if file_path.endswith('.html'):
                self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, f"File not found: {self.path}")
            return

handler = MyHttpRequestHandler
handler.directory = DIRECTORY

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print(f"Serving files from: {DIRECTORY}")
    httpd.serve_forever()
