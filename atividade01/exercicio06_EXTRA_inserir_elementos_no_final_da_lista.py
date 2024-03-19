class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None

def inserir_valor(lst, valor):
  if lst is None:
    aux = Lista(valor)
    aux.prox = lst
    return aux
  
  atual = lst
  while atual.prox is not None:
    atual = atual.prox
  aux = Lista(valor)
  atual.prox = aux
  return lst

def lista_imprimi(lst):
  atual = lst
  
  while atual is not None:
    print(atual.info)

    atual = atual.prox

lst1 = None
lst1 = inserir_valor(lst1, 40)
lst1 = inserir_valor(lst1, 30)
lst1 = inserir_valor(lst1, 20)

lista_imprimi(lst1)
