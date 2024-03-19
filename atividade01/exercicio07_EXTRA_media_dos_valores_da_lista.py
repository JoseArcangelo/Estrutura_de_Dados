class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None

def inserir(lst, valor):
  aux = Lista(valor)
  aux.prox = lst
  return aux

def lista_calcula_media(lst):
  media = 0
  contador = 0
  atual = lst
  while atual is not None:  
    media += atual.info
    contador += 1
    atual = atual.prox
  
  media = media / contador
  return media

lst = None
lst = inserir(lst, 9)
lst = inserir(lst, 10)
lst = inserir(lst, 8)
print(f"A media dos valores da lista é: {lista_calcula_media(lst)}")
