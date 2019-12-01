'''def funcao():
  return [1,2]
lista = []
lista += funcao()
print(lista)'''

def diferencaLista(lista1, lista2):
  saida = []
  for ele in lista1:
    if not ele in lista2:
      saida.append(ele)
  return saida

lista1 = [1,4,3,2,6,5,0,7]
lista2 = [6,7,0,2,3,4,1,5]
filho1 = lista1[:4] + lista2[4:]
print(lista1, lista2)
print(filho1)
filho1Sem = list(dict.fromkeys(filho1))
print(filho1Sem)
print(diferencaLista(range(8), filho1Sem))
