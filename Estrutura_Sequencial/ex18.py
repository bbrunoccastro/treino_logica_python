# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

megabytes = float(input("Digite o tamanho dos arquivos em megabytes: "))
velocidade = float(input("Digite a velocidade da internet em megabytes por segundo: "))

tempoDownload1 = megabytes / (velocidade / 8)
tempoDownload2 = round(tempoDownload1 / 60)

print(f"O tempo de download será de aproximadamente {tempoDownload2} minutos")
