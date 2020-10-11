# Modelos Erro, Tendência e Sazonalidade (ETS)

<h2 style="text-align: left">

  [« Voltar](https://github.com/vcwild/wtp-model) | ETS

</h2>

## Introdução

Os modelos de suavização exponencial utilizam médias ponderadas de observações anteriores, fornecendo maior importância para a observação mais recente e decrescente à medida que as observações se tornam mais antigas. Erro, Tendência e Sazonalidade (ETS) são os termos aplicados no cálculo do método de suavização. De acordo com a escolha do modelo de previsão, cada um desses parâmetros pode ser iterado de forma multiplicativa, aditiva ou ser simplesmente ignorado.

# Métodos de Modelagem Exponencial
## Aditivo

Útil quando a tendência e a variação da sazonalidade são relativamente constantes em magnitude ao longo do tempo (tendência linear).

## Multiplicativo

Útil quando a tendência e variação sazonal aumentam ou diminuem em magnitude ao longo do tempo (tendência exponencial).

# Cenários possíveis para série temporal

1 - Sem tendência, sem sazonalidade<br/>
2 - Sem tendência, sazonalidade constante<br/>
3 - Sem tendência, sazonalidade aumentando<br/>
4 - Tendência linear, sem sazonalidade<br/>
5 - Tendência linear, sazonalidade constante<br/>
6 - Tendência linear, sazonalidade aumentando<br/>
7 - Tendência exponencial, sem sazonalidade<br/>
8 - Tendência exponencial, sazonalidade constante<br/>
9 - Tendência exponencial, sazonalidade aumentando

# Modelos ETS

- [Suavização Simples (SES)](#ses)<br/>
- [Método Linear de Holt](#hl)<br/>
- [Método Exponencial de Holt](#he)<br/>
- [Método de Holt-Winters](#hw)

## Suavização Simples <a name="ses"></a>

O método de previsão exponencial simples é viável em situações onde não haja tendência clara ou padrão sazonal.

O método de previsão é calculado multiplicando valores anteriores por pesos relativos, que são calculados baseados em um parâmetro de suavização $\alpha$. Essa será  a magnitude dos pesos aplicados aos valores anteriores da série, onde cada um dos pesos vai decrescendo exponencialmente conforme as observações se tornam mais antigas. A fórmula geral será:

<img src="https://render.githubusercontent.com/render/math?math=Previsao = Peso_t\ Y_t \ %2B \ Peso_{t-1} Y_{t-1} %2B \ Peso_{t-2}\ Y_{t-2}\ %2B \ ...\ %2B \ (1-\alpha)^n Y_n" />

 Onde: <br/>
 ![formula](https://render.githubusercontent.com/render/math?math=t) : número de períodos anteriores ao atual (t=0 para o mais recente)<br/>
 ![formula](https://render.githubusercontent.com/render/math?math=Y_t) : valor da série temporal no período $t$<br/>
 ![formula](https://render.githubusercontent.com/render/math?math=Peso_t=\alpha(1-\alpha)^t)<br/>
 ![formula](https://render.githubusercontent.com/render/math?math=\alpha) : padrão de suavização entre 0 e 1<br/>
 ![formula](https://render.githubusercontent.com/render/math?math=n) : número total de períodos<br/>

## Suavização Exponencial Dupla (Método Linear de Holt) <a name="hl"></a>

O método de suavização exponencial dupla é altamente viável em qualquer situação que não haja padrão sazonal no conjunto de dados.

É baseado no método SES, mas além de incluir o nível, também considera a tendência da série temporal no cálculo. Ele atinge essa possibilidade realizando dois cálculos de suavização, um para o nível de magnitude e outro para a tendência.

O cálculo de tendência é realizado de maneira linear ou aditiva, possibilitando que o resultado da predição não seja mais plano, mas que siga tendência positiva ou negativa.

## Suavização Exponencial Dupla (Método Exponencial de Holt) <a name="he"></a>

É uma variação do método linear de Holt. Porém considera que o nível e a tendência da série são aplicados de forma multiplicativa. Significando que a tendência da série irá crescer ou diminuir de forma exponencial, exibindo previsões numa taxa de crescimento de tendência fatorial

### Método de Amortecimento de Tendência

É uma solução que apresenta parâmetros de amortecimento da linha de tendência, suavizando-a até torná-la plana após certo tempo. Pode ser aplicado de forma aditiva ou multiplicativa. 

O parâmetro de amortecimento é chamado $\Phi$, modelos com valores $\Phi$ pequenos pressupõem que a tendência muda muito lentamente com o tempo, enquanto modelos com valores altos pressupõe, mudança rápida.

## Suavização Exponencial por Holt Winters <a name="hw"></a>

É a técnica que envolve três equações com parâmetros de suavização associados a cada componente da série: nível, tendência e sazonalidade

# Resumo

- **SES**: encontra o nível da série temporal<br/>
- **Método Linear Holt**: encontra nível, modelo aditivo para tendência linear<br/>
- **Método Exponencial Holt**: Encontra nível, modelo multiplicativo para tendência exponencial<br/>
- **Método Holt-Winters**: Encontra nível, aditivo para tendência, multiplicativo e aditivo para componentes sazonais

[« Voltar](https://github.com/vcwild/wtp-model)