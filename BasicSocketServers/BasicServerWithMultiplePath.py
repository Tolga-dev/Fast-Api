import http.server
import socketserver
import urllib.parse

class HttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == "/":
            self.wfile.write(bytes("Hello, World!", "utf8"))
        elif self.path == "/test":
            self.wfile.write(bytes("This is a test page.", "utf8"))
        else:
           self.wfile.write(bytes("This page does not exist.", "utf8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode("utf-8"))
        print(post_data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("POST request received.", "utf8"))

PORT = 5000
handler = HttpRequestHandler

if __name__ == "__main__":
    with socketserver.TCPServer(("localhost", PORT), handler) as httpd:
        print("Serving at port:", PORT)
        httpd.serve_forever()

