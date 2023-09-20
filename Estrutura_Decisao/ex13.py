# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Digite o numero correspondente ao dia desejado: "))

while numero != 1 or numero != 2:
    if numero == 1:
        print("Número correto!!")
        print("Domingo")
        break
    elif numero == 2:
        print("Número correto!!")
        print("Segunda")
        break
    else:
        print("Número incorreto, tente novamente!!")
        numero = int(input("Digite o numero correspondente ao dia desejado: "))