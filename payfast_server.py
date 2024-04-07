import http.server
import urllib.parse

SANDBOX_MODE = True

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        pfData = {}
        postData = post_data.split('&')
        for item in postData:
            key, value = item.split('=')
            pfData[key] = value
        pf_param_string = ""
        for key in pfData:
            if key != 'signature':
                pf_param_string += key + "=" + urllib.parse.quote_plus(pfData[key].replace("+", " ")) + "&"
        pf_param_string = pf_param_string[:-1]

        # Now you can use pf_param_string for further processing
        # For demonstration, let's just print it
        print(pf_param_string)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')

def run(server_class=http.server.HTTPServer, handler_class=RequestHandler, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
