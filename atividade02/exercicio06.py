class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None

def inserir_valor(lst, valor):
  aux = Lista(valor)
  aux.prox = lst
  return aux

def lista_imprimi(lst):
  atual = lst
  
  while atual is not None:
    print(atual.info)
    atual = atual.prox

def copia(lst):
  atual = lst
  lst_copia = None
  l_auxiliar = []
  while atual is not None:
    l_auxiliar.insert(0, atual.info)
    atual = atual.prox
  
  for i in range(len(l_auxiliar)):
    lst_copia = inserir_valor(lst_copia, l_auxiliar[i])
  return lst_copia
    
lst = None
lst = inserir_valor(lst, 40)
lst = inserir_valor(lst, 30)
lst = inserir_valor(lst, 20)
lista_imprimi(lst)

lst_copia = copia(lst)
print("\n--LISTA COPIA--")
lista_imprimi(lst_copia)
