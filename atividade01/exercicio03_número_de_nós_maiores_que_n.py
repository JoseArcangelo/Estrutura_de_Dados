class Lista:
  def __init__(self, info = None):
    self.info = info
    self.prox = None

def insere_lista(lst, valor):
  aux = Lista(valor)
  aux.prox = lst
  return aux

def maiores(lst, n):
  atual = lst
  contador = 0
  while atual is not None:
    if atual.info > n:
      print(atual.info)
      contador += 1
    atual = atual.prox
  return contador

lst = None
lst = insere_lista(lst, 12)
lst = insere_lista(lst, 13)
lst = insere_lista(lst, 5)
lst = insere_lista(lst, 20)
n = int(input("Inoforme um valor: "))
print("--VALORES MAIORES QUE SEU VALOR INFORMADO--")
print(f"O total de nós maiores que {n} na lista encadeada é {maiores(lst, n)}")
