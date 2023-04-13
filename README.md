# Redes Neurais e Algoritmos Genéticos, a busca pela otimização e aperfeiçoamento

<p style='text-align: justify'> O presente repositório está em construção, então, alterações no decorrer do tempo estão sujeitas. </p>

<p style='text-align: justify'> Aqui nesse README podemos encontrar a resolução de problemas de Algoritmos Genéticos e de Redes Neurais. Para tal, a linguagem Jupyter Notebook é predominante nos códigos e a linguagem de Phython também é usada de forma sutil nesse repositório. </p>

<p style='text-align: justify'> O objetivo principal é alcançar uma otimização passando por diversos experimentos que estão ou estarão disponíveis em suas determinadas seção, onde os primeiros experimentos são de Algoritmos Genéticos e o primeiro desafio é o da Busca Aleatória. </p>

### Algoritmo de Busca Aleatória e Busca em Grade

<p style='text-align: justify'> O algoritmo de Busca Aleatória nem sempre garante que o resultado almejado será alcançado, apresentando assim uma ineficiência em vários caso, todavia, no segundo experimento que é o da Busca em Grade nenhum resultado será repetido e o mesmo será alcançado, no entanto, esse método precisa ser mais polido já que várias tentativas foram necessárias, elevando o custo computacional e o tempo. Ambos os algoritmos foram usados para o problema das caixas binárias, com 4 unidades e em ambos uma otimização é possível. </p>

### Algoritmo Genético

#### Caixas Binárias

<p style='text-align: justify'> Nesse terceiro experimento temos o Algoritmo Genético, o qual é inspirado nos princípios da evolução na natureza. Dessa maneira, seguindo os fundamentos da evolução Darwiniana onde temos os princípios da variação, herança e seleção, além de outros parâmetros implementados como chance de cruzamento, gerações e mutação. A respeito do resultado foi possível alcançar o objetivo de encontrar uma solução para o problema das caixas binárias sendo possível afirmar que ele é mais "inteligente" que os dois anteriores, haja vista que foi mais bem elaborado. Todavia, nesse problema como o objetivo é de encontrar o valor um em todos os genes, o método de Algoritmo genético nem sempre vai levar ao resultado desejado, mesmo levando em conta as várias gerações, portanto, também necessitando de aperfeiçoamento. </p>

#### Caixas Não-Binárias

<p style='text-align: justify'> Não obstante ao experimento anterior, o Problema das caixas não-binárias também usa como base o método do Algoritmo Genético, contudo, possuí valores máximos determidos e em forma de constantes, estes que não necessáriamente foram alcançados em seu máximo sempre. Ademais, devido a quantidade superior de números, o custo computacional é maior já que o sistema é maior. E em todos os algoritmos até o devido momento uma otimização é possível e para conhecer esses novos algoritmos aguarde por novas atualizações. </p>

#### Descobrindo a Senha

<p style='text-align: justify'> Um pouco diferente dos demais experimentos, o quinto desafio consiste em descobrir uma senha, portanto, também usando algumas constantes iguais aos dos experimentos anteriores, uma nova se destaca, constante essa que é usada para avaliar e julgar, como nesse método o código já consegue identificar quantos caracteres tem a senha, o problema é descobrir quais são os corretos. Desse modo, caso uma letra esteja muito distante da correta, uma penalização será feita e essa possível resposta estará mais longe na fila, seguindo essa ordem e realizando um "torneio" até que o caractere correto seja selecionado. Por fim, como o algoritmo não possui critério de parada, espera-se que após algumas tentativas a todos os caracteres estejam corretos, assim compondo a senha desejada. </p>

#### Caixeiro Viajante

<p style='text-align: justify'> Também usando os Algoritmos Genéticos temos o sexto experimento, que é o do caixeiro viajante ou para pessoas alienadas que leram errado uma vez e não conseguem esquecer como eu, o famoso caixão viajante. Desse modo, o experimento consiste em descobrir a rota de menor distância entre 𝑛 pontos no plano cartesiano, nesse caso, assumiu-se que esses pontos são cidades e que possuem distancias diferentes, estas que o caixeiro viajante não se pode passar pela mesma cidade duas vezes. </p>

#### Problema da Mochila

<p style='text-align: justify'> Indiferente dos demais no quesito método, aqui também usá-se os Algoritmos Genéticos, onde o problema da mochila há uma limitação de peso. Desse modo, duas principais funções foram criadas, estas que representam o problema matemático em forma de código e aplicam um limite ao máximo de peso suportado pela mochila. Ademais, como o problema visa uma maximização e visando os itens que foram determinados, junto com seus respectivos pesos e valores, o algoritmo tenta alcançar o valor máximo e não extrapolar o peso para evitar a penalização. Contudo o algoritmo é probabilístico, portanto, nem sempre retornara o maior valor e a melhor solução possível, dessa maneira, o número de gerações determina quantas serão as tentativas que o código tentara. </p>