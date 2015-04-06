import asyncore
import socket

class Client(asyncore.dispatcher_with_send):

    def __init__(self, host, port):
        # Connect and other init things
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

        # Get and send msg
        self.out_buffer = raw_input("(you)> ")

    def handle_close(self):
        self.close()

    def handle_read(self):
        print("(" + tcpHostIP + ")> " + str(self.recv(1024)))
        self.out_buffer = raw_input("(you)> ")

tcpHostIP = raw_input("Host =")
tcpPort = 5005

client = Client(tcpHostIP, tcpPort)
asyncore.loop()
