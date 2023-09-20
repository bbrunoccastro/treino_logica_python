# Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.

produto1 = float(input("Digite o preço do prod 1: "))
produto2 = float(input("Digite o preço do prod 2: "))
produto3 = float(input("Digite o preço do prod 3: "))

menor = produto1
if produto1 < produto2 and produto1 < produto3:
    menor = produto1
elif produto2 < produto1 and produto2 < produto3:
    menor = produto2
else:
   menor = produto3

print(f"Você deve levar o prod no valor de R${menor}")