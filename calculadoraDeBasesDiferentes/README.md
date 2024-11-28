# Calculadora de Bases Diferentes

Nesta pasta, se encontra presente o meu projeto final da unidade 1 de Computação Numérica.
O objetivo do projeto é o desenvolvimento de um algoritmo capaz de realizar soma e multiplicação entre dois valores de bases diferentes, retornando o resultado final em uma base de escolha do usuário também.

Inicialmente, ao desenvolver esse código, realizei a implementação do algoritmo de conversão entre bases para o recebimento de entradas do tipo Int, desconsiderando que entradas do tipo Float também deveriam ser válidas. Sendo assim, precisei realizar alterações no algoritmo para que ele se adequasse à proposta do projeto, que era de tornar a calculadora funcional para quaisquer entrada.

No arquivo .ipynb, podemos ver que o primeiro código disponível é justamente o da conversão com inteiros, sendo esse o mesmo código que já disponibilizei aqui na pasta de conversorDeBase; abaixo dele, coloquei a adaptação de funcionalidade que fiz para que o código recebesse também Float. A abordagem que tive foi be simples: eu já estava conseguindo converter Int, então porque não "quebrar" o meu código em dois inteiros, um pré e um pós vírgula? Com essa premissa, realizei a alteração do algoritmo, podendo então proceder para a parte das operações.

Inicialmente, quis garantir que ao menos funcionasse usando a base 10 de ponte, ou seja, pegasse as duas entradas, transformasse em dois valores na base 10, para que a soma e a multiplicação fossem feitas da forma mais simples possível (literalmente "+" e "*"); garantindo que esse algoritmo funcionasse, poderia partir daí para um algoritmo que destrinchasse melhor os calculos de soma e multiplicação, realizando eles sem a base 10 de ponte.

A ideia para a realização da soma e multiplicação entre bases diferentes, sem a ponte 10, foi a seguinte: não podemos realizar a conversão para base 10, porém podemos converter os dois valores para a base final escolhida pelo usuário; sendo assim, com os dois novos valores na base escolhida para a saída, podemos realizar as operações.