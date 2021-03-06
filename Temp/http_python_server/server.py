## Code from https://os.mbed.com/teams/Cloud-Hackathon/code/HTTP-Python-Demo/
#----------DEMO--------

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import socket
 
class MyHandler(BaseHTTPRequestHandler):
#class MyTCPHandler(SocketServer.BaseRequestHandler):
    
    # def handle(self):
    #     print "testing"
    #     print self.request.recv(1024).strip();
    
    # HTTP REQUESTS HERE
      def do_POST(self):
        print("testing")
        content = b"POST: Hello, Mbed!"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)
        return
        
      def do_GET(self):
        content = b"GET: Hello, Mbed!"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)
        return
                
def do_PUT(self):
    content = b"PUT: Hello, Mbed!"
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.send_header('Content-Length', len(content))
    self.end_headers()
    self.wfile.write(content)
    return
 
##----------------------------------------------
def run():
    httpd = HTTPServer(('10.25.1.101', 8080), MyHandler)
    print "HTTP server running on port 8080"
    print "Your IP address is: ", socket.gethostbyname(socket.gethostname())
    httpd.serve_forever()
 
if __name__ == '__main__':
    run()
    # HOST, PORT = 'localhost', 8080
    # server = SocketServer.TCPServer((HOST,PORT), MyTCPHandler)
    # 
    # server.serve_forever()
