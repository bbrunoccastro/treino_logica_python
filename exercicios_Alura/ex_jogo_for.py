import random

numero_secreto = random.randrange(1,20)

tentativas = 5
rodada = 1
pontos = 1000

print("Escolha um nível para jogar :)")
print("(1) Fácil - (2) Médio - (3) Difícil")
nivel = int(input("Digite o nível: "))

if (nivel == 1):
    tentativas = 15
elif (nivel == 2):
    tentativas = 8
else:
    tentativas = 4

for rodada in range(1,tentativas + 1):
    print(f"Tentativa {rodada} de {tentativas}")
    chute = int(input("Digite o seu chute: "))
    print(f"Você digitou: {chute}")

    if (chute < 1 or chute > 20):
        print("Digite um número entre 1 e 20!!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print(f"Você acertou, o número secreto é: {numero_secreto} e você fez {pontos} pontos")
        break
    else:
        if (maior):
            print("Seu palpite foi maior que o número secreto!! :(")
            if (rodada == tentativas):
                print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
        elif (menor):
            print("Seu palpite foi menor que o número secreto!! :(")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (rodada == tentativas):
                print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

print(f"Fim do Jogo!! O número era {numero_secreto}")