class Lista:
    def __init__(self, info = None):
        self.info = info
        self.prox = None
        self.ante = None

def insere_lista(lst, valor):
  novo = Lista(valor)
  novo.prox = lst
  return novo

def lista_imprimi(lst):
  atual = lst
  while atual is not None:
    print(atual.info)
    atual = atual.prox

def separa(lst, n):
    

    atual = lst
    while atual is not None:
        if atual.info == n:
            break
        atual = atual.prox
    atual.prox = atual.prox

    

    return atual

lst = None
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)
lst = insere_lista(lst, 70)
lst = insere_lista(lst, 80)
lst = insere_lista(lst, 90)
lst = insere_lista(lst, 100)
lista_imprimi(lst)
lst2 = separa(lst, 80)


print("--Primeira PARTE--")

print("--SEGUNDA PARTE--")
lista_imprimi(lst2)
