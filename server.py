from socket import *

a = 0
b = 0
line = 1
serverPort = 12003
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    connectionInfo = "Connect by: " + str(addr)

    sentence = connectionSocket.recv(1024).decode()
    wordslist = sentence.split()
    lines = sentence.split('\n')

    for i in sentence:
        a += 1

    capitalizedSentence = connectionInfo + "\n" + "Total character(s) is(are): " + str(a) + "\n" + "Total line(s) is(are): " + str(len(lines)) + "\n" + "Total word(s) is(are): " + str(len(wordslist))
    connectionSocket.send(capitalizedSentence.encode())

    print(connectionInfo)
    print("Connection done \nThe server is ready to receive")
    connectionSocket.close()
