# Experimentos de redes neurais artificiais

<p align="justify"> Nesse README podemos encontrar a resolução de problemas de Redes Neurais Artificiais. Para tal, a linguagem Jupyter Notebook é predominante nos códigos, mas também, é usada a linguagem de python principalmente em funcoes.py. Ademais, foi usado o Black para uma melhor formatação dos códigos. </p>

### R.01 - Derivadas

Esse material não possuí um desafio, mas sim, uma introdução a derivadas, sendo de extrema impotância no decorrer do repositório.

### R.02 - Classes

A respeito desse experimento, tem-se que ele foca principalmente na introdução do funcionamento das classes. Desse modo, entendendo a estrutura, como são os métodos `dunder` e não `dunder`, fomos introduzidos a como alterar a classe e também como realizar alterações fora dela. Assim, por meio dos novos conceitos, um desafio foi proposto, cujo objetivo é adicionar um novo argumento no método `__init__`.

### R.03 - Construindo um Grafo Automaticamente

Por meio desse experimento, fomos introduzidos a como iniciar a construção de uma rede neural artificial. Assim entendendo a estrutura, como funcionam os operadores de adição e multiplicação, a estrutura dos progenitores, o operador mãe e como plotar um grafo. Desse modo, compreendendo como funcionam as classe, foi possível criar uma que gerasse automaticamente um `grafo computacional`, este que representa todas as operações matemáticas que ocorreram ao se computar um certo valor, onde o valor foi com base no grafo feito na aula do dia 27/04/2023. Portanto, o valor utilizado foi $g$, para que fosse possível visualizar todo o grafo, assim, sendo útil para experimentos futuros os quais necessitam do grafo computacional como na computação dos gradientes  para realizar o `backpropagation`.

Imagem gerada pelo Graphviz Online, para plotar a rede neural criada no experimento R.03

![image](https://user-images.githubusercontent.com/106711102/236648255-cf1bd3c1-328a-4ae4-8a2d-22d59af40e8f.png)

### R.04 - Computando Gradientes Locais

O presente desafio, foca na implementação de gradientes locais e do cálculo de backpropagation para a classe usada no experimento anterior, onde, buscamos uma otimização e automatização do processo, portanto, usamos métodos como o `propagar` e algoritmos de `autograd`, resultando em uma classe capaz de criar um grafo a e executar o `backpropagation`, sem apresentar problemas matemáticos ou erro em algum dos vértices, para a rede representada pelo grafo.

### R.05 - Finalizando a Classe Valor

Esse experimento, por meio das classes, apresenta algumas operações necessárias para que seja usada em redes neurais artificiais. Assim é introduzido a classe `Valor`  a qual é uma implementação que representa valores numéricos e permite operações como adição, multiplicação, exponenciação, divisão e as mesmas em ordem invertida, além de conseguir a aplicação da função sigmoide. Assim, são importantes pois muitas operações matemáticas são realizadas nessas redes, como soma ponderada, multiplicação por pesos, cálculos de ativação e propagação de gradientes. Portanto, ao implementar a classe `Valor` com essas funcionalidades, torna-se possível utilizá-la como base para construir uma rede neural artificial mais completa.

### R.06 - Redes Neurais Artificiais

O notebbok referente a **Redes Neurais Artificiais**, nos apresenta a como criar uma rede neural artificial usando Python. Dessa maneira, construindo uma rede neural multicamadas de forma que seja possível criar uma rede que seja capaz de processar informações e realizar operações com base em sinapses artificiais ponderadas, somas, propagação dos dados entre outros que foi determinado na classe `Valor` e criado no **experimento R.04**, mas também disponível no arquivo `classes.py`. Além disso, é introduzida a ideia de uma camada de neurônios e também é apresentado o conceito de Multilayer Perceptron (MLP).

### R.07 - Treinando uma rede neural

A respeito desse desafio o principal objetivo desse notebook é treinar uma rede neural artificial tipo Multilayer Perceptron usando Python. Assim, é apresentado um exemplo de treinamento de uma rede neural artificial tipo Multilayer Perceptron (MLP) usando Python puro, este que descreve a criação das classes necessárias para construir a rede neural, incluindo a classe Neuronio, a classe Camada e a classe MLP, além de importar a classe qeu foi crida e usada nos materias anteriores `Valor`. Além disso foi intoduzido a função de perda `loss function`, esta que calcula a soma dos erros quadráticos entre as previsões e os valores verdadeiros.

### R.08 - Treinando uma rede neural usando pytorch

Em sequêmcia ao notebook anterior (**experimento R.07**), esse possúi o objetivo de treinar uma rede neural artificial tipo Multilayer Perceptron usando pytorch. Assim, é ressaltado os motivos para utilizar PyTorch, como sua otimização eficiente, ampla variedade de funcionalidades prontas para uso, suporte ao treinamento em GPUs e sua relevância tanto na academia quanto no mundo corporativo, sendo bem mais eficiente do que a rede neural que foi criada no decorrer do semestre. Portanto, através do exemplo apresentado (dos diamantes), é possível compreender as etapas envolvidas no treinamento de uma rede neural, desde a preparação dos dados até a avaliação do modelo, que foi feito um treinamento e depois o teste, evidenciando a eficacia desse método e da biblioteca pytorch.

## Contribuições

<p align="justify"> O presente git possuí como único autor [Ygor Ruas](https://github.com/YgorRuas/Redes_Neuro_Anais/tree/main), contudo, o arquivo advem da disciplina de Redes Neurais e Algoritmos Geneticos do Professor [Cassar. Daniel](https://github.com/drcassar/template_rnag), onde foI realizado uma ramificação para o desenvolvimento desse git. Além disso, como contribuições temos os alunos da primeira turma da ilum, estes que ajudaram de forma coletiva em parte da montagem e estruturação dos códigos. </p>

## Agradecimentos

<p align="justify"> Agradecimento especial ao Professor Daniel Cassar pelo apoio no decorrer da disciplina e pelas aulas ministradas. </p>
