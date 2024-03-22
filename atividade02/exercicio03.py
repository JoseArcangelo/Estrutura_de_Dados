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

def marge(lst1, lst2):
  atual_lst1 = lst1
  atual_lst2 = lst2
  lst3 = None

  while atual_lst1 is not None:
    lst3 = inserir_valor(lst3, atual_lst2.info)
    lst3 = inserir_valor(lst3, atual_lst1.info)

    atual_lst1 = atual_lst1.prox
    atual_lst2 = atual_lst2.prox

  return lst3

lst1 = None
lst1 = inserir_valor(lst1, 40)
lst1 = inserir_valor(lst1, 30)
lst1 = inserir_valor(lst1, 20)

lst2 = None
lst2 = inserir_valor(lst2, 70)
lst2 = inserir_valor(lst2, 60)
lst2 = inserir_valor(lst2, 50)

print("--Lista 1--")
lista_imprimi(lst1)

print("--Lista 2--")
lista_imprimi(lst2)

lst3 = marge(lst1, lst2)
print("--Lista com a intercalação de Lista1 e Lista 2--")
lista_imprimi(lst3)
