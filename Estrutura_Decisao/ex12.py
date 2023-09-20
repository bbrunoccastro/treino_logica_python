import math

salarioBruto = 0
valorhora = float(input("Digite o valor da sua hora: "))
horaTrab = float(input("Digite a qtde de horas trabalhadas: "))

salarioBruto = float(valorhora * horaTrab)

inss = salarioBruto * 0.10
fgts = salarioBruto * 0.11
sindicato = salarioBruto * 0.03
ir = float(0)
isento = " "
faixaIr = " "

if salarioBruto <= 900:
    faixaIr = "0"
    isento = str("ISENTO")
elif salarioBruto > 900 and salarioBruto <= 1500:
    faixaIr = "5%"
    ir = salarioBruto * 0.05
elif salarioBruto > 1500 and salarioBruto <= 2500:
    faixaIr = "10%"
    ir = salarioBruto * 0.10
else:
    faixaIr = "20%"
    ir = salarioBruto * 0.20

descontos = [inss, ir, sindicato]
totalDescontos = math.fsum(descontos)
salarioLiquido = salarioBruto - totalDescontos

print(f"O salário Bruto é  : R${salarioBruto}")
print(f"(-) IR   ({faixaIr})      : R${ir}")
print(f"(-) INSS (10%)     : R${inss}")
print(f"(-) SINDICATO (3%) : R${sindicato}")
print(f"(-) FGTS (11%)     : R${fgts}")
print(f"Total de descontos : R${totalDescontos}")
print(f"Salário Líquido:   : R${salarioLiquido}")