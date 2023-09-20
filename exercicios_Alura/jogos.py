import ex_jogo_forca
import ex_jogo_advinhacao_for

def escolhe_jogo():
    print("**********************************")
    print("** Escolha qual jogo quer jogar **")
    print("**********************************")

    print("(1) Forca - (2) Advinhação")
    jogo = (int(input("Qual jogo? ")))

    if jogo == 1:
        print("Jogando forca :D ")
        ex_jogo_forca.jogar()
    elif jogo == 2:
        print("Jogando Advinhação :D ")
        ex_jogo_advinhacao_for.jogar()

    if (__name__ == "__main__"):
        escolhe_jogo()