import http.server
import socketserver


class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Hello World!", "utf8"))
            return None
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 5000
handler = HttpRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    