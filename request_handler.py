#! /usr/bin/python3

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        request_path = self.path

        print('\n----- Request Start ----->\n')
        print(request_path)
        print(self.headers)
        content_len = int(self.headers.get('Content-Length'))
        get_body = self.rfile.read(content_len)
        print(get_body)
        print('<----- Request End -----\n')
        self.send_response(200)
        
    def do_POST(self):

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)
        request_headers = self.headers
        print(request_headers)
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body)
        print('<----- Request End -----\n')
        self.send_response(200)

def main():
    port = 5053
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever

if __name__=='__main__':
    main()