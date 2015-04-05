import socket
import sys

# Setting everything up
tcpIP = raw_input("Host =")
tcpPort = 5005
bufferSize = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((tcpIP, tcpPort))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print "Connection address: " + str(addr)
    while True:
        data = conn.recv(bufferSize)
        print("(" + addr[0] + ")> " + str(data))
        if not data: 
            break
        msg = raw_input("(you)> ")
        if msg == "exit":
            sys.exit()
        conn.send(msg)
    conn.close()
