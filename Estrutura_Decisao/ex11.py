#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
# lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salarioAntes = float(input("Digite o Salário: "))
faixa = " "
aumento = 0

if salarioAntes <= 280.00:
    aumento = salarioAntes * 0.20
    salarioFinal = salarioAntes + (aumento)
    faixa = "Aumento de 20%"
elif salarioAntes > 280.00 and salarioAntes <= 700.00:
    aumento = salarioAntes * 0.15
    salarioFinal = salarioAntes + (aumento)
    faixa = "Aumento de 15%"
elif salarioAntes > 700.00 and salarioAntes <= 1500.00:
    aumento = salarioAntes * 0.10
    salarioFinal = salarioAntes + (aumento)
    faixa = "Aumento de 10%"
else:
    aumento = salarioAntes * 0.05
    salarioFinal = salarioAntes + (aumento)
    faixa = "Aumento de 5%"

print(f"O salário antes do reajuste era: R${salarioAntes}")
print("O Salário recebe um aumento de: " + faixa)
print(f"O aumento foi de R${aumento}")
print(f"O Salário final passa a ser: R${salarioFinal}")