import forca
import adivinhacao

def escolha_jogo():

    print("***********************************")
    print("******* Escolha o teu jogo! *******")
    print("***********************************")

    print("1. Forca")
    print("2. Advinhação")

    jogo = int(input())

    if (jogo == 1):
        print("***FORCA!***")
        forca.jogar()
    else:
        print("***ADIVINHAÇÃO!***")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()

