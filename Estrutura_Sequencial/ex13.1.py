altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo: ")

calculoH = float(72.7*altura) - 58
calculoM = float(62.1*altura) - 44.7

if sexo == 'H':
    print("Seu peso ideal é: " + str(calculoH))
elif sexo == 'M':
    print("seu peso ideal é: " + str(calculoM))
else:
    print("Não consigo calcular")