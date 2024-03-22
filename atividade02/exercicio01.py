class Lista:
    def __init__(self, info = None):
        self.info = info
        self.prox = None

def insere_lista(lst, valor):
  novo = Lista(valor)
  novo.prox = lst
  return novo

def retira_n(lst, valor):
  def verificar(lst, valor):
    atual = lst
    while atual is not None:
      if atual.info == valor:
        retira_n(lst, valor)
      atual = atual.prox
    return
  
  atual = lst
  # se for o primeiro elemento
  if atual.info == valor:
    lst = atual.prox
    atual = None
    
  while atual is not None:
    if atual.prox.info == valor:
      aux = atual.prox
      atual.prox = aux.prox
      aux = None
    atual = atual.prox
  
  ###Função que ira verificar se ha mais elementos(valor) na lista
  verificar(lst, valor)
  return lst
  
def lista_imprimi(lst):
  atual = lst
  while atual is not None:
    print(atual.info)
    atual = atual.prox

lst = None
lst = insere_lista(lst, 100)
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)
lst = insere_lista(lst, 70)
lst = insere_lista(lst, 80)
lst = insere_lista(lst, 100)
lst = insere_lista(lst, 90)
lst = insere_lista(lst, 100)
lista_imprimi(lst)
lst = retira_n(lst, 100)
print("\nREMOVEU")
lista_imprimi(lst)
