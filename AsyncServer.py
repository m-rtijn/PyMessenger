import asyncore
import socket

class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)

    def handle_accept(self):
        socket, address = self.accept()
        print("Incoming connection from " + str(address))
        SendHandler(socket)

class SendHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        print("(" + "other" + ")> " + self.recv(1024))
        self.out_buffer = raw_input("(you)> ")


server = Server("127.0.0.1", 5005)
asyncore.loop()
