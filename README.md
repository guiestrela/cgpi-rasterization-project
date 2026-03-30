# Rasterizacao de Imagens em Python

## Sobre o projeto
Este projeto demonstra conceitos fundamentais de computacao grafica por meio de duas abordagens para a mesma cena:
- geracao vetorial em SVG;
- rasterizacao manual em imagem matricial.

A cena contem duas retas diagonais e um circulo central.

## Conceitos aplicados
- Rasterizacao
- Algoritmo incremental para reta (estilo Bresenham)
- Teste de pertinencia para preenchimento de circulo
- Diferenca entre representacao vetorial e bitmap

## Estrutura
- `src/main.py`: orquestra a execucao.
- `src/vector.py`: gera a versao vetorial.
- `src/raster.py`: cria imagens raster e salva saidas.
- `src/algorithms.py`: algoritmos de desenho.
- `outputs/`: arquivos gerados.

## Resultados

### Vetorial
Arquivo gerado: `outputs/vector.svg`

### Circulo (Matricial)
![circulo](outputs/circle.png)

### Rasterizacao completa
![raster](outputs/rasterized.png)

## Tecnologias
- Python
- NumPy
- Pillow
- Pycairo

## Como executar

1. (Opcional) criar e ativar ambiente virtual.
2. Instalar dependencias.
3. Executar o projeto como modulo.

```bash
pip install -r requirements.txt
python -m src.main
```

Observacao: executar `python src/main.py` pode falhar com erro de import dependendo do `PYTHONPATH`.

## Saidas esperadas
Ao final da execucao, os seguintes arquivos sao gerados em `outputs/`:
- `vector.svg`
- `circle.png`
- `rasterized.png`
