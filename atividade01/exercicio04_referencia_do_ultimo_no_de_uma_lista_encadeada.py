class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None

def inserir_valor(lst, valor):
  aux = Lista(valor)
  aux.prox = lst
  return aux

def ultimo(lst):
  atual = lst
  while True:
    if atual.prox == None:
      return atual.info
    atual = atual.prox

lst = None
lst = inserir_valor(lst, 20)
lst = inserir_valor(lst, 30)
lst = inserir_valor(lst, 40)
print(f"Referencia do ultimo nó da lista encadeada: {ultimo(lst)}")
