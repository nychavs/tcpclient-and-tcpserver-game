from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Servidor pronto para receber chamadas')

while 1:
   connectionSocket, addr = serverSocket.accept()
  
   fraseRecebida = connectionSocket.recv(1024)

   print('Mensagem de ', addr[0],' ----> ',fraseRecebida.decode('utf-8'))
   
   # 127.0.0.1
   #Envia uma mensagem de resposta
   resposta = input("Letra: ")
   connectionSocket.send(resposta.encode('utf-8'))

   # connectionSocket.close()
