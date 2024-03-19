class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None

def inserir(lst, valor):
  aux = Lista(valor)
  aux.prox = lst
  return aux

#Verificar comprimento da lista
def list_comprimento(lst):
  atual = lst
  counter = 0
  while atual is not None:
    counter += 1
    atual = atual.prox
  return counter

lst = None
lst = inserir(lst, 1)
lst = inserir(lst, 5)
lst = inserir(lst, 8)
print(list_comprimento(lst))
