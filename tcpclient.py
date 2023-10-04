from socket import *
import advinha_palavras

while True:
   
   serverName = input('Digite o endereco IP de destino:')
   
   serverPort = 12000

   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((serverName,serverPort))

   #Envia mensagem para servidor
   texto = ("\nbem vindo ao jogo, você possui 8 vidas\nou seja,"+ 
            "se você errar mais de 8 letras em uma única tentativa,você perde. Bom jogo!!\n")
   clientSocket.sendto(texto.encode('utf-8'),(serverName,serverPort))
   
   # advinha_palavras.sorteia_palavra()
   #Recebe mensagem do servidor
   letra = clientSocket.recv(1024).decode('utf-8')
   print('Resposta do servidor:', letra)
   
   clientSocket.close()
