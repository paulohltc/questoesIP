# "A cafeteria"
[Problem](https://www.dikastis.com.br/problems/01EJGP11RGQEJQKRRJR84Y60T8)

![Cafeteria](https://github.com/paulohltc/questoesIP/blob/main/cafeteria/src/cafeteria1.jpg)

Este cenário de Among Us é composto de no **mínimo** 2 integrantes (**1 Impostor e 1 tripulante**), isso implica que, havendo mais integrantes, é possível um número maior de impostores.  A partida inicia com um jogador ausente temporariamente e os demais jogadores permanecem imóveis em função de um justo acordo prévio. Enquanto isso, o Impostor articula seus planos discretamente, cujo objetivo é matar os tripulantes mais distantes (importante observar a possibilidade de mais de 1 impostor e assim considerar a maior distância **COMUM** dos impostores envolvidos). 

Seu trabalho é identificar os tripulantes mais distantes e relatar aos impostores.

Para não haver erro ou dúvida, o impostor anexou este esboço das distâncias de um exemplo.

![Cafeteria2](https://github.com/paulohltc/questoesIP/blob/main/cafeteria/src/cafeteria2.jpg)


### INPUT
É garantido que haverá pelo menos 1 impostor e 1 tripulante e eles estão em círculo, ou seja, o primeiro está conectado com o último.

> J

Número natural >= 2 que representa a quantidade de jogadores da partida

Seguidas por J linhas do formato:

> C1 N1

Separadas por um espaço, onde C é a classe (**IMPOSTOR ou TRIPULANTE**) e **N** é o nome do jogador

>C2 N2

>. . .

>CJ NJ

No qual CJ NJ representa o último jogador da partida

### OUTPUT


Só haverá mais de um tripulante na saída caso ocorra empate nas distâncias. Se realmente houver esse empate, a ordem que deverá ser imprimida é a ordem que foi recebida na entrada 

> N1

Nome do tripulante mais distante

> N2

> . . .

> Nk

No qual Nk é o nome do último tripulante mais distante, onde K é um número natural, tal que 1 <= k < J-1


### TESTS
### Case 1:
#### Input:
```
9
TRIPULANTE Rafael
TRIPULANTE Pedro
TRIPULANTE Marcelo
IMPOSTOR Saulo
TRIPULANTE Marcos
IMPOSTOR Miguel
TRIPULANTE Jow
TRIPULANTE Gomes
TRIPULANTE Theus
```
#### Output:
```
Rafael
Theus
```
### Case 2:
#### Input
```
7
TRIPULANTE Amangos
TRIPULANTE Nandoca
IMPOSTOR agiota
TRIPULANTE guembas
IMPOSTOR palao
TRIPULANTE Leila
TRIPULANTE omacaco12
```
#### Output
```
Amangos
omacaco12
```
