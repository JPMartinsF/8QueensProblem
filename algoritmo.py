#Joao Pedro Martins
#Disciplina: Inteligência Artificial
#Semestre: 2019.2

#Professor: Sergio Palma

from random import sample
from statistics import median

#Geração dos pais:
#Seis pais serao gerados com genes definidos aleatoriamente
def criaGene():
  gene = sample(range(0,8),8)
  return gene

#Calculo do custo:
#Se for adjacente ou estiver na mesma linha diagonal ou horizontal, aumenta o custo
def calculaCusto(gene):
  custo = 0
  for index in range(len(gene) - 1):
    for nextIndex in range(index + 1, len(gene)):
      if (abs((gene[index] - gene[nextIndex])) == (nextIndex - index) or gene[index] == gene[nextIndex]):
        custo += 2
  return custo
def calculaCustoGeracao(listaGeracao):
  custoGeracao = 0
  for gene in listaGeracao:
    custoGene = calculaCusto(gene)
    #print(custoGene)
    custoGeracao += custoGene
  #print()
  #print(custoGeracao)
  return custoGeracao

#Crossover:
#Pares seguidos de pais farao crossover de metade de seus genes (pai1 e pai2, etc)
#Se houver numero repetido, o programa ira colocar os que faltam em ordem crescente
#def diferencaLista(lista1, lista2):
#  return list(set(lista1) - set(lista2))

def diferencaLista(lista1, lista2):
  out = []
  for ele in lista1:
    if not ele in lista2:
      out.append(ele)
  return out

def crossover(pai1, pai2):
  gene11 = pai1[:4]
  gene12 = pai1[4:]
  gene21 = pai2[:4]
  gene22 = pai2[4:]
  
  filho1 = gene11 + gene22
  filho2 = gene21 + gene12
  filho1 = list(dict.fromkeys(filho1))
#  print(filho1)
  filho2 = list(dict.fromkeys(filho2))
#  print(filho1, filho2)
#  print(diferencaLista(range(8), filho1))
  filho1 += diferencaLista(range(8), filho1)
  filho2 += diferencaLista(range(8), filho2)
#  print(filho1, filho2)
  return [filho1, filho2]

#gene1 = criaGene()
#gene2 = criaGene()
#print(gene1, gene2)
#print(diferencaLista(gene1, gene2))
#crossover(gene1, gene2)

#Mutacao:
#A cada crossover, os filhos irao sofrer mutacao na qual cada um troca dois genes de posicao, os mutantes serao um novo par de filhos

def mutacao(gene):
  novoGene = gene[:]
  trocaGenes = sample(range(0,8),2)
  aux = novoGene[trocaGenes[0]]
  novoGene[trocaGenes[0]] = novoGene[trocaGenes[1]]
  novoGene[trocaGenes[1]] = aux
  return novoGene

#gene = [0,1,2,3,4,5,6,7]
#print(gene)
#print(mutacao(gene))

#Cricao de nova geracao:
#Cada par de pais ira fazer crososver e gerar quatro filhos desse crossover, dois "comuns" e dois que sofrerao mutacao

def criaGeracao(listaGeracao):
  listaNovaGeracao = []
  for i in range(0,5,2):
    filhos = crossover(listaGeracao[i], listaGeracao[i + 1])
    mutantes = filhos[:]
    for index in range(len(mutantes)):
      mutantes[index] = mutacao(mutantes[index])
    listaNovaGeracao += filhos + mutantes
  return listaNovaGeracao

#Evolucao elitista:
#A cada geracao, a metade com maior custo sera descartada

def elitismo(listaGeracao):
  listaElitista = []
  listaCusto = []
  for elem in listaGeracao:
    listaCusto += [calculaCusto(elem)]
  mediana = median(listaCusto)
  
  for elem in listaGeracao:
    custo = calculaCusto(elem)
    if (len(listaElitista) == 6):
      break
    if (custo <= mediana):
      listaElitista += [elem]
  return listaElitista

#Algoritmo em execucao

pai1 = criaGene()
pai2 = criaGene()
pai3 = criaGene()
pai4 = criaGene()
pai5 = criaGene()
pai6 = criaGene()
geracaoUm = [pai1, pai2, pai3, pai4, pai5, pai6]

print("Primeira Geracao\n")
for pai in geracaoUm:
  print(pai)  
  print(calculaCusto(pai))
print(calculaCustoGeracao(geracaoUm))
print()
#print("Segunda Geracao sem elitismo\n")
geracaoDois = criaGeracao(geracaoUm)
#for pai in geracaoDois:
#  print(pai)  
#  print(calculaCusto(pai))
#print(calculaCustoGeracao(geracaoDois))
print()
geracaoDois = elitismo(geracaoDois)
print("Segunda Geracao com elitismo\n")
for pai in geracaoDois:
  print(pai)
  print(calculaCusto(pai))
print(calculaCustoGeracao(geracaoDois))
print()
#print("Terceira Geracao sem elitismo\n")
geracaoTres = criaGeracao(geracaoDois)
#for pai in geracaoTres:
#  print(pai)  
#  print(calculaCusto(pai))
#print(calculaCustoGeracao(geracaoDois))
print()
geracaoTres = elitismo(geracaoTres)
print("Terceira Geracao com elitismo\n")
for pai in geracaoTres:
  print(pai)
  print(calculaCusto(pai))
print(calculaCustoGeracao(geracaoTres))
print()
#print("Quarta Geracao sem elitismo\n")
geracaoQuatro = criaGeracao(geracaoTres)
#for pai in geracaoQuatro:
#  print(pai)  
#  print(calculaCusto(pai))
#print(calculaCustoGeracao(geracaoDois))
print()
geracaoQuatro = elitismo(geracaoQuatro)
print("Quarta Geracao com elitismo\n")
for pai in geracaoQuatro:
  print(pai)
  print(calculaCusto(pai))
print(calculaCustoGeracao(geracaoQuatro))
