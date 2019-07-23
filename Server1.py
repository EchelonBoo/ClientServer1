#SERVER 1

#Group C
#Bethany Hanrahan - K00230399
#David Chiemeka - K00228312

import socket														#this allows you to use python's socket library

host = socket.gethostbyname(socket.gethostname())					#this gets the ip address of the network you are on and sets it as the host 
port = 13232														#this is set by the programmer, it is the port number we will be using to connect the client and server
error = 'You did not enter all letters, try again!' 				#create an error message to be used later

print('The host IP is:', host)										#prints the host to the user
print('The port number is: ', port)									#prints the port number to the user

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server1:  #create a socket object and specify that we're using IPv4 and TCP
	server1.bind((host, port))										#this associates the socket with the specific host address and port num
	server1.listen()												#this lets the server accept connections, the server is listening for a connection
	connection, address = server1.accept()							#this creates a new socket object and allows a connection and address to be passed to it from the client
	with connection:
		print('Connection Address', address)						#prints back to the user on the server window, the connection address used when connected to the client
		while True:													#enter a while loop
			info = connection.recv(1024)							#this reads the data from the client and saves it in the info variable
			if info.isalpha():										#takes the info variable and calls the built in isalpha python function
				print('Message Recieved: ', info.decode())			#if it is comprised of all letters then it prints the message to the server side			
				connection.sendall(info)							#gets the user to enter another string on the client side
			else:													#if the string entered isn't all letters
				print('Error, not all characters you entered were letters.') #print the error message on the client side and let them try again
				connection.sendall(error.encode())