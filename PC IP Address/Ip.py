import socket

check = input("Do you want to get your IP Address: Y/N").upper()

if check == "Y":
	print(socket.gethostbyname(socket.gethostname()))

else:
	exit()