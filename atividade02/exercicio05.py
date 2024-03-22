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

def igual(lst1, lst2):
  def tamanho(l):
    atual = l
    contador = 0
    while atual is not None:
      contador+=1
      atual = atual.prox
    return contador

  tamanho_lst1 = tamanho(lst1)
  tamanho_lst2 = tamanho(lst2)
  if tamanho_lst1 != tamanho_lst2:
    return False
  
  atual_lst1 = lst1
  atual_lst2 = lst2
  while atual_lst1 is not None:
    if atual_lst1.info != atual_lst2.info:
      return False
    atual_lst1 = atual_lst1.prox
    atual_lst2 = atual_lst2.prox

  return True

lst1 = None
lst1 = inserir_valor(lst1, 40)
lst1 = inserir_valor(lst1, 30)
lst1 = inserir_valor(lst1, 20)

lst2 = None
lst2 = inserir_valor(lst2, 40)
lst2 = inserir_valor(lst2, 30)
lst2 = inserir_valor(lst2, 20)

print("--Lista 1--")
lista_imprimi(lst1)

print("--Lista 2--")
lista_imprimi(lst2)

print(igual(lst1, lst2))
