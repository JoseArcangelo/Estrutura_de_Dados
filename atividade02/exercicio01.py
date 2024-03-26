class Lista:
    def __init__(self, info = None):
        self.info = info
        self.prox = None

def insere_lista(lst, valor):
  novo = Lista(valor)
  novo.prox = lst
  return novo

def retira_n(lst, valor):
  def contar(lst, valor, contador):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            contador += 1
        atual = atual.prox
    return contador

  contador = 0
  contador = contar(lst, valor, contador)
  
  atual = lst
  # se for o primeiro elemento
  if atual.info == valor:
    lst = atual.prox
    atual = None
    if contador > 1:
        retira_n(lst, valor)
    return lst

  while atual is not None:
    if atual.prox.info == valor:
      aux = atual.prox
      atual.prox = aux.prox
      aux = None
      if contador > 1:
        retira_n(lst, valor)
      return lst
    atual = atual.prox

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
lst = retira_n(lst, 90)
print("REMOVEU")
lista_imprimi(lst)
print("\nREMOVEU")
lista_imprimi(lst)
