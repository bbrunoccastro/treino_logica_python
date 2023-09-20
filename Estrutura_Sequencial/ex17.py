import math

print("Bem vindo a Loja de tintas Marazul!!")

# Solicita Qual a área a ser pintada
areaPintar = float(input("Primeiro digite a área a ser pintada: "))

# Atribui os litros em variaveis
litroMaiorLata = float(18)
litroMenorLata = float(3.6)

# Atribui preço a variaveis
lataMaiorValor = float(80.00)
lataMenorValor = float(25.00)

# Quantos metros cada lata pinta
lataMaiorPinta = float(litroMaiorLata * 6)
lataMenorPinta = float(litroMenorLata * 6)

# Quantos litros pinta 1 metro
litroPintaUmMetro = (1 / 6)

# Litros necessários
litroNecessario = areaPintar * litroPintaUmMetro
litroNecessario = litroNecessario + (litroNecessario * 0.10)

# Quantidade necessária
quantasLatas = round(litroNecessario / litroMaiorLata + 0.5)
quantosgaloes = round(litroNecessario / litroMenorLata + 0.5)

# Custo segregado por lata e galão
custoLatas = float(quantasLatas * lataMaiorValor)
custoGaloes = float(quantosgaloes * lataMenorValor)

# Quantidade e valor da combinação
latasOtimizadas = int(litroNecessario // litroMaiorLata + 0.5)
galoesOtimizados = math.ceil((litroNecessario - latasOtimizadas * litroMaiorLata) / litroMenorLata)
latasGaloes = (lataMaiorValor * latasOtimizadas) + (lataMenorValor * galoesOtimizados)

print("-------------------------------------------------------------------")
print("Uma lata de 18 Litros pinta " + str(lataMaiorPinta) + " Metros")
print("Uma lata de 3.6 Litros pinta " + str(lataMenorPinta) + " Metros")
print("-------------------------------------------------------------------")
print(f"Então para pintar a área de  {areaPintar} metros será necessário: {litroNecessario}L " )
print("-------------------------------------------------------------------")
print(f"Somente em Latas 18L: {quantasLatas} unidades, e custará: R${custoLatas}")
print(f"Somente em galões 3,6L: {quantosgaloes} unidades, e custará: R${custoGaloes} ")
print("-------------------------------------------------------------------")
print("Para melhor aproveitar os tamanhos das latas... ")
print(f"Precisará de {latasOtimizadas} Latas e {galoesOtimizados} Galões" )
print(f"E custará no total: R${latasGaloes}")
print("-------------------------------------------------------------------")