import math

# Defina a cobertura da tinta em metros quadrados por litro
cobertura_por_litro = 3

# Defina o tamanho da lata de tinta em litros e seu preço
litros_por_lata = 18
preco_por_lata = 80.00

# Solicite ao usuário o tamanho em metros quadrados da área a ser pintada
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calcule a quantidade de litros de tinta necessária
litros_necessarios = area_a_ser_pintada / cobertura_por_litro

# Calcule o número de latas de tinta necessárias (arredondado para cima)
latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)

# Calcule o preço total
preco_total = latas_necessarias * preco_por_lata

# Exiba a quantidade de latas de tinta necessárias e o preço total
print(f"Você precisará de {latas_necessarias} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}")