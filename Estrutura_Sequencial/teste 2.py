import math
area = float(input("area: "))

litros_necesario = area / 3

latas_necessario = math.ceil(litros_necesario / 18)

preco_total = latas_necessario * 80

print(latas_necessario)
print(preco_total)