# Introdução

Série temporal univariada, ou simplesmente série temporal é o conjunto de observações de uma variável realizadas em sequência ao longo do tempo. A dimensão do tempo é uma dependência explícita inerente a cada uma das observações dentro da série. 

Essa característica é tanto uma restrição quanto uma fonte relevante de informações se comparado a métodos clássicos de análise de dados que não consideram a dimensão do tempo. As observações só farão sentido em ordem cronológica e tendem a perder o contexto se avaliadas fora de ordem, individualmente ou por amostragem aleatória.

Os registros da série temporal precisam estar ordenados de forma cronológica e com igual espaço de tempo entre valores.
No caso do projeto, a periodicidade de coleta dos dados difere dependendo da variável. Há registros realizados por mês, por trimestre e por semestre. Deverá ser selecionado o período que capture da forma mais fidedigna os dados originais, com a menor perda de informação.

# Nomenclatura

Em uma série temporal, o eixo horizontal representa o tempo e o eixo vertical a variável em estudo. A observação no presente da série temporal é dita obs(t) ou obs(t+0), as observações futuras obs(t+n), análises no passado são comumente chamadas de "lag" e descritas como obs(t-n), sendo n o número de intervalos a percorrer em relação ao presente. A primeira observação anterior ao presente será denominada "t-1" ou "lag1".

## Componentes de uma série temporal

### Nível

É o valor médio ou faixa base de uma série.

### Tendências

São mudanças ou movimentos graduais para valores relativamente maiores (tendência positiva) ou menores (tendência negativa) ao longo do tempo. Uma série com tendência horizontal/plana é chamada de série estacionária ou sem tendência.

### Padrões sazonais ou sazonalidade

Ocorrem em séries temporais que exibem padrão repetitivo em intervalos fixos e previsíveis. Estão geralmente relacionados a datas (e.g. feriados, estações do ano, datas comemorativas, anos, meses, semanas, dias do mês, horas do dia). Dizemos que uma série temporal é sazonal quando o registro das observações que ocorrem ao longo desta se repetem entre períodos iguais de tempo.

A sazonalidade determinística pressupõe um padrão sazonal regular e estável no tempo, de forma que seja possível prever o comportamento da série a partir dos dados existentes. Já a sazonalidade estocástica ocorre quando o componente sazonal da série varia ao longo do tempo. 

Para obter o componente sazonal é necessário remover a tendência da série temporal, se existente, geralmente utilizando processos estocásticos que transformarão a série em estacionária. 

### Padrões cíclicos

São padrões de comportamento em séries temporais que não ocorrem em intervalos fixos, são geralmente mais longos que a duração de padrões sazonais e são mais difíceis de identificar (e.g. comportamento do mercado de ações, comportamento do tráfego de veículos, consumo de energia). Quanto maior for a extensão do período cíclico, maior tende a ser a magnitude de mudança no ciclo. 

### Ruído

Ruído é o nome dado a variabilidade contida nas observações da série temporal que não conseguem ser observadas pelo modelo de previsão.

Todas séries temporais possuem nível, a maior parte delas contém ruído/aleatoriedade, algumas possuem tendência e sazonalidade.

## Comportamento dos Componentes

### Sistemático

São os componentes da série que possuem consistência ou recorrência, podem ser descritos e modelados (i.e. nível, tendência e sazonalidade).

### Não-sistemático

São os componentes que não podem ser modelados diretamente (i.e. ruído).

# Análise de Série Temporal

Na estatística, a análise de séries temporais envolve a elaboração de modelos que melhor capturam ou descrevem uma série temporal observada. Essa área de estudo procura capturar o comportamento das séries temporais, o que envolve a realização de testes de hipótese e inferência estatística sobre os dados e decomposição da série em componentes. 

A qualidade de um modelo descritivo é definida por quão preciso é o modelo em relação ao conjunto de dados e a qualidade da interpretação realizada sobre a série temporal.

## Gráfico de Decomposição de Série Temporal

Plot 1 - Série temporal

Plot 2 - Sazonalidade

Plot 3 - Tendência (média móvel centrada da série temporal)

Plot 4 - Erro/Resíduo (diferença entre o valor observado e a linha de tendência)

# Previsão de Série Temporal

Trata-se do uso de dados históricos para prever o comportamento das observações da série temporal. Pode também ser chamada de extrapolação do modelo de análise. 
Na previsão de série temporal deveremos separar o conjunto de dados em treino/teste ou treino/teste/validação. O conjunto de dados de treino é ajustado o modelo de análise e o conjunto de testes é utilizado para verificar a acurácia da previsão realizada. 

O conjunto validador é utilizado para avaliação pós modelagem e deve ser consultado uma só vez, não permitindo ser utilizado de forma recursiva para ajuste dos dados de treino aos dados do validador, assim garantindo que os dados de comportamento da série do validador não sejam vazados ao ajuste do modelo de treino. Na falta de um conjunto validador, os dados de teste são considerados validadores.