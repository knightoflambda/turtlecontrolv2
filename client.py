import socket
import msvcrt

class Client:
    def __init__(self):
        self.sock = socket.socket()
        self.hostname = "localhost"
        self.port = 7000

    def start_connection(self):
        self.sock.connect((self.hostname, self.port))
        print("[Client has successfully connected to " + self.hostname + "]")
        while True:
            keycode = ord(msvcrt.getch())
            if keycode == 119 or keycode == 115 or keycode == 97 or keycode == 100:
                self.sock.send(str(keycode).encode())
            elif keycode == 224:
                special_keyc = ord(msvcrt.getch())
                self.sock.send(str(special_keyc).encode())
            elif keycode == 27:
                self.sock.send(str(keycode).encode())
                self.sock.close()

c = Client()
c.start_connection()
        