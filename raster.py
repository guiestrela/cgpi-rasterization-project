import numpy as np
from PIL import Image
from algorithms import desenha_circulo, desenha_reta

def criar_imagem():
    img = np.ones((500, 500), dtype=np.uint8) * 255
    return img

def salvar(img, nome):
    Image.fromarray(img).save(f"outputs/{nome}")

def passo2():
    img = criar_imagem()
    img = desenha_circulo(img, (250, 250), 120, 200)
    salvar(img, "circle.png")

def passo3():
    img = criar_imagem()

    img = desenha_reta(img, (100, 150), (400, 350), 0)
    img = desenha_reta(img, (400, 150), (100, 350), 80)
    img = desenha_circulo(img, (250, 250), 120, 200)

    salvar(img, "rasterized.png")