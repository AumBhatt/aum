#!/usr/bin/env python3

import socket
from time import sleep
import os

clear = lambda: os.system('clear')
clear()

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 4998        # Port to listen on (non-privileged ports are > 1023)

sample = "sendir,1:1,0,37000,1,1,166,167,20,63,20,64,19,64,19,23,19,22,20,23,19,23,19,23,19,64,19,64,19,64,19,23,19,23,19,23,19,23,19,23,19,22,20,64,19,23,19,23,19,\
23,19,23,19,23,19,23,19,63,20,23,19,64,19,63,20,64,19,63,20,64,19,63,20,1729,166,167,20,64,19,64,19,64,19,23,19,23,19,23,19,23,19,23,19,64,19,64,19,64,19,\
23,19,23,19,23,19,23,19,23,21,21,19,64,19,23,19,23,19,23,19,23,19,23,19,23,19,64,19,23,19,63,20,63,20,64,19,63,20,64,19,64,19,3692"
def mySocket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print("\n-----------------------------------", "\nListening py3 @http://127.0.0.1:" + str(PORT), "\n-----------------------------------")
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data, type(data))
                if str(data, 'utf-8') == 'get_IRL\r':
                    conn.send(bytes('IR Learner Enabled', 'utf-8'))
                    print("Sending sample command")
                    conn.send(bytes(sample, 'utf-8'))
                else:
                    conn.send(bytes('IR Learner Disabled', 'utf-8'))
                # print("echoing.....")
            print(" > Client Disconncted")
    mySocket()
mySocket()