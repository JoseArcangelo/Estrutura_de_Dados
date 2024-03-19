class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None

def inserir_valor(lst, valor):
  aux = Lista(valor)
  aux.prox = lst
  return aux

def concatena(lst1, lst2):
    if lst1 is None:
        return lst2
    atual = lst1
    while atual.prox is not None:
      atual = atual.prox
    atual.prox = lst2
    return lst1

def lista_imprimi(lst):
  atual = lst
  
  while atual is not None:
    print(atual.info)

    atual = atual.prox

lst1 = None
lst1 = inserir_valor(lst1, 40)
lst1 = inserir_valor(lst1, 30)
lst1 = inserir_valor(lst1, 20)

lst2 = None
lst2 = inserir_valor(lst2, 70)
lst2 = inserir_valor(lst2, 60)
lst2 = inserir_valor(lst2, 50)

lst3 = concatena(lst1, lst2)
lista_imprimi(lst3)
