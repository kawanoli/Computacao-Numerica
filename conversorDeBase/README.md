# Conversor de base

*Neste projeto, eu criei um programa que realiza o processo de conversão entre bases numéricas, de uma base N qualquer para outra base N qualquer, sem usar a base decimal (base 10) de ponte.*

Inicialmente, precisamos introduzir ao leitor e usuário do programa, uma limitação inicial do projeto: só conseguimos realizar a conversão de bases até a base 36, pois é onde se "estouram" os caracteres possíveis de utilização (de "0" à "9", e de "a" à "z"); caso o usuário deseje fazer a conversão para uma base maior, precisará definir quais os próximos caracteres que podem ser utilizados após o trigésimo terceiro, adicioná-los no dicionário de caracteres possíveis de serem utilizados, e aumentar o valor que o programa "deixa passar" na verificação de base válida, ao pegar as bases digitadas pelo usuário.
> Exemplo:
Caso eu queira converter para uma base 37, eu posso definir no meu dicionário que o 36º indice do meu dicionário é ";", sendo essa uma escolha pessoal minha de caractere. Sendo assim, se eu digitar o valor 37 na base 10, e quiser converter para a base 37, o resultado impresso pelo meu programa será ";0".

Destrinchando um pouco mais sobre o funcionamento do programa desenvolvido, a lógica pensada para a conversão de base, seria com a criação de um dicionário com todos os caracteres que podem ser utilizados, de forma que o programa pudesse se referenciar por eles para saber qual caractere utilizar para representar um valor convertido, além de usar o dicionário para verificar também qual o índice que aquele caractere representa no dicionário, para poder realizar a conversão.

O método utilizado para a conversão de base no programa é o das divisões sucessivas; a escolha se deu por conta de ser um método que pode se aplicar em quaisquer conversão de base, criando assim um "caso geral". As divisões se dão por meio de referenciação ao dicionário criado, ou seja, não se trabalha diretamente com um valor, mas sim com uma referência.

A ideia por trás da conversão é bem simples: o programa vai "andando" pelo dicionário, até chegar no último caractere possível de ambas as bases (seja pra a leitura do valor de entrada, ou para o valor que deve ser convertido); ao chegar no ultimo caractere possível, adiciona-se +1 valor na próxima casa, zera a casa atual, e o resto da divisão permanece no "carry" para ser calculado e repetir o mesmo processo anteriormente feito; ao se encontrar um valor que seja menor que a base que se deseja converter (ou seja, encontrarmos a última divisão possível), o "carry" (que é o nosso resto) é posto na casa atual do programa.
> Vale destacar que, caso uma das casas subsequentes "estoure" seu limite de caracteres possíveis, a mesma fará o processo acima.

Ao final, haverá uma conversão da lista de resultados para a base correta, de modo a obter o novo valor.