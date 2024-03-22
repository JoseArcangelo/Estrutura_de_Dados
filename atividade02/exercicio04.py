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

def inverte(lst):
  atual = lst
  lst2 = None
  while atual is not None:
    lst2 = inserir_valor(lst2, atual.info)
    atual = atual.prox
  return lst2

lst = None
lst = inserir_valor(lst, 40)
lst = inserir_valor(lst, 30)
lst = inserir_valor(lst, 20)
lista_imprimi(lst)

print("\n--Inverteu--")
lst = inverte(lst)
lista_imprimi(lst)
