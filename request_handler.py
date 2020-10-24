#! /usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        request_path = self.path

        print('\n----- Request Start ----->\n')
        print(request_path)
        print(self.request_version)
        print(self.headers)
        print(self.client_address)
        print('\n<----- Request End -----\n')
        response = '(Response to %s)' % self.client_address[0]
        self.send_response(200, response)
        
    def do_POST(self):

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)
        request_headers = self.headers
        print(request_headers)
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body)
        response = '%s\n(Response to %s)' % (post_body, self.client_address[0])
        print('\n<----- Request End -----\n')
        self.send_response(200, response)

def main():
    port = 5053
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

if __name__=='__main__':
    main()