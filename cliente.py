from socket import *
from colorama import Fore

# serverName = input('Digite o endereco IP de destino:')

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    resposta_servidor = clientSocket.recv(1024).decode()
    resposta_servidor = resposta_servidor.replace("[", "")
    resposta_servidor = resposta_servidor.replace("]", "")
    resposta_servidor = resposta_servidor.replace("_", "")
    resposta_servidor = resposta_servidor.replace('"', "")
    print(resposta_servidor)

    print("\n")
    palavra = clientSocket.recv(1024).decode()
    print('Palavra:', palavra)

    if "Parabens" in palavra or "infelizmente" in palavra:
        break
    else:
        letra = input('Digite uma letra: ')
        clientSocket.send(letra.encode())



clientSocket.close()
