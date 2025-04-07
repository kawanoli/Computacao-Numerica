# Construção de uma rede neural para identificação de sistemas não lineares

Este projeto tem como objetivo a **identificação de sistemas não lineares**. Para isso, foi utilizada uma abordagem de **rede neural** com base em **funções de base radial (RBF)**.

**Etapas do Projeto:**

1.  **Importação de Bibliotecas e Carregamento de Dados:**
    *   Foram importadas as bibliotecas `numpy`, `matplotlib.pyplot`, `numpy.linalg`, e `scipy.signal`.
    *   Os dados foram carregados a partir de dois arquivos: `dados_01.dat` e `dados_02.dat`.
    *   Para cada conjunto de dados (data1 e data2), foram criadas matrizes para o tempo (`t1`, `t2`), a entrada (`u1`, `u2`), e a saída (`y1`, `y2`).

2.  **Visualização dos Dados Brutos:**
    *   Os dados de saída `y1` em função de `t1` e `y2` em função de `t2` foram plotados para visualizar seu comportamento inicial.

3.  **Definição da Lei de Formação e Criação das Matrizes de Entrada:**
    *   Foi identificada uma **lei de formação** para criar as entradas da rede neural, dada pela seguinte expressão:
        ```
        x.append(y[i-1] + y[i-2] + u[i-1] + u[i-2] + np.sin(y[i-1]) + np.sign(u[i-1]) * u[i-1]**2)
        ```

    *   Com base nessa lei, foram criadas as listas `x1` (usando `y1` e `u1`) e `x2` (usando `y2` e `u2`), que representam as características de entrada para a rede neural. Os primeiros valores dessas listas são mostrados nos prints.

4.  **Definição dos Parâmetros da Rede Neural:**
    *   **Cálculo de $\sigma$ (Sigma):** Uma função `calculate_sigma` foi definida para calcular uma estimativa para o parâmetro $\sigma$ das funções gaussianas. Essa função calcula as distâncias euclidianas entre todos os pares de pontos nos dados de entrada (`x1`) e retorna a distância média. O valor de $\sigma$ encontrado para `x1` foi de **14.788056007732532**. Posteriormente, o valor de $\sigma$ utilizado no algoritmo foi definido como **14.782186497790441**.
    *   **Número de Neurônios e Centros das Gaussianas:** Foi definido o número de neurônios da rede neural (`n = 4`). Os centros das funções gaussianas (`c`) foram determinados como **4 pontos linearmente espaçados entre o valor mínimo e máximo de `x1`**, resultando em `[-16.65660921  -5.46782244   5.72096432  16.90975109]`.

5.  **Treinamento da Rede Neural:**
    *   Uma matriz `Phi1` foi criada com dimensões correspondentes ao número de amostras em `x1` e ao número de centros gaussianos.
    *   Os elementos de `Phi1` foram calculados usando a função gaussiana: $\phi_j(x_i) = \exp(-\frac{||x_i - c_j||^2}{2\sigma^2})$, onde $x_i$ são os valores em `x1` e $c_j$ são os centros gaussianos. A implementação específica nos excertos usa $\exp(-(2\sigma^2)^{-1} * abs(x1[i] - c[j])**2)$.
    *   Os pesos da camada de saída da rede neural (`w`) foram estimados utilizando a **pseudo-inversa** da matriz `Phi1` multiplicada pelo vetor de saída desejado `y1` (`w = la.pinv(Phi1) @ y1`).
    *   A saída estimada do modelo para os dados de treinamento (`y_est1`) foi calculada como o produto da matriz `Phi1` pelos pesos `w` (`y_est1 = Phi1 @ w`).

6.  **Avaliação do Modelo de Treinamento:**
    *   Foi gerado um gráfico comparando a saída real dos dados de treinamento (`y1`) com a saída estimada pelo modelo (`y_est1`) em função do tempo (`t1`).
    *   O **erro quadrático médio (EQM1)** do modelo na etapa de treinamento foi calculado, resultando em **0.4097163788134824**.

7.  **Teste do Modelo com o Segundo Dataset:**
    *   Para **validar o modelo**, foram utilizados os dados do arquivo `dados_02.dat`. Foi assumido que a quantidade de dados de treino é consideravelmente maior que a quantidade de dados usados para teste.
    *   Uma matriz `Phi2` foi criada de forma similar a `Phi1`, mas utilizando os dados de entrada `x2`.
    *   A saída do modelo para os dados de teste (`y_est2`) foi estimada multiplicando a matriz `Phi2` pelos pesos treinados `w` (`y_est2 = Phi2 @ w`).
    *   Finalmente, um gráfico foi gerado comparando a saída real dos dados de teste (`y2`) com a saída estimada pelo modelo (`y_est2`) em função do tempo (`t2`).

Este projeto demonstra a aplicação de uma rede neural RBF para a identificação de um sistema não linear, utilizando dados de treinamento para ajustar os pesos da rede e dados de teste para avaliar a capacidade de generalização do modelo.