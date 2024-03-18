class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None

#CIRAR UMA LISTA
def criar_lista():
  return None

#INSERIR ELEMENTO NA LISTA
def insere_lista(lst, valor):
  novo = Lista(valor)
  novo.prox = lst
  return novo

#IMPRIMIR CADA ELEMENTO DA LISTA EM ORDEM
def lista_imprimi(lst):
  atual = lst
  while atual is not None:
    print(atual.info)
    atual = atual.prox

#VERIFICAR SE A LISTA ESTA VAZIA
def lista_vazia(lst):
  return lst is None

#BUSCAR UM ELEMENTO
def busca(lst, valor):
  atual = lst
  while atual is not None:
    if atual.info == valor:
      return True
    atual = atual.prox
  return False

####REMOVER UM ELEMENTO
def remover_elemento(lst, valor):
  atual = lst
  # se for o primeiro elemento
  if atual.info == valor:
    lst = atual.prox
    atual = None
    return lst

  while atual is not None:
    if atual.prox.info == valor:
      aux = atual.prox
      atual.prox = aux.prox
      aux = None
      return lst

    atual = atual.prox
    
lst = criar_lista()
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)
lst = insere_lista(lst, 70)
lst = insere_lista(lst, 80)
lst = insere_lista(lst, 90)
lst = insere_lista(lst, 100)
lista_imprimi(lst)
print(lista_vazia(lst))
print(busca(lst, 70))

print("\nREMOVIDO")
lst = remover_elemento(lst, 100)
lista_imprimi(lst)
