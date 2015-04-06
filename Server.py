# Made by Tijndagamer and released under the MIT license
# Copyright 2015

import socket
import time
import sys

# Setting everything up
tcpHostIP = raw_input("tcpHostIP =")
tcpPort = 5005
bufferSize = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((tcpHostIP, tcpPort))
sock.listen(1)

while True:
    print("Waiting for connection...")

    # Connecting
    conn, addr = sock.accept()
    print "Connection address: " + str(addr)

    while True:

        # Receiving
        recvMsg = conn.recv(bufferSize)
        if not recvMsg: 
            break
        
        # Check for left message
        try:
            if recvMsg == "--LEFT--":
                print("Client has left, terminating connection.")
                conn.close()
                break
        except:
            pass

        # Print recvMsg
        print("(" + addr[0] + ")> " + str(recvMsg))

        # Sending
        msg = raw_input("(you)> ")

        # Check if message is an internal command
        if msg == "exit":
            conn.send("--LEFT--")
            conn.close()
            break

        # Send msg
        try:
            conn.send(msg)
        except:
            print("Error sending message, terminating connection.")
            break
    conn.close()
    print("Connection closed.")
