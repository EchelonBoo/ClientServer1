#CLIENT 2

#Group C
#Bethany Hanrahan - K00230399
#David Chiemeka - K00228312

import socket															#this allows you to use python's socket library

Client = socket.socket()												#create a socket object and let it equal the the varable Client
Client.connect((socket.gethostbyname(socket.gethostname()), 13232))		#get the IP address for the host and set the port number
while True:																#enters while loop
	string = input("Please enter a string: ")							#gets the user to enter a string and save it in a variable
	Client.send(string.encode())										#send the user's input to the server to check if it is all letters
	print("The server says:", Client.recv(1024).decode())				#sends the message from the server repeating back out what you have entered if it was all letters, otherwise the error message
	
	
	
	
