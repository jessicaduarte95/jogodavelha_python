# Jogo da Velha

import os
import random
from colorama import Fore, Back, Style # Importar o colorama para utilizar cores (Fore para a cor da frete e Back para o fundo).

jogarNovamente = "Sim" or "sim"
jogadas = 0
quemJoga = 2 # O número 2 será o jogar e o 1 a cpu.
maxJogadas = 9
vitoria = "Não"
Velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global Velha 
    global jogadas
    os.system("cls")

    print ("    0   1   2")
    print ("0:  " + Velha[0][0] + " | " + Velha[0][1] + " | " + Velha[0][2])
    print ("   -----------")
    print ("1:  " + Velha[1][0] + " | " + Velha[1][1] + " | " + Velha[1][2])
    print ("   -----------")
    print ("2:  " + Velha[2][0] + " | " + Velha[2][1] + " | " + Velha[2][2])
    print ("\nJogadas: " + Fore.BLUE +  str(jogadas) + Fore.RESET)


def jogoJogador():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
            while Velha[l][c] != " ":
                l = int(input("Linha: "))
                c = int(input("Coluna: "))
            Velha[l][c] = Fore.RED + "X" + Fore.RESET 
            quemJoga = 1
            jogadas += 1
        except:
            print ("Linha e/ou coluna inválida(s).")
            os.system("pause")

def cpu():
    global jogadas
    global quemJoga 
    global maxJogadas

    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while Velha[l][c] != " ":
            l = random.randrange(0,3)
            c -= random.randrange(0,3)
        Velha [l][c] = Fore.GREEN + "O" + Fore.RESET
        jogadas += 1
        quemJoga = 2

def Vitoriaverificar():
    global Velha
    Vitoria = "Não"
    simbolos = [Fore.RED + "X" + Fore.RESET, Fore.GREEN + "O" + Fore.RESET]
    for s in simbolos:
        Vitoria = "Não"

        # Verificar vitórias em linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (Velha[il][ic] == s):
                     soma += 1
                ic += 1
            if soma == 3:
                Vitoria = s 
                break
            il += 1
        if (Vitoria != "Não"):
            break

        # Verificar vitória em colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (Velha[il][ic] == s):
                    soma += 1
                il += 1 
            if soma == 3:
                Vitoria = s
                break
            ic += 1
        if (Vitoria != "Não"): 
            break

        # Verificar Diagonal 1
        soma = 0 
        idiagonal = 0
        while idiagonal < 3:
            if (Velha[idiagonal][idiagonal] == s):
                soma += 1
            idiagonal += 1
        if (soma == 3):
            Vitoria = s
            break

        # Verificar Diagonal 2
        soma = 0 
        idiagonall = 0
        idiagonalc = 2
        while idiagonalc >= 0:
            if (Velha[idiagonall][idiagonalc] == s):
                soma += 1
            idiagonall += 1
            idiagonalc -= 1
        if (soma == 3):
            Vitoria = s
            break
    return Vitoria

def redefinir ():
    global Velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vitoria
    jogadas = 0
    quemJoga = 2 # O número 2 será o jogar e o 1 a cpu.
    maxJogadas = 9
    vitoria = "Não"
    Velha = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

while(jogarNovamente == "Sim" or jogarNovamente =="sim"):
    while True:
        tela()
        jogoJogador()
        cpu()
        tela()
        
        vitoria = Vitoriaverificar()
        if (vitoria != "Não") or (jogadas >= maxJogadas):
            break 
        
    print(Fore.GREEN + "Fim de jogo" + Fore.RESET)
    if (vitoria == (Fore.RED + "X" + Fore.RESET) or vitoria == (Fore.GREEN + "O" + Fore.RESET)):
        print(Fore.YELLOW + "Resultado: Jogador " + Fore.RESET+ vitoria + Fore.YELLOW + " venceu" + Fore.YELLOW)
    else:
        print("Resultado: Empate")

    jogarNovamente = input(Fore.BLUE + "Jogar Novamente? (Sim/Não): " + Fore.RESET)
    redefinir()