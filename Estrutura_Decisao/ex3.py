# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite uma letra: ")

if letra.lower() == 'f':
    print("A letra digitada é '" + letra.upper() + "' e é Valida!!!")
elif letra.lower() == 'm':
    print("A letra digita é '" + letra.upper() + "' e é Valida!!!")
else:
    print("Letra inválida, digite F ou M!!!")