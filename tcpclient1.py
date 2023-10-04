from socket import *

while True:
   
   serverName = input('Digite o endereco IP de destino:')
   
   serverPort = 12000

   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((serverName,serverPort))

   #Envia mensagem para servidor
   texto = input('Digite algo:')
   clientSocket.sendto(texto.encode('utf-8'),(serverName,serverPort))
   
   #Recebe mensagem do servidor
   resposta = clientSocket.recv(1024).decode('utf-8')
   print('Resposta do servidor:', resposta)
   
   clientSocket.close()
