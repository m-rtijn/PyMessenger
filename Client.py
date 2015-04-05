import socket
import time
import sys

# Setting everything up
tcpHostIP = raw_input("host =")
tcpPort = 5005
bufferSize = 1024

# Connecting to server
print("Connecting to server...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((tcpHostIP, tcpPort))

while True:
    msg = raw_input("(you)> ")
    if msg == "exit":
        sys.exit()
    sock.send(msg)
    backMsg = sock.recv(bufferSize)
    print("(" + tcpHostIP + ")> " + str(backMsg))

