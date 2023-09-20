print("Bem vindo a Loja de tintas Nova Pintura!!")
areaPintar = float(input("Primeiro digite a área a ser pintada: "))
metroPinta = float(1/3)
lataValor = float(80.00)
litroLata = float(18)

lataPinta = litroLata * 3
print("Uma lata pinta: " + str(lataPinta) + " Metros")
litrosPrecisa = areaPintar * metroPinta
print("Você precisará dessa quantida:  " + str(litrosPrecisa) + " L")
quantasLatas = int(litrosPrecisa / litroLata) + 1
print("Será necessário comprar " + str(quantasLatas) + " Latas")
print("E custará R$" + str(quantasLatas * lataValor))
