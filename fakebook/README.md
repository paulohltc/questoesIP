# "Fakebook"
[Problem](https://www.dikastis.com.br/problems/01EP2KFYYSQSX3ZMXXD11G3CGZ)

> Essa questão deve ser feita usando dicionário.

![fakebook](https://media.giphy.com/media/jAcErkAtRU4x2/giphy.gif)

Um grupo de amigos estava curioso pra saber quem era amigo de quem na rede social Fakebook. Eles entendiam por amigo de uma pessoa P, qualquer pessoa adicionada diretamente de P ou qualquer pessoa que fosse amiga de um amigo de P, até brincavam dizendo "Um amigo de meu amigo também é meu amigo".

Lembrando que uma amizade no Fakebook é mutua, se Aroldo é amigo de Fernando, fica implícito que Fernando é amigo de Aroldo.

O caso teste 1, por exemplo:
> {Aroldo:
Fernando, Guilherme, Joao}

> {Fernando:
Aroldo, Guilherme} 

> {Guilherme:
Aroldo, Fernando, Joao}

> {Joao:
Aroldo, Guilherme, Dindo}

Fernando e Dindo são amigos, já que Fernando é amigo de Aroldo, Aroldo amigo de Joao, e Joao amigo de Dindo.

Seu objetivo é criar um programa que, dadas 2 pessoas e seus ciclos de amizade, verifiquem se elas são amigas ou não


### INPUT
A entrada começa com um natural P, representando a quantidade de pessoas citadas. Seguido de P linhas N, representando os nomes delas.

> P

> N1

> N2

> ...

> NP

A próxima linha é um inteiro Q>=0 que diz a quantidade de amizades diretas.
Seguido por Q linhas A, com AiP1 e AiP2 separados por espaço, onde P1 e P2 significa P1 é amigo de P2, e i variando de 1 até Q. É garantido que essas AiP1 e AiP2 estão nas linhas N1,N2 ... NP.

> Q

> A1P1 A1P2

> A2P1 A2P2

> ...

> AQP1 AQP2

* SEGUIDO POR "1"

> 1


Seguido por X e Y, separados por um espaço, onde X e Y significam os nomes pelos quais você irá verificar se X é amigo de Y.
> X Y
### OUTPUT
> R

Onde R é a resposta pro problema, sendo "SIM" caso X e Y sejam amigos e "NÃO" caso contrário

### TESTS
### Case 1
#### Input
```
5
Aroldo
Fernando
Joao
Guilherme
Dindo
5
Aroldo Fernando
Guilherme Aroldo
Joao Aroldo
Guilherme Fernando
Dindo Joao
1
Aroldo Dindo
```
#### Output
```
SIM
```
### Case 2
#### Input
```
5
Paulo
Nathan
Fabricio
Luis
Guilherme
3
Paulo Guilherme
Nathan Fabricio
Luis Fabricio
1
Fabricio Paulo
```
#### Output
```
NAO
```