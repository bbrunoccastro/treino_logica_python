numero_secreto = 25

tentativas = 0
rodada = 1

while (rodada <= tentativas):
    print(f"Tentativa {rodada} de {tentativas}")
    chute = int(input("Digite o seu chute: "))
    print(f"Você digitou: {chute}")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print(f"Você acertou, o número secreto é: {numero_secreto}")
    else:
        if (maior):
            print("Seu palpite foi maior que o número secreto!! :(")
        elif (menor):
            print("Seu palpite foi menor que o número secreto!! :(")

    rodada = rodada + 1

print("Fim do Jogo!!")