import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    numero_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        numero_de_tentativas = 20
    elif(nivel == 2):
        numero_de_tentativas = 10
    else:
        numero_de_tentativas = 5

    for rodada in range(1,numero_de_tentativas + 1 ):

        print("Tentativa {} de {}".format(rodada, numero_de_tentativas))
        chute_str = input("Escolha um numero: ")
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Errou! O numero é menor do que seu chute")
            elif(menor):
                print("Errou! O numero é maior do que seu chute")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()