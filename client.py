from socket import *
import sys

serverIP = '44.195.93.105'
serverPort = 12003
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

file = open(sys.argv[1], "r")
data = file.read()

clientSocket.send(data.encode())
modifiedSentence = clientSocket.recv(1024)
result = "\nFrom the server:\n" + modifiedSentence.decode()
print(result)
clientSocket.close()