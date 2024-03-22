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

def circular(lst):
  atual = lst
  aux = atual
  while atual is not None:
    if atual.prox == None:
      atual.prox = aux
      return lst
    atual = atual.prox

def remover_elemento(lst, valor):
  atual = lst
  while atual is not None:
    if atual.prox.info == valor:
      aux = atual
      atual.prox = atual.prox.prox
      aux = None
      return lst
    atual = atual.prox

lst = None
lst = inserir_valor(lst, 40)
lst = inserir_valor(lst, 30)
lst = inserir_valor(lst, 20)
lst = inserir_valor(lst, 1000)
lst = inserir_valor(lst, 820)
lst = circular(lst)

lst =  remover_elemento(lst, 40)
lst = inserir_valor(lst, 4129120)
# lista_imprimi(lst)
