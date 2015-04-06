# Made by Tijndagamer and released under the MIT license
# Copyright 2015

import socket
import time
import sys

def Client():
    hostIP = raw_input("Host =")
    port = 5005
    bufferSize = 1024

    # Connecting to server
    print("Connecting to server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostIP, port))

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
            print("Error sending message, terminating connection.")
            break

        # Receiving
        try:
            recvMsg = sock.recv(bufferSize)
        except:
            print("Error receiving message, terminating connection.")
            break
        
        # Check for left message
        try:
            if recvMsg == "--LEFT--":
                print("Server has left, terminating connection.")
                break
        except:
            pass

        # Print recvMsg
        print("(" + hostIP + ")> " + str(recvMsg))

    sock.close()
    time.sleep(0.1)
    return

def Server():
    hostIP = raw_input("Host =")
    port = 5005
    bufferSize = 1024

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((hostIP, port))
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
        choice = raw_input("Do you want to keep listening for new connections or stop? y/n")
        if choice == "y":
            pass
        else:
            return

def main():
    print("PyMessenger")
    while True:
        cmd = raw_input(">")
        cmd = cmd.lower()
        if cmd == "client":
            Client()
        elif cmd == "server":
            Server()
        elif cmd == "exit":
            sys.exit()

main()
