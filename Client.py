import socket
import time
import sys

# Setting everything up
tcpHostIP = raw_input("tcpHostIP =")
tcpPort = 5005
bufferSize = 1024

# Connecting to server
print("Connecting to server...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((tcpHostIP, tcpPort))

while True:
    msg = raw_input("(you)> ")

    # Check if the msg is an internal command
    if msg == "exit":
        sock.send("--LEFT--")
        break

    # Sending
    try:
        sock.send(msg)
    except:
        print("Error sending message, terminating connection")
        break

    # Receiving
    try:
        recvMsg = sock.recv(bufferSize)
    except:
        print("Error receiving message, terminating connection")
        break
    
    # Check for left message
    try:
        if recvMsg == "--LEFT--":
            print("Server has left, terminating connection")
            break
    except:
        pass

    # Print the recvMsg
    print("(" + tcpHostIP + ")> " + str(recvMsg))

sock.close()
time.sleep(0.1)
sys.exit()

