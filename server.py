import turtle
import socket

class Server:

    """ 
    119 w
    115 s
    97  a
    100 d
    27  ESC
            224 SPECIAL
            72  UP
            80  DOWN
            75  LEFT
            77  RIGHT
    """

    def __init__(self):
        self.hostname = "localhost"
        self.port = 7000

        self.screen = None
        self.turt = None
        self.sock = None

        self.speed = 10
        self.degree = 20

        self.s1 = 2
        self.s2 = 2
        self.s3 = 2

        self.colors = ["yellow", "blue", "green"]

    def create_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("Server")
        self.screen.setup(width=1024, height=768, startx=20, starty=20)
        self.turt = turtle.Turtle()
        self.turt.shape("turtle")

    def create_server(self):
        self.sock = socket.socket()
        self.sock.bind((self.hostname, self.port))
    
    def start_server(self):
        self.sock.listen()
        print("[Server is now receiving connections]")
        conn, addr = self.sock.accept()
        print("[Client connection accepted]")
        run = True
        i = 0
        while run:
            cmsg = conn.recv(1024)
            char = int(cmsg.decode())
            print("char: " + str(char))
            if char == 119:
                self.turt.forward(self.speed)
            elif char == 115:
                self.turt.backward(self.speed)
            elif char == 97:
                self.turt.left(self.degree)
            elif char == 100:
                self.turt.right(self.degree)
            elif char == 27:
                run = False
            elif char == 72:
                self.s1 = self.s1 + 1
                self.s2 = self.s2 + 1
                self.s3 = self.s3 + 1
                self.turt.turtlesize(self.s1, self.s2, self.s3)
            elif char == 80:
                self.s1 = self.s1 - 1
                self.s2 = self.s2 - 1
                self.s3 = self.s3 - 1
                self.turt.turtlesize(self.s1, self.s2, self.s3)
            elif char == 75:
                i = i + 1
                if i > len(self.colors) - 1:
                    i = 0
                self.turt.color(self.colors[i * -1])
            elif char == 77:
                i = i + 1
                if i > len(self.colors) - 1:
                    i = 0
                self.turt.color(self.colors[i])
            
        self.sock.close()
        self.screen.bye()

s = Server()
s.create_screen()
s.create_server()
s.start_server()