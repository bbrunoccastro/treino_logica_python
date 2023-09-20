pesoTrazido = float(input("Digite o peso que você pescou: "))
pesoExedido = float(0.00)
precoKgAdd = float(4.00)
precoAdicional = float(0.00)

if pesoTrazido > 50.0:
    pesoExedido = pesoTrazido - 50
    precoAdicional = pesoExedido * precoKgAdd
    print("Você trouxe " + str(pesoTrazido) + "KG de peixes pescados")
    print("Porém excedeu o peso em " +  str(pesoExedido) + "KG")
    print("E por isso deve pagar uma multa de R$" + str(precoAdicional))
else:
    print("Você está dentro do limite estabelecido de 50Kgs de peixes pescados, siga viagem!!")