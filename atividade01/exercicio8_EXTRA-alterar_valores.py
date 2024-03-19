class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None

def inserir(lst, valor):
  aux = Lista(valor)
  aux.prox = lst
  return aux

def lista_altera(lst):
  atual = lst
  while atual is not None:
    atual.info -= atual.info * 2
    atual = atual.prox
  return lst
  
def lista_imprimi(lst):
  atual = lst
  while atual is not None:
    print(atual.info)
    atual = atual.prox

lst = None
lst = inserir(lst, 9)
lst = inserir(lst, 10)
lst = inserir(lst, 8)
lst = lista_altera(lst)
lista_imprimi(lst)
