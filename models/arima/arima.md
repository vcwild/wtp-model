## ARIMA
ARIMA são modelos de previsão de séries temporais que utilizam autocorrelação, diferenciação e médias móveis para estimar e prever o comportamento dos dados. Um modelo SARIMA também leva em consideração a sazonalidade.

Os modelos ARIMA utilizam os parâmetros "p", "d", "q", "P", "D" e "Q". Cada uma das letras está relacionada a uma parcela do modelo ARIMA.

**AR (Auto-regressivo)**: modelo utilizado para representação de um tipo de processo aleatório que varia de acordo com o tempo. Está relacionado aos parâmetros "p" e "P" do modelo ARIMA.

**I (Integrado)**: está relacionado com a diferenciação da série temporal. Esse conceito é utilizado para remover tendência na série e torná-la estacionária. São os parâmetros "d" e "D" no modelo ARIMA. Lembrando que para que uma série temporal seja considerada estacionária é necessário seus valores não estejam elencados ao tempo, isto é, que tenha uma função cujo valor médio é constante em toda sua extensão.

**MA (Média-Móvel/Moving Average)**: é um estimador calculado a partir da sequência de amostras de uma série temporal, geralmente utilizado para suavizar flutuações curtas e destacar tendências a longo prazo. Corresponde aos parâmetros "q" e "Q" do modelo ARIMA.

### Definindo os Parâmetros
O parâmetro "d" é definido de acordo com a necessidade de diferenciação da série temporal, séries identificadas como estacionárias possuem d = 0.

Para estimar o parâmetro "p" no modelo ARIMA é necessário interpretar a função de autocorrelação (ACF). O valor de "p" será equivalente ao máximo número de registros acima da margem entre registros abaixo da margem. Isto é, sempre que o valor do registro for abaixo da margem, a contagem de "p" é reiniciada.

Para estimar o parâmetro "q" é necessário interpretar a função de autocorrelação parcial (PACF) e identificar o valor crítico. O valor de "q" é definido de forma análoga ao de "p" (maior número de registros acima da margem entre intervalos), sendo a única diferença o gráfico interpretado.
