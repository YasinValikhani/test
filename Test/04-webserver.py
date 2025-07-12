from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello! I'm a simple web server :)</h1>")

# آدرس و پورت سرور
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)

print("Server is running on http://localhost:8000")
httpd.serve_forever()
