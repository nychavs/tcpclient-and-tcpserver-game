import random
from socket import *
from colorama import Fore

palavra_escolhida = ""
qtd_caracteres = ""
palavra_array = []
lista_erros = []
novo_jogo = 1
erros = 0

def sorteia_palavra():
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
    texto.append(palavra_escolhida)

    dica_escolhida = lista_dicas[numero_palavra]
    dica = ("Dica: " + str(dica_escolhida))
    texto.append(dica)

    global qtd_caracteres
    qtd_caracteres = "_"*len(palavra_escolhida)

    global palavra_array
    palavra_array = list(qtd_caracteres)
    palavra_array_str = palavra_array
    texto.append(str(palavra_array_str))
    
def verifica_letra(letra):
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
            erros = ("\nerros: " + str(erros))
            texto.append(erros)
            erros_lista = (str(lista_erros))
            texto.append(erros_lista)
            print("mandando erros...")

    if erros == 8:
        print(Fore.RED + "\ninfelizmente não foi dessa vez!")
        global novo_jogo
        novo_jogo = 0
    else:
        palavra_array_str = palavra_array
        texto.append(palavra_array_str)
        print("mandando array...")
    
    return texto


serverName = input('Digite o endereco IP de destino:')
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

texto = ["Bem vindo ao jogo! você possui 8 vidas... ou seja: "+ 
            "você perde se errar mais de 8 letras em uma única tentativa. Bom jogo!!"]

sorteia_palavra()

texto = str(texto).replace("[", "\n")
texto = str(texto).replace("]", "\n")
texto = str(texto).replace(",", "")
texto = str(texto).replace("'", "")
texto = str(texto).replace('"', "")
clientSocket.sendto(texto.encode('utf-8'),(serverName,serverPort))

resposta = clientSocket.recv(1024).decode('utf-8')
print('Letra:', resposta)

while novo_jogo == 1:
    texto = str(verifica_letra(resposta))
    
    clientSocket.sendto(texto.encode('utf-8'),(serverName,serverPort))
    resposta = clientSocket.recv(1024).decode('utf-8')
    
    print('Letra:', resposta)

    if palavra_array == list(palavra_escolhida):
        print(Fore.GREEN + "\nparabens você concluiu o jogo!")
        print(Fore.WHITE)
        novo_jogo = 0

