import math

# Defina a cobertura da tinta em metros quadrados por litro
cobertura_por_litro = 6

# Defina o tamanho das latas e galões de tinta em litros e seus preços
litros_por_lata = 18
preco_por_lata = 80.00
litros_por_galao = 3.6
preco_por_galao = 25.00

# Solicite ao usuário o tamanho em metros quadrados da área a ser pintada
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Adicione uma folga de 10%
area_a_ser_pintada += area_a_ser_pintada * 0.1

# Calcule a quantidade de litros de tinta necessária
litros_necessarios = area_a_ser_pintada / cobertura_por_litro

# Calcule a quantidade de latas de 18 litros necessárias
latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)

# Calcule o preço total ao comprar apenas latas
preco_latas = latas_necessarias * preco_por_lata

# Calcule a quantidade de galões de 3,6 litros necessários
galoes_necessarios = math.ceil(litros_necessarios / litros_por_galao)

# Calcule o preço total ao comprar apenas galões
preco_galoes = galoes_necessarios * preco_por_galao

# Calcule a combinação de latas e galões que minimiza o desperdício
min_desperdicio = float('inf')
melhor_combinacao = None

for num_latas in range(latas_necessarias + 1):
    for num_galoes in range(galoes_necessarios + 1):
        total_litros = (num_latas * litros_por_lata) + (num_galoes * litros_por_galao)
        if total_litros >= litros_necessarios:
            desperdicio = total_litros - litros_necessarios
            if desperdicio < min_desperdicio:
                min_desperdicio = desperdicio
                melhor_combinacao = (num_latas, num_galoes)

# Calcule o preço total com a melhor combinação
latas_utilizadas, galoes_utilizados = melhor_combinacao
preco_combinacao = (latas_utilizadas * preco_por_lata) + (galoes_utilizados * preco_por_galao)

# Exiba as quantidades e preços nas três situações
print(f"Quantidade de latas de 18 litros a serem compradas: {latas_necessarias}")
print(f"Preço ao comprar apenas latas de 18 litros: R$ {preco_latas:.2f}")

print(f"Quantidade de galões de 3,6 litros a serem comprados: {galoes_necessarios}")
print(f"Preço ao comprar apenas galões de 3,6 litros: R$ {preco_galoes:.2f}")

print(f"Melhor combinação: {latas_utilizadas} latas de 18 litros e {galoes_utilizados} galões de 3,6 litros")
print(f"Preço com a melhor combinação: R$ {preco_combinacao:.2f}")