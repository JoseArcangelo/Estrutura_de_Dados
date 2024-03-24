##COLOQUEI UM CONTADOR NO lista_imprimi para nao ficar em um Loop infinito

class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None
    self.ante = None

def inserir_valor(lst, valor):
  aux = Lista(valor)
  aux.prox = lst
  return aux

def lista_imprimi(lst):
  atual = lst
  contador = 0
  while atual is not None:
    print(atual.info)
    atual = atual.prox
    if contador == 10:
      break
    contador += 1

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
      atual.prox = atual.prox.prox
      return lst
    atual = atual.prox
  
def inseri_valor_circular(lst, valor):
  atual = lst
  aux = atual
  while atual is not None:
    if atual.prox == aux:
      valor = Lista(valor)
      atual.prox = valor
      valor.prox = aux
      return lst
      
    atual = atual.prox

lst = None
lst = inserir_valor(lst, 10)
lst = inserir_valor(lst, 20)
lst = inserir_valor(lst, 30)

lst = circular(lst)

# lst =  remover_elemento(lst, 10)

lst = inseri_valor_circular(lst, 40)
lista_imprimi(lst)
