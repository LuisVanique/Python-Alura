import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
tentativas = 0
pontos = 1000

print("Qual o nivel de dificuldade?")
print("(1) Fácil (2) Médio (3) Díficil")

nivel = int(input("Defina o nivel: "))

if(nivel == 1):
    tentativas = 20
elif(nivel == 2):
    tentativas = 10
else:
    tentativas = 5

for rodadas in range(1,tentativas + 1):
    print("Tentativa {} de {}".format(rodadas,tentativas))
    chute = int(input("Digite um numero: "))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou! e sua pontuação foi {}".format(pontos))
        break
    else:
        if(maior):
            print("O numero chutado é menor!")
        elif(menor):
            print("O numero chutado é maior!")

        pontos = pontos - chute

print("Fim do jogo!")







