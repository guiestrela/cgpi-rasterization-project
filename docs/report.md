# Relatorio do Projeto de Rasterizacao

## 1. Objetivo
Este projeto demonstra conceitos basicos de computacao grafica por meio de duas abordagens:
- Geracao vetorial de primitivas geometricas com Cairo.
- Rasterizacao em imagem matricial com NumPy e Pillow.

A cena contem duas retas diagonais e um circulo central.

## 2. Estrutura do Projeto
- `main.py`: ponto de entrada; executa as etapas do projeto.
- `vector.py`: gera a versao vetorial da cena em SVG.
- `raster.py`: organiza o pipeline de rasterizacao e salvamento.
- `algorithms.py`: implementa os algoritmos de desenho de reta e circulo.
- `outputs/`: pasta de arquivos de saida.

## 3. Etapas Executadas
O fluxo principal e:
1. Exibir mensagem de inicio.
2. Gerar a imagem vetorial (`vector.svg`).
3. Gerar imagem com apenas circulo rasterizado (`circle.png`).
4. Gerar imagem rasterizada completa (`rasterized.png`).
5. Exibir mensagem de sucesso.

## 4. Implementacao
### 4.1 Vetorial (SVG)
No modulo vetorial sao desenhados:
- Uma reta preta de (100, 150) ate (400, 350).
- Uma reta cinza de (400, 150) ate (100, 350).
- Um circulo de centro (250, 250) e raio 120.

A saida e salva em `outputs/vector.svg`.

### 4.2 Raster (Imagem)
A imagem raster e criada como matriz 500x500 em tons de cinza (uint8), iniciada em branco (255).

#### Desenho de reta
A funcao de reta utiliza um algoritmo incremental com erro acumulado (estilo Bresenham), marcando os pixels do ponto inicial ate o final.

#### Desenho de circulo
A funcao do circulo percorre todos os pixels e aplica a condicao:

$(x - cx)^2 + (y - cy)^2 \le r^2$

Quando verdadeira, o pixel recebe a cor especificada.

## 5. Dependencias
Para execucao, o projeto utiliza:
- `pycairo`
- `numpy`
- `Pillow`

## 6. Execucao
Com o ambiente virtual ativo, execute:

```bash
python main.py
```

Na validacao realizada, a execucao concluiu com sucesso (codigo 0) e gerou os arquivos esperados.

## 7. Resultados
Arquivos gerados em `outputs/`:
- `vector.svg`
- `circle.png`
- `rasterized.png`

## 8. Conclusao
O projeto atende ao objetivo de comparar geracao vetorial e rasterizacao de uma mesma cena, evidenciando o pipeline de desenho em ambos os formatos e consolidando conceitos fundamentais de computacao grafica.