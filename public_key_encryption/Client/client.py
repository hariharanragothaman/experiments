import sys
import socket

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

class CLI(object):
    def __init__(self, host='127.0.0.1', port=9999):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = "Hello World"   
 
    def connect(self):
        try:
            self.sock.connect((self.host, self.port))
            self.sock.sendall("Client::OK")
        except:
            raise Exception("Unable to connect to Server")
    
    def close(self):
        self.sock.close()

    def send(self):
        try:
            self.sock.sendall(self.data)
        except:
            raise Exception("Cannot send data")

    def recieve(self):
        received_data = self.sock.recv(1024)
        print "\nThe data recieved is:", received_data

if __name__ == '__main__':
    client = CLI()
    client.connect()
    client.send()
    client.recieve()
