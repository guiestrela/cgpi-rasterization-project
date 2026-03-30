# Relatorio do Projeto de Rasterizacao

## 1. Introducao
Este trabalho apresenta uma implementacao didatica de rasterizacao em Python, comparando duas formas de representar a mesma cena geometrica:
- representacao vetorial (SVG), baseada em primitivas geometricas;
- representacao matricial (bitmap), baseada em pixels.

A cena utilizada contem duas retas diagonais e um circulo central. O objetivo principal e consolidar os conceitos de desenho de primitivas, discretizacao de coordenadas e geracao de imagens digitais.

## 2. Objetivos
Os objetivos especificos do projeto sao:
1. Gerar uma versao vetorial da cena com Cairo.
2. Implementar rasterizacao manual de reta e circulo.
3. Produzir imagens finais em tons de cinza usando matriz NumPy e exportacao com Pillow.
4. Comparar, de forma pratica, a diferenca entre os fluxos vetorial e matricial.

## 3. Arquitetura e Organizacao
Estrutura principal do codigo:
- `src/main.py`: ponto de entrada e orquestracao das etapas.
- `src/vector.py`: gera a cena vetorial em SVG.
- `src/raster.py`: cria imagens, chama algoritmos e salva resultados.
- `src/algorithms.py`: implementa os algoritmos de reta e circulo.
- `outputs/`: diretorio de saida dos artefatos gerados.

Essa separacao melhora a legibilidade e facilita a manutencao por responsabilidade de modulo.

## 4. Metodologia
### 4.1 Cena Geometrica
Foram utilizados os seguintes elementos:
- reta 1: de (100, 150) ate (400, 350), cor preta;
- reta 2: de (400, 150) ate (100, 350), cor cinza escuro;
- circulo: centro em (250, 250), raio 120, cor cinza claro.

### 4.2 Pipeline Vetorial
No fluxo vetorial, as primitivas sao desenhadas diretamente em uma superficie SVG (500 x 500), preservando descricao geometrica e independendo da resolucao de exibicao.

Saida: `outputs/vector.svg`.

### 4.3 Pipeline Raster
No fluxo raster, a imagem e representada por uma matriz `500 x 500` do tipo `uint8`, inicializada com valor 255 (branco). Cada primitiva altera valores de pixels na matriz.

Saidas:
- `outputs/circle.png`: imagem com circulo rasterizado;
- `outputs/rasterized.png`: imagem final com duas retas e um circulo.

## 5. Algoritmos Implementados
### 5.1 Reta (Incremental com erro acumulado)
O desenho de reta utiliza uma abordagem incremental baseada no controle de erro (estilo Bresenham). Em cada iteracao, o algoritmo decide se avanca no eixo x, no eixo y ou em ambos, ate atingir o ponto final.

Vantagens:
- baixo custo computacional por pixel;
- boa aproximacao discreta da reta continua;
- nao requer operacoes de ponto flutuante para cada passo.

### 5.2 Circulo (Teste de pertinencia por distancia)
Para cada pixel da imagem, e verificado se o ponto pertence ao disco de raio `r` e centro `(cx, cy)`:

$$
(x - cx)^2 + (y - cy)^2 \le r^2
$$

Se a condicao for verdadeira, o pixel recebe a cor do circulo.

Vantagens:
- implementacao simples e robusta.

Limitacao:
- varredura completa da imagem, com custo proporcional ao numero total de pixels.

## 6. Complexidade (Resumo)
Considerando imagem `W x H`:
- reta: custo aproximado de `O(max(|dx|, |dy|))`;
- circulo (implementacao atual): `O(W * H)`;
- memoria da imagem: `O(W * H)`.

## 7. Ambiente e Dependencias
Bibliotecas utilizadas:
- `numpy`
- `Pillow`
- `pycairo`

## 8. Execucao
No estado atual do projeto, a forma recomendada de execucao e via modulo:

```bash
python -m src.main
```

Observacao: ao executar diretamente `python src/main.py`, podem ocorrer erros de import dependendo do `PYTHONPATH` do ambiente.

## 9. Validacao e Resultados
Durante a validacao do projeto:
1. O fluxo principal executou com sucesso.
2. Foram gerados os artefatos esperados em `outputs/`.
3. Um smoke test funcional das rotinas principais foi executado sem falhas.

Arquivos finais gerados:
- `outputs/vector.svg`
- `outputs/circle.png`
- `outputs/rasterized.png`

## 10. Discussao
O experimento evidencia a diferenca conceitual entre os modelos:
- no vetor, a cena e definida por entidades geometricas;
- no raster, a cena e definida por amostras discretas de intensidade.

Como atividade de computacao grafica introdutoria, o projeto atende ao objetivo pedagogico e demonstra claramente o processo de rasterizacao manual.

## 11. Melhorias Futuras
Como evolucao do projeto, recomenda-se:
1. Adicionar anti-aliasing nas retas e no contorno do circulo.
2. Implementar algoritmo de circunferencia incremental (ponto medio/Bresenham de circulo) para reduzir custo.
3. Criar testes automatizados para validar pixels-chave da cena.
4. Incluir comparacao visual e metrica entre versao vetorial e raster.

## 12. Conclusao
O projeto cumpre seu proposito de apresentar fundamentos de rasterizacao e consolidar conceitos de conversao geometrica para imagem digital. A arquitetura modular e adequada para extensoes futuras e para aprofundamento em algoritmos de desenho mais eficientes.