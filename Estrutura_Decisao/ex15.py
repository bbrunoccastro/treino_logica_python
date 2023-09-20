lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
formaTri = True

if ((lado1 + lado2) > lado3):
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo Equilatero formado, possui 3 lados iguais :)")
    elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2) or (lado2 == lado3 and lado2 != lado1):
        print("Triângulo Isóseles Formado, possui 2 lados iguais:)")
    else:
        print("Triângulo Escaleno Formado, possui 3 Lados diferentes")
else:
    print("Não forma triângulo")
