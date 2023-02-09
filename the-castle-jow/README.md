# "The Castle Jow"
[Problem](https://www.dikastis.com.br/problems/01ENJKPGHCWHYQDMX7GYZPM06C)

O Algoritmo de *De Casteljau* é usado para criar curvas, que se utiliza de um conceito chamado interpolação linear.

Uma interpolação linear de dois pontos A e B é uma combinação deles, de forma que todos os pontos formados estejam na reta produzida pelos dois.
Um ponto genérico P seria descrito dessa forma para qualquer **t** real:

* **P =(1-t)*A + t*B** 

Note que para **t** entre 0 e 1, o ponto P estará no segmento AB.


O Algoritmo de *De Casteljau* funciona da seguinte forma:
Dado *n* pontos onde a ordem importa, chamados de C (pontos de controle), pra um *t* específico, calcule as interpolações dois a dois desses pontos (C1 e C2, C2 e C3, ... , Cn-1 e Cn). Pegue essas interpolações e interpole dois a dois novamente com o mesmo *t*, e continue fazendo isso até se resumir em um ponto. Esse ponto pertence a curva (chamada de Curva de Bézier).

![gif](https://upload.wikimedia.org/wikipedia/commons/f/f4/Bezier_Linear_Interpolation.gif)


No contexto da questão, só utilizaremos o *t* variando entre 0 e 1.
É necessário que trate os pontos como tuplas bidimensionais.

No caso teste 2 por exemplo, pro t = 0.25, a primeira interpolação de (0,0) e (1,0) ficaria (0.75).(0,0)+(0.25).(1,0) = (0.25,0) a segunda interpolação seria de (1,0) e (0,1), ficando (0.75,0.25). Fazendo a última interpolação de (0.25,0) e (0.75,0.25) ficaria (0.75).(0.25,0) + (0.25).(0.75,0.25) = (0.375,0.0625) que é arredondado pra (0.38,0.06).


* Utilize a função round para tratar o arredondamento.


### INPUT
A primeira entrada *n* é um inteiro 2<=n<=20 que representa a quantidade de pontos de controle, seguidas por n linhas com os pontos de controle na forma CX e CY, separados por um espaço, onde  |CX| < 100 e  |CY| < 100 e ambos são inteiros.

>n

>C1X C1Y

>C2X C2Y

>..

>CnX CnY

Seguido por Q, a quantidade de *t*'s consultados, que é um inteiro tal que
1<= Q <= 500, seguidas por Q linhas com os valores de t, tal que t é um valor decimal e 0 <= t <= 1.

> Q

> t1

> t2

> ...

> tq
### OUTPUT
Sua saída deve ser composta com Q pontos resultante P do Algoritmo de *De Casteljau*, onde cada PX e PY são valores flutuantes arredondados para 2 casas decimais separadas por um espaço.

>P1X P1Y

>P2X P2Y

> ...

>PQX PQY

### TESTS
### Case 1
#### Input
```
4
0 0
1 1
3 1
4 0
5
0
0.25
0.5
0.75
1
```
#### Output
```
0.00 0.00
0.91 0.56
2.00 0.75
3.09 0.56
4.00 0.00
```
### Case 2
#### Input
```
3
0 0
1 0
0 1
3
0.25
0.5
0.75
```
#### Output
```
0.38 0.06
0.50 0.25
0.38 0.56
```