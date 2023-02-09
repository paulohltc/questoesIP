# "Labirintos Mágicos"
[Problem](https://www.dikastis.com.br/problems/01EKTC8S8KJ15Z11V2RZ323KVM)

Após Ariadne passar no teste 1 (Números Mágicos), realizado por Cobb, ela deveria mostrar que era capaz de criar labirintos que possuíssem saídas. Dessa forma, resolveu criar um algoritmo para provar sua habilidade. Como ela não possuía muita familiaridade com programação, pediu sua ajuda.


![](https://media.giphy.com/media/ZzQDCNn6pKRmU/giphy.gif)


O Algoritmo idealizado consistia em uma matriz 10x10 onde a entrada estava localizada exatamente na primeira casa da linha 0 e coluna 0, e a saída estava na ponta oposta da matriz (9, 9). Ela lhe forneceu as seguintes informações: 

* Os 1's da matriz era o caminho que ele poderia percorrer, e os 0's eram locais inacessíveis.
* Você só poderá se deslocar na vertical e horizontal
* Em caso de bifurcação, essa deve ser a ordem de prioridade: Sul > Leste > Norte > Oeste.
* O mapa não tinha caminhos circulares.

(este problema deve ser resolvido utilizando recursão)


### INPUT
10 linhas contendo 10 números que podem ser 0's e 1's, correspondendo ao mapa. Sendo o primeiro número da primeira linha sempre 1.

### OUTPUT
Uma única linha contendo:

> **“Esse labirinto possui saída!”**

Caso seja possível sair do labirinto.

OU

> **“Esse labirinto não possui saída!”**

Caso não seja possível sair do labirinto


### TESTS
### Case 1
#### Input
```
1 0 1 0 0 0 0 0 0 0
1 0 1 1 0 0 0 0 0 0
1 1 1 0 0 1 0 0 0 0
1 0 0 0 0 1 0 0 0 0
1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 1 1 1 1 1

```
#### Output
```
Esse labirinto possui saída!
```
### Case 2
#### Input
```
1 0 1 0 0 0 0 0 0 0
1 0 1 1 0 0 0 0 0 0
1 1 1 0 0 1 0 0 0 0
1 0 0 0 0 1 0 0 0 0
1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 1 0 0 0 1
```
#### Output
```
Esse labirinto não possui saída!
```