# Experimentos de otimização e algoritmos genéticos

<p align="justify"> O presente repositório está em construção, então, alterações no decorrer do tempo estão sujeitas. </p>

<p align="justify"> Aqui nesse README podemos encontrar a resolução de problemas de Algoritmos Genéticos. Para tal, a linguagem Jupyter Notebook é predominante nos códigos, mas também, é usada a linguagem de python principalmente em funcoes.py. Ademais, foi usado o Black para uma melhor formatação dos códigos. </p>

### A.01 - Busca Aleatória

<p align="justify"> O objetivo principal é alcançar uma otimização passando por diversos experimentos, onde o primeiro desafio é o da Busca Aleatória, este que é um algoritmo onde certamente seria classificado como um ótimo jogador de futebol, pois sua função é "chutar" valores, assim sorteando candidatos possíveis visando a soluções para o problema. Dessa maneira, sendo um método não eficiente e que nem sempre garante que o resultado almejado será alcançado. Contudo, nem todas as esperanças se foram, pois tudo dá para otimizar, ou não... Mas nesse caso é possível, se antes a possibilidade de não obter o resultado desejado era um impasse então o segundo experimento é a solução! </p>

### A.02 - Busca em Grade

<p align="justify"> A Busca em Grade visa testar todas as combinações possíveis para cada situação, onde é determinada pelo código, entre um ou mais conjunto de parâmetros. Assim, nenhum resultado será repetido e o mesmo será alcançado, assim, sendo determinístico, no entanto, o custo computacional para grandes valores ou variáveis, normalmente é alto. </p>

# Algoritmo Genético

## O que são algoritmos genéticos

<p align="justify"> Algoritmos Genéticos consistem em uma classe de algoritmos de busca heurística inspirados no processo de seleção natural da evolução biológica, apoiando-se nas ideias de Darwin. Portanto, a ideia dos algoritmos genéticos é simular a evolução, assim, buscando o melhor individuo correlacionado a função objetivo de cada caso, normalmente, envolvendo uma maximização ou minimização. Assim, a evolução de uma população para solucionar os problemas envolvem técnicas como a utilizando de seleção, cruzamento e mutação. Desse modo, possuindo os critérios de parada, o presente método retornará o melhor individuo encontrado na função local, este que se não é o melhor individuo, normalmente é próximo do mesmo. Assim, sendo probabilístico, já que o memo caminho não será retornado no mesmo código. Por fim, são amplamente utilizados para resolver problemas de otimização em uma variedade de campos, incluindo matemática, engenharia, ciência da computação, economia, finanças, biologia entre outros. </p>

## Instruções e especificações
<p align="justify"> Os Algoritmos Genéticos sempre buscam uma otimização ou por meio de uma minimização ou por meio de uma maximização de uma função local. Assim, retornando o melhor indivíduo encontrado, o que torna o método probabilística e não determinística, diferente de uma busca por exaustão. Desse modo, sendo possível resolver problemas de forma satisfatória, como os de NP-difícil que demandariam de muito custo computacional se fosse realizada a busca por exaustão. Portanto, os Algoritmos Genéticos nem sempre garantem que a resposta encontrada é a melhor solução possível ou que o caminho para chegar a tal resposta será o mesmo. </p>

Também temos que a seção de `funcoes.py` serve para depositas as funções criadas no decorrer dos experimentos, e está onde na linguagem de python. Assim sendo importadas durante os experimentos para que a resolução dos mesmos seja possível.

<p align="justify"> Para a formatação dos códigos foi usado o Black na sua versão online. </p>

## Descrição dos experimentos

### A.03 - Caixas Binárias

<p align="justify"> Tá bom... Já está cansado de computação e ainda não resolveu o problema de modo eficiente, nesse terceiro experimento temos o Algoritmo Genético, o qual é inspirado nos princípios da evolução na natureza. Dessa maneira, seguindo os fundamentos da evolução Darwiniana onde temos os princípios da variação, mutação e seleção, além de outros parâmetros implementados como chance de cruzamento, gerações e mutação. A respeito do resultado foi possível alcançar o objetivo de encontrar uma solução para o problema das caixas binárias sendo possível afirmar que ele é mais "inteligente" que os dois anteriores, haja vista que foi mais bem elaborado. Todavia, nesse problema como o objetivo é de encontrar o valor um em todos os genes, o método de Algoritmo genético nem sempre vai levar ao resultado desejado, mesmo levando em conta as várias gerações, portanto, também necessitando de aperfeiçoamento. </p>

### A.04 - Caixas Não-Binárias

<p align="justify"> Não obstante ao experimento anterior, o Problema das caixas não-binárias também usa como base o método do Algoritmo Genético, contudo, possuí valores máximos determinados e em forma de constantes, estes que não necessariamente foram alcançados em seu máximo sempre, já que são probabilísticos. Ademais, devido a quantidade superior de números, o custo computacional é maior já que o sistema é maior.  </p>

### A.05 - Descobrindo a Senha

<p align="justify"> Um pouco diferente dos demais experimentos, o quinto desafio consiste em descobrir uma senha, portanto, também usando algumas constantes iguais aos dos experimentos anteriores, uma nova se destaca, constante essa que é usada para avaliar e julgar, como nesse método o código já consegue identificar quantos caracteres tem a senha, o problema é descobrir quais são os corretos. Desse modo, caso uma letra esteja muito distante da correta, uma penalização será feita e essa possível resposta estará mais longe na fila, seguindo essa ordem e realizando um "torneio" até que o caractere correto seja selecionado. Por fim, como o algoritmo não possui critério de parada, espera-se que após algumas tentativas, estas que não são iguais, todos os caracteres estejam corretos, assim compondo a senha desejada. </p>

### A.06 - Caixeiro Viajante

<p align="justify"> Também usando os Algoritmos Genéticos temos o sexto experimento, que é o do caixeiro viajante ou para pessoas alienadas que leram errado uma vez e não conseguem esquecer como eu, o famoso caixão viajante. Desse modo, o experimento consiste em descobrir a rota de menor distância entre 𝑛 pontos no plano cartesiano, nesse caso, assumiu-se que esses pontos são cidades e que possuem distancias diferentes, estas em que o caixeiro viajante não pode passar pela mesma cidade duas vezes. Vale destacar que o experimento foi concluído com 5 cidades e como desafio para o leitor, fica de fazer o mesmo procedimento com 30 cidades, boa sorte! </p>

### A.07 - Problema da Mochila

<p align="justify"> O problema da mochila há uma limitação de peso, diferente do experimento do Caixeiro Viajante. Desse modo, duas principais funções foram criadas, estas que representam o problema matemático em forma de código e aplicam um limite ao máximo de peso suportado pela mochila. Ademais, como o problema visa uma maximização e visando os itens que foram determinados, junto com seus respectivos pesos e valores, o algoritmo tenta alcançar o valor máximo e não extrapolar o peso para evitar a penalização. Contudo o algoritmo é probabilístico, portanto, nem sempre retornara o maior valor e a melhor solução possível, dessa maneira, o número de gerações determina quantas serão as tentativas que o código tentara. </p>

### GA.01 - Senha de Tamanho Variável 

<p align="justify"> Mediante ao problema apresentado que é da senha de tamanho variável, este que o computador não tem conhecimento do tamanho da senha e mesmo com essa problemática o objetivo é encontrar a senha desejada. Assim, usando funções semelhantes ao experimento 5 só que alteradas e criando um modo de "punir" as palavras com quantidade de caracteres errados, estes que a punição varia conforme o desvio em relação a senha correta. Punição essa que está estabelecida como constante. Desse modo, cabe salientar a respeito desse método, que o tempo de execução não foi grande, considerando o limite estabelecido de caracteres como (100), onde o tempo em relação a todas as possibilidades e ao tamanho dessa senha com a quantidade de caracteres possíveis, foi relativamente rápida. </p>

### GA.03 - Caixeiro Com Gasolina Infinita

<p align="justify"> O objetivo do **experimento GA.03** é encontrar a solução para o problema do caixeiro viajante com gasolina infinita e mostrar seu caminho de maneira gráfica. Desse modo, diferente do **experimento A.06** onde era de minimização, este é de maximização e para isso, funções como `selecao_torneio_max` foram utilizadas para que fosse possível encontrar a solução do problema. Assim, usando algoritmos genéticos para encontrar a maior distância possível. Ademais, para demonstrar o resultado foi feito um grafo que demonstra o caminho percorrido, sem repetir nenhuma cidade e retornando para a inicial, além disso, também foi feito um gráfico em coordenadas (x,y) para que fosse notável essa distância entre os pontos. </p>

## Contribuições

<p align="justify"> O presente git possuí como único autor [Ygor Ruas](https://github.com/YgorRuas/Redes_Neuro_Anais/tree/main), contudo, o arquivo advem da disciplina de Redes Neurais e Algoritmos Geneticos do Professor [Cassar. Daniel](https://github.com/drcassar/template_rnag), onde foI realizado uma ramificação para o desenvolvimento desse git. Além disso, como contribuições temos os alunos da primeira turma da ilum, estes que ajudaram de forma coletiva em parte da montagem e estruturação dos códigos. </p>

## Agradecimentos

<p align="justify"> Agradecimento especial ao Professor Daniel Cassar pelo apoio no decorrer da disciplina e pelas aulas ministradas. </p>
