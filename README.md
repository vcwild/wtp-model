<h2 style="text-align: center">

 [«](https://github.com/vcwild/wtp-eda) | [Apresentação](#ovr) | [Procedimento](#proc) | [Dicionário de Dados](https://github.com/vcwild/wtp-eda/blob/master/dicionario_dados.md) | [Q.A.](#qa)

</h2>

## Etapas Anteriores

- [Coleta de Dados]()
- [Limpeza de Dados]()
- [Tratamento de Dados]()
- [Análise Exploratória]()

# Apresentação <a name="ovr"></a>
## Previsão de Séries Temporais

O projeto tem objetivo de gerar previsões por modelagem de séries temporais.

## Escopo do projeto

- Receber dados tratados da etapa anterior
- Identificar padrôes representados pela sequência dos dados
- Adequar os dados para executar modelos de previsão de série temporal
- Modelar séries temporais, decompondo-as em componentes (nível, tendência, sazonalidade e resíduos)
- Ajustar os dados a 3 tipos de modelos de previsão
- Prever os próximos 12 meses de cada série temporal em cada um dos modelos
- Comparar os resultados das previsões e verificar o modelo mais preciso para cada caso

## Modelos de Previsão Utilizados

- [Médias Móveis Integradas Autoregressivas (ARIMA)](./arima/arima.md)
- [Suavização Exponencial (ETS)](./ets/ets.md)
- [Prophet](https://facebook.github.io/prophet/)

# Procedimento <a name="proc"></a>

 - [Identificação e remoção de anomalias](#remove)
 - [Imputação de valores nos campos removidos](#impute)
 - [Comparação das séries corrigidas com as anteriores](#compare)
 - [Decomposição sazonal das séries temporais](#decompose)
 - [Ajuste dos dados ao modelo de análise temporal](#fit)
 - [Aplicar previsão do modelo ajustado](#predict)
 - [Comparação da eficácia entre os modelos](#compare)

 ## Identificação e remoção de anomalias <a name="remove"></a>

 Serão lidos os dados tratados da fase de EDA e verificada a persistência de observações anômalas. Caso existam, serão removidas da fase de modelagem. A remoção será executada pelo algoritmo Isolation Forest. A remoção de dados anômalos funcionará como um filtro para dados que eventualmente poderão enviesar a interpretação dos modelos de análise temporal, devido a pequena quantidade de registros (< 100).

 ## Imputação de valores nos campos removidos <a name="impute"></a>

 As observações removidas pela etapa anterior serão substituídas pela média ponderada anual para cada intervalo, utilizando o algoritmo k-Nearest Neighbors com k=11, utilizando o método de distância euclidiana.

 ## Comparação das séries corrigidas com as anteriores <a name="compare"></a>

 Será realizada comparação entre as séries com registro anômalo e as com valores imputados a fim de identificar se os valores alterados impactaram negativamente na interpretabilidade da série original ou se melhoraram o ajuste aos modelos de análise temporal.

## Decomposição sazonal das séries temporais <a name="decompose"></a>

As séries temporais serão decompostas em tendência, sazonalidade e ruído.

## Ajuste dos dados ao modelo de análise temporal <a name="fit"></a>

As séries temporais serão ajustadas para cada um dos modelos contidos nos tipos:

### ETS
Modelos:
- Suavização Exponencial Simples com \alpha=0.2;
- Suavização Exponencial Dupla Linear com \alpha=0.6 e \beta=0.2;
- Método Holt-Winters Tendência e Sazonalidade Aditivos; 
- Método Holt-Winters Tendência Aditiva Sazonalidade Multiplicativa;
- Método Holt-Winters Tendência Aditiva Sazonalidade Multiplicativa; 
- Método Holt-Winters Tendência e Sazonalidade Multiplicativos

Obs 1: os métodos Holt-Winters utilizam transformação Box-Cox prévia e nível de suavização \alpha=0.6
Obs 2: O modelo ETS mais preciso será definido pela menor raiz do erro médio quadrado (RMSE) encontrada na diferença entre o modelo e os dados de treino.

### ARIMA

- Parâmetro "d" definido de acordo com resultado do teste ADF.
- Parâmetro "D" fixo em 1.
- Parâmetros restantes ajustados caso a caso de acordo com inferếncias realizadas em cada série.

Obs: O modelo ARIMA mais preciso será definido pelo menor Critério de Informação Akaike (AIC) encontrado na comparação entre o modelo e os dados de treino.

## Aplicar previsão do modelo ajustado <a name="predict"></a>

Gerar previsão para os próximos 12 meses utilizando cada um dos modelos ajustados aos dados de treino.

## Comparação da eficácia entre os modelos <a name="compare"></a>

Trazer o melhor resultado de cada um dos tipos de modelo (ETS, ARIMA) e realizar comparação com os demais tipos (ETS, ARIMA e Prophet) para verificar qual foi a melhor previsão dos dados observados.

# Q.A. <a name="qa"></a>

## 1 - Quais os tipos dos dados de origem?

Os dados de origem são tabulares, provenientes de análise laboratorial e anotações realizadas por profissional laboratorista.
A maior parcela dos dados são variáveis contínuas, todas as observações das variáveis estão acompanhadas de rótulo com data.

## 2 - Qual a precisão dos dados?

Os dados são provenientes de ensaios laboratoriais, são revisados e já foram utilizados anteriormente para emissão de relatórios. Podem conter falha de digitação, falha de leitura, falha operacional ou escala alterada.

## 3 - Quantos dados estão disponíveis para análise? Será possível juntá-los?

Os dados estão fragmentados em diversos documentos dispostos de forma tabular e preenchidos de forma distinta ao longo do tempo, não possuem normalização ou uniformidade. Será feita a união dos dados por tentativas, inicialmente serão agrupados em conjuntos por semelhança de elementos da estrutura, depois condicionados a mesma formatação para então unificação de todo o conteúdo relacionável e armazenamento em datasets.

## 4 - Qual é o horizonte de evento das predições?

Com os dados existentes, estima-se que a previsão seja de no máximo 1 ano, incluindo o conjunto de validação. O ano de 2020 (t+2) é atípico e não será possível modelar utilizando os dados da série histórica. 

## 5 - Qual a frequência de tempo que será preciso realizar a análise? 

Será realizada por intervalo mensal.

## 6 - Essa análise é estática ou será atualizada quando receber novos dados?

Será estática, mas o modelo de previsão gerado poderá receber novos dados se caso aplicado o mesmo procedimento de ETL.

## 7 - Qual/quais a(s) métrica(s) de análise do modelo?

As métrica de análise utilizadas serão a raiz do erro médio quadrado (RMSE) entre os valores verdadeiros e preditos e Critério de Informação Akaike (AIC). Os modelos cuja RMSE é menor são os mais precisos, isto é, geraram menor resíduo pela proximidade entre predição e valores observados.
