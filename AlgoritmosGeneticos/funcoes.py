import random

def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    Args:
        indivíduo: lista contendo os genes das caixas binárias.
    Return:
        A soma dos genes do indivíduo.
    """
    return sum(individuo) 

def gene_cb():
    """Fornece um gene válido ao problema das caixas binárias
    Return:
        Um valor zero ou um.
    """
    lista = [0,1]
    gene = random.choice(lista)
    return gene
def individuo_cb(n):
    """Gera um individuo ao problema das caixas binárias.
    Args:
        n: número de genes do indivíduo.
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo

def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.
    
    Args:
      tamanho: tamanho da população.
      n: número de genes de um individuo
    
    Returns:
        Uma Lista onde cada item é um individuo. Um individuo é uma lista com n genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao


def selecao_roleta_max(populacao, fitness):
    """seleciona individuos de uma população usando método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
        populacao: lista com todos os individuos da população
        fitness: lista com o valor da funcao objetivo dos individuos da população
        
    Returns:
        População dos indivíduos selecionados.
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def funcao_objetivo_pop_cb(individuo):
    """ Computa a funcao objetivo no problema das caixas binárias
    
    Args:
       populacao: lista contendo os genes das caixas binárias
       
    Return:
       Um valor representando a soma dos genes do individuo.
    """
    
    return sum(individuo)

def funcao_objetivo_pop_cb(populacao):
    """calcula a funcao objetivo para todos os membros de uma população
    
    Args:
       populacao: lista com todos os individuos da população
       
    Return:
       Liista de valores representando a fitness de cada individuo da população
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness

def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.
    
    Args:
       pai: uma lista representando um individuo
       mae: uma lista representando um individuo
       
    Returns:
       Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2


def mutacao_cb(individuo):
    """ Reakiza a mutação de um gene no problema das caixas binárias
    
    Args:
        individuo: uma lista representando um individuo no problema das caixas binárias
        
    Return:
       Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo