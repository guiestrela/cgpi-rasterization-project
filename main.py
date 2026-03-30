from vector import cria_imagem_vetorial
from raster import passo2, passo3

def main():
    print("Iniciando projeto de computação gráfica...")

    cria_imagem_vetorial()
    passo2()
    passo3()

    print("Imagens geradas com sucesso!")

if __name__ == "__main__":
    main()