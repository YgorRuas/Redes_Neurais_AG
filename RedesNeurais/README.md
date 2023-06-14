# Experimentos de redes neurais artificiais

<p align="justify"> Nesse README podemos encontrar a resolução de problemas de Redes Neurais Artificiais. Para tal, a linguagem Jupyter Notebook é predominante nos códigos, mas também, é usada a linguagem de python principalmente em funcoes.py. Ademais, foi usado o Black para uma melhor formatação dos códigos. </p>

## O que são Rdese Neurais?

<p align="justify">  Redes neurais são algoritmos que se baseiam em um processamento de dados similar ao processamento de informações de um cérebro humano que ocorrem por meio de um conjunto extremamente complexo de células, os neurônios, estes que são responsáveis pela tomada de decisão do raciocínio e corpo humanos. Portanto, os neurônios são formados por dendritos, conjuntos de terminais de entrada, pelo corpo central, e pelos axônios, além dos terminais de saídas. </p>
<p align="justify">  Desse modo, a comunicação dos neurônios ocorrem por meia da sinapse, região onde dois neurônios entram em contato e transmitem impulsos nervosos. Estabelecido o funcionamento biológico, assim, observa-se que o comportamento das redes neurais é similar ao de um neurônio visto que a estrutura computacional é baseada em um sistema três camdas, sendo um de input, dado pelo valor de entrada; a camada escondida e um neurônio que soma os valores de entrada recebidos e incrementa um viés; e por fim, o output, este sendo um valor de saída das operações. </p>

<center>
<img src='./Rededogcat.gif' style="width:900px;height:400px"/>
</center>

### Backpropagation

É um algoritmo muito utilizado em redes neurais devido o ajuste do peso das conexões entre os neurônios com o objetivo de minimizar o erro entre as saídas da rede e os valores desejados. Assim, o processo é dividido em duas etapas: propagação para frente `forward propagation` e retropropagação do erro `backwardpropagation`. 
  
<p align="justify">  Desse modo, o primeiro processo considerando os dados de entrada alimentados na rede e os valores de saída cálculados a partir da ativação dos neurônios durante a etapa de propagação para frente, é que os dados de entrada são alimentados na rede, já os de saídas são calculadas através das ativações dos neurônios, por sua vez, o segundo processo, determina que o erro entre as saídas da rede e os valores desejados, assim é propagado de volta para a rede. Ademais, os pesos das conexões são atualizados de forma a se obter um erro mínimo, utilizando o gradiente que é calculado através da derivada parcial do erro em relações aos pesos e são repetidos até que a rede forneça uma saída com um erro aceitável.  </p>

<center>
<img src='./Backprogation_Example.gif' style="width:700px;height:400px"/>
</center>

## Arquivos

<b> Arquivos .py</b>:

<p style='text-align: justify'> 📂 <a href="https://github.com/YgorRuas/Redes_Neuro_Anais/blob/main/RedesNeurais/classes.py">classes.py</a> - Neste arquivo estão alocados todas as classes criadas com o objetivo de auxiliar na otimização do código..</p>

<p style='text-align: justify'> 📂 <a href="https://github.com/YgorRuas/Redes_Neuro_Anais/blob/main/RedesNeurais/constantes.py">constantes.py</a> - Neste arquivo estão alocadas todas as constantes utilizadas nos códigos fonte para a resolução dos exercícios. É um ambiente destinado para guardar e armazenar as constantes de modo a otimizar o código.</p>

<p style='text-align: justify'> 📁 <a href="https://github.com/YgorRuas/Redes_Neuro_Anais/blob/main/RedesNeurais/funcoes.py">funcoes.py</a> - Neste arquivo, serão armazenadas todas as funções sendo utilizadas ao longo do tempo nos experimentos/projetos. Com este arquivo, a reutilização de funções nos mais diversos arquivos da pasta será possibilitada, assim como a organização será evidenciada.</p>

<p style='text-align: justify'> 📁 <a href="https://github.com/YgorRuas/Redes_Neuro_Anais/blob/main/RedesNeurais/README.md">README.md</a> - É o arquivo do readme, do repositório referente a Redes Neurais, onde fica o cartão de visita para essa seção do repositório.</p>


## Descrição dos experimentos

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

O presente git possuí como único autor [Ygor Ruas](https://github.com/YgorRuas/Redes_Neuro_Anais/tree/main), contudo, o arquivo advem da disciplina de Redes Neurais e Algoritmos Geneticos do Professor [Cassar. Daniel](https://github.com/drcassar/template_rnag), onde foI realizado uma ramificação para o desenvolvimento desse git. Além disso, como contribuições temos os alunos da primeira turma da ilum, estes que ajudaram de forma coletiva em parte da montagem e estruturação dos códigos.

## Agradecimentos

<p align="justify"> Agradecimento especial ao Professor Daniel Cassar pelo apoio no decorrer da disciplina e pelas aulas ministradas. </p>
