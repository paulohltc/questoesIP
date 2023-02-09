# "Números Mágicos"
[Problem](https://www.dikastis.com.br/problems/01EKMT4Q0V723PQS129YV8MS13)

Cobb está precisando de uma arquiteta nova para desenhar os sonhos no seu plano de Inception. Não podia ser uma pessoa qualquer, precisa ser uma excepcional no que faz, já que isso é muito importante para ele, e precisa ocorrer tudo de maneira perfeita. Ariadne se interessou em participar mas precisava fazer alguns testes para mostrar sua competência, e precisou da sua ajuda para isso.


![Inception](https://media.giphy.com/media/1412QM7NaCZMyc/giphy.gif)


O teste 1 de Cobb seria um teste de raciocínio matemático. **Ele definiu que uma sequência de números é considerada mágica se e somente se a razão do MMC (mínimo múltiplo comum) pelo MDC (maior divisor comum) for diferente do próprio MMC e diferente de 1**. Seu trabalho é dizer se uma sequência de números é mágica e o correspondente grau de mágica. O grau de mágica foi definido por Arthur, amigo de Cobb como o **fatorial da quantidade de números da sequência, depois somado com a razão do MMC/MDC**.


![Spin](https://media.giphy.com/media/9UqRcQHzBou6A/giphy.gif)


Cobb instruiu que a solução desse e dos demais testes fosse usando recursão, já que irão se basear nisso no plano de Inception.

### INPUT
> T

> Q1

> N1 N2 ... NQ1

> Q2

> N1 N2 ... NQ2

> ...

> QT

> N1 N2 ... NQT

* Sendo T um inteiro tal que 1 <= T <= 100 que representa a quantidade de casos testes

Seguido por T casos testes compostos de:



* Qi onde cada Qi, com i variando de 1 até T, é um inteiro tal que
1 <= Qi <= 10

Seguido por Qi números separados entre si por um espaço
* N1 N2 ... NQi onde cada número Nk pertencente à sequência, com k variando de 1 até Qi, é um inteiro tal que -1024 <= Nk <= 1024, com Nk diferente de 0

### OUTPUT

Aparecendo T respostas R, uma pra cada caso teste.

> R1

> R2

> ...

> RT


Se naquele caso teste os números forem feios imprima:

> "Numeros feios"

Se forem mágicos imprima:

> "Numeros magicos! " concatenado com X


* Onde X é um racional de aproximação de 1 casa decimal

X representando a grau de mágica daquela sequência

### TESTS
### Case 1
#### Input
```
1
6
16 18 24 36 48 20
```
#### Output
```
Numeros magicos! 1080.0
```
### Case 2
#### Input
```
3
3
11 110 121
1
1024
4
32 24 20 28
```
#### Output
```
Numeros magicos! 116.0
Numeros feios
Numeros magicos! 864.0
```