# Projeto de Computação Numérica: Resolução de Equações Diferenciais Ordinárias

Este projeto explora a **resolução numérica de Equações Diferenciais Ordinárias (EDOs)**, um tópico central da matemática aplicada com vasta aplicação em áreas como física e engenharia. Dada a dificuldade em encontrar soluções analíticas para muitas EDOs, este trabalho se concentra na implementação e comparação de métodos numéricos para obter **aproximações das soluções**.

**Métodos Numéricos Implementados e Analisados:**

1.  **Método de Euler:**
    *   Este é um dos **métodos mais simples e fundamentais** para resolver EDOs, aproximando a solução através de uma aproximação linear em pequenos passos de tempo.
    *   A fórmula recursiva utilizada é: $y_{n+1} = y_n + h \cdot f(t_n, y_n)$, onde $h$ é o passo de integração.
    *   O Método de Euler destaca-se pela sua **simplicidade de implementação e entendimento**.
    *   A **precisão** depende do tamanho do passo $h$, com um erro global de ordem $O(h)$, o que significa que a precisão melhora linearmente com a redução do passo.
    *   O método pode ser **instável**, especialmente para EDOs rígidas ou grandes intervalos de tempo, onde o erro pode crescer rapidamente.

2.  **Método de Runge-Kutta:**
    *   Este projeto também analisou o Método de Runge-Kutta (RK), com foco principal no **Método de Runge-Kutta de quarta ordem (RK4)**, uma família de métodos mais avançados que visa melhorar a precisão do Método de Euler.
    *   O RK4 calcula uma **média ponderada de várias estimativas da derivada** em cada passo para obter uma aproximação mais precisa.
    *   A fórmula geral do RK4 é apresentada no documento.
    *   O RK4 oferece **alta precisão**, com um erro global de ordem $O(h^4)$, uma melhoria significativa em relação ao Método de Euler.
    *   Apesar de ser **mais complexo** de implementar e possuir um **custo computacional maior** devido aos múltiplos cálculos por passo, o RK4 é **mais estável** e robusto, especialmente para EDOs rígidas, permitindo o uso de passos maiores sem grande perda de precisão.

**Implementação no Projeto:**

*   Devido à exigência de implementação manual sem o uso de bibliotecas nativas do Python, as soluções primárias apresentadas neste trabalho utilizam o **Método de Euler**. Foi escolhido um tamanho de passo ($dt$ ou $h$) que busca um equilíbrio entre **boa precisão e baixo custo computacional**.
*   Para fins de comparação e validação, ao final de cada questão, é apresentada uma **resolução breve utilizando o Método de Runge-Kutta** através da função `solve_ivp` da biblioteca SciPy. Esta função, otimizada em C++, permite comparar os resultados com a implementação manual do Método de Euler de forma eficiente. A implementação manual do Método de Runge-Kutta não é o foco principal deste trabalho.

**Aplicações e Simulações:**

Este projeto aplica os métodos numéricos a três sistemas dinâmicos distintos para ilustrar sua funcionalidade e comportamento:

1.  **Sistema de Duas Massas Acopladas:**
    *   Foi modelado um sistema composto por duas massas conectadas por molas e amortecedores, sujeito a uma força externa.
    *   As equações diferenciais que descrevem o movimento do sistema foram definidas.
    *   O sistema foi simulado utilizando o **Método de Euler** para obter os deslocamentos das massas em função do tempo e gerar diagramas de fase.
    *   A influência de diferentes parâmetros do sistema (massas, constantes das molas, coeficientes de amortecimento e força externa) na resposta do sistema foi explorada.
    *   Os resultados obtidos com o Método de Euler foram comparados com aqueles gerados pela função `solve_ivp` (RK4/5) do SciPy, demonstrando semelhanças visuais nos resultados. A comparação destacou a tendência do Método de Euler em acumular erro ao longo do tempo em sistemas dinâmicos mais complexos, enquanto o Runge-Kutta oferece maior precisão.

2.  **Modelo de Predador-Presa:**
    *   Um modelo clássico de interação entre populações de presas e predadores foi implementado utilizando equações diferenciais.
    *   Simulações numéricas com o **Método de Euler** foram realizadas para analisar pontos críticos, o comportamento do sistema com diferentes condições iniciais e o impacto da caça na população de predadores.
    *   Os resultados foram visualizados através de gráficos da população de presas e predadores ao longo do tempo, bem como diagramas de fase.
    *   A comparação com a solução obtida através da função `solve_ivp` (Runge-Kutta) revelou que o Método de Euler pode apresentar oscilações ou irregularidades, especialmente com passos não suficientemente pequenos, enquanto o Runge-Kutta fornece uma solução mais suave e precisa.

3.  **Pêndulo Amortecido:**
    *   O comportamento de um pêndulo amortecido foi modelado por um sistema de equações diferenciais não lineares.
    *   O **Método de Euler** foi utilizado para simular a posição e a velocidade angular do pêndulo em função do tempo, além de gerar o diagrama de fase.
    *   A simulação foi ajustada para exibir um comportamento de subamortecimento, onde as oscilações diminuem de amplitude ao longo do tempo devido à dissipação de energia.
    *   A comparação com os resultados obtidos com a função `solve_ivp` (Runge-Kutta) mostrou uma concordância notável para este tipo de simulação mais simples e rápida, validando a implementação do Método de Euler.

**Conclusões Gerais:**

*   O **Método de Euler** é uma ferramenta simples e computacionalmente eficiente para a resolução numérica de EDOs, mas sua **precisão é limitada** e pode acumular erros significativos ao longo do tempo, especialmente em sistemas dinâmicos complexos.
*   O **Método de Runge-Kutta**, embora mais complexo e custoso computacionalmente, oferece uma **precisão muito maior** e é mais robusto para uma ampla gama de problemas, incluindo EDOs rígidas e simulações de longo prazo.
*   Para modelagens iniciais e problemas mais simples, o **Método de Euler pode ser suficiente** para obter uma primeira análise do comportamento do sistema. No entanto, para problemas que exigem maior precisão, o **Método de Runge-Kutta é preferível**.
*   A utilização da função `solve_ivp` do SciPy demonstrou ser uma ferramenta eficiente e precisa para a resolução de EDOs, sendo preferível para implementações que necessitam de alta performance e precisão, especialmente em sistemas complexos ou simulações de longa duração.

Este projeto fornece uma análise prática e comparativa de dois importantes métodos numéricos para a resolução de EDOs, ilustrando suas características, vantagens e limitações através de aplicações em sistemas dinâmicos relevantes.