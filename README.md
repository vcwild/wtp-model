<h2 style="text-align: center">

  [Apresentação](#ovr) | [Q.A.](#qa)

</h2>

## Etapas Anteriores
- [Coleta de Dados]()
- [Limpeza de Dados]()
- [Tratamento de Dados]()
- [Análise Exploratória]()

# Apresentação <a name="ovr"></a>
## Previsão de Séries Temporais
O projeto tem objetivo de gerar modelos de previsão por séries temporais.

## Escopo do projeto
- Gerar modelos de previsão baseados em séries temporais
- A fonte de dados disponível trata apenas de variáveis numéricas
- Os dados estão dispostos ao longo do tempo
- As variáveis-alvo que queremos prever serão sempre numéricas

## Tipos de modelo disponíveis para o problema
Suavização Exponencial/Exponential Smoothing (ETS)
Médias Móveis Integradas Autoregressivas/Autoregressive Integrated Moving Average (ARIMA)

## Objetivos Principais desse Projeto
- Identificar padrôes representados pela sequência dos dados
- Modelar séries temporais, transformando-as em estacionárias
- Prever os valores de cada série temporal
- Prever impacto ambiental no sistema de tratamento de água

## O que esse projeto NÃO abordará
- Diagnóstico ambiental ou operacional
- Análise de riscos ou previsão de falhas
- Relatório de falhas operacionais ou de leitura
- Avaliação de desempenho do sistema de tratamento

# Q.A. <a name="qa"></a>

## O que é?
Previsão de série temporal, em linhas gerais, é o uso de um modelo estatístico baseado em dados históricos para prever valores futuros.

## Que tipos de variáveis poderemos utilizar?
Qualquer variável que seja registrada ao longo do tempo (e.g. crescimento populacional, preço de um produto, temperatura). Nesse projeto as variáveis utilizadas são observações de amostra laboratorial.

## Como definir o intervalo de tempo?
Os registros da série temporal precisam estar ordenados de forma cronológica e com igual espaço de tempo entre valores.
No caso do projeto, a periodicidade de coleta dos dados varia de acordo com a variável, sendo realizados por mês, por trimestre e por semestre. Será selecionado o período que capture da forma mais fidedigna os dados originais, com a menor perda de informação.

## O que são tendências?


## O que são padrões sazonais?



