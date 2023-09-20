import statistics as st

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
notas = [nota1, nota2]
media = st.mean(notas)
conceito = " "
decisao = " "

if media >= 0.0 and media < 4.00:
    conceito = "E"
    decisao = "REPROVADO"
elif media >= 4.0 and media < 6:
    conceito = "D"
    decisao = "REPROVADO"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
    decisao = "APROVADO"
elif media >= 7.5 and media < 9.0:
    conceito = "B"
    decisao = "APROVADO"
elif media >= 9.0 and media <= 10.0:
    conceito = "A"
    decisao = "APROVADO"
else:
    print("Media não aceita! Revise as notas imputadas!")

print(f"As notas foram {notas} com média {media} \n" 
      f"Portando o aluno foi: {decisao}, Com conceito: {conceito}")