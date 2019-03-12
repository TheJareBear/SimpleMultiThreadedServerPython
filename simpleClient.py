#!/usr/bin/env python3

import socket
import os
import threading

dip = input("IP to connect to: ")
dport = int(input("Port to connect to: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((dip, dport))
except:
	print("Server not found")
	exit()

while 1:
	try:
		data = s.recv(2048).decode()
	except:
		print("Socket connection failed, exiting")
		exit()
	os.system("clear")
	print(data)
