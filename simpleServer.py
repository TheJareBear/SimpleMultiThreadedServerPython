#!/usr/bin/env python3

import socket
import os
import threading
from time import sleep
 
tick = 32 #server tick

def main():
	#start the listening thread
	port = int(input("Port to listen on: "))
	thread = threading.Thread(target=listener, args=(port,))
	thread.daemon = True
	thread.start()

	#keep process alive until finished
	input("Press enter when finished")

def listener(port):
	if port < 1024 or port > 65535:
		print("INVALID PORT")
		return
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		#print("Starting listener....")
		try:
			s.bind(("127.0.0.1", port))
		except:
			print("Port {} already in use".format(port))
			return
		
		#print("Socket bind complete")
		s.listen()
		print("\n\nListening on port " + str(port))

		while 1:
			
			conn, addr = s.accept()

			print('New session opened.')
			print('Connected by ' + addr[0] + ':' + str(addr[1]))

			thread = threading.Thread(target=clientHandler, args=(conn,addr))
			thread.daemon = True
			thread.start()


def clientHandler(session, address):
	clientInfo = f"{address[0]}:{address[1]}"
	while 1: #continue to send the client information
		try:
			session.sendall(clientInfo.encode())
			#print(f"sent to client at {address[0]}")
		except:
			print("Send to socket failed, connection closed")
			session.close()
			return #return thread

		sleep(1/tick)


if __name__ == '__main__':
	main()


