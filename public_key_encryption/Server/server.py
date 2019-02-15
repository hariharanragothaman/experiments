"""
Server Code
"""
import SocketServer
import subprocess

from Crypto.PublicKey import RSA
from Crypto import Random


# Generate Public Private Keys

random_generator = Random.new().read
private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()
pub_string = public_key.exportKey()

def generate_private_key():
    """
    Generate Private Key
    """
    priv_command =["openssl","genrsa", "-out", "private.pem", "1024"]
    subprocess.call(priv_command)

def obtain_public_key():
    """
    Get Public Key
    """
    pub_command =["openssl","rsa", "-in", "private.pem", "-pubout", "-out", "public.pem"]
    subprocess.call(pub_command)

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        #self.request.send("Clear Text Message:: Hi, who is this?")
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "\n{} wrote:{}".format(self.client_address[0], self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
