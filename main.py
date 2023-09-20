import random
def misturar(palavra):
    letras = list(palavra)
    random.shuffle(letras)
    mistura = ''.join(letras)
    return mistura.lower()

palavra = ("Atenção")
print(misturar(palavra))
