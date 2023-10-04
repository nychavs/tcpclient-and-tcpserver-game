import random
from socket import *
from colorama import Fore

palavra_escolhida = ""
qtd_caracteres = ""
palavra_array = []
lista_erros = []
novo_jogo = 1
erros = 0

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Servidor pronto para receber chamadas')

# Configuração do servidor
# host = '127.0.0.1'  # Endereço do servidor


print("Aguardando conexão do cliente...")
connectionSocket, addr = serverSocket.accept()
print("Cliente conectado:", addr)
print('Conexao estabelecida com ----> ', addr[0])

def sorteia_palavra():
    texto = []
    lista_palavras = []
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.read()
    
    with open("dicas.txt", "r") as arquivo2:
        dicas = arquivo2.read()

    lista_palavras = palavras.split(";")
    lista_dicas = dicas.split(";")
    numero_palavra = random.randint(1,19)

    global palavra_escolhida
    palavra_escolhida = lista_palavras[numero_palavra].lower()

    dica_escolhida = lista_dicas[numero_palavra]
    dica = ("Dica: " + str(dica_escolhida))
    texto.append(dica)

    global qtd_caracteres
    qtd_caracteres = "_"*len(palavra_escolhida)

    global palavra_array
    palavra_array = list(qtd_caracteres)
    
    return texto

def verifica_letra(letra):
    print("verificando letra...")
    acertos = 0
    global erros
    texto = []
    for indice, caractere in enumerate(palavra_escolhida):
        if caractere == letra:
            acertos += 1
            palavra_array[indice] = letra

        if acertos == 0 and indice+1 == len(palavra_escolhida):
            erros += 1
            if letra not in lista_erros:
                lista_erros.append(letra)

        if erros > 0:
            texto = []
            erros_text = ("Erros: " + str(erros))
            texto.append(erros_text)
            erros_lista = (str(lista_erros))
            texto.append(erros_lista)
            print("mandando erros...")
    
    return texto

# Inicialize o jogo
novo_jogo = 1
dica = sorteia_palavra()
connectionSocket.send(str(dica).encode())

while novo_jogo == 1:
    # Enviar a palavra parcialmente adivinhada para o cliente
    palavra_enviar = " ".join(palavra_array)
    connectionSocket.send(palavra_enviar.encode())

    # Receber a letra do cliente
    resposta = connectionSocket.recv(1024).decode()
    print('Letra:', resposta)

 
    texto = verifica_letra(resposta)
    resposta_servidor = str(texto)
    connectionSocket.send(resposta_servidor.encode())

    if palavra_array == list(palavra_escolhida):
        parabens = (Fore.GREEN + "\nParabens, você concluiu o jogo!")
        connectionSocket.send(parabens.encode())
        connectionSocket.close()
        serverSocket.close()
        novo_jogo = 0
    if erros == 8:
        perdeu = ("infelizmente não foi dessa vez!")
        connectionSocket.send(perdeu.encode())
        connectionSocket.close()
        serverSocket.close()
        novo_jogo = 0


