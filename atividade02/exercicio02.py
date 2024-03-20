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
    
    def separa_primeira_parte(lst, n):
        segunda_parte = None        
        atual = lst
        while True:
            segunda_parte = insere_lista(segunda_parte, atual.info)
            if atual.info == n:
                return segunda_parte
            atual = atual.prox
    
    # def separa_primeira_parte(lst, n):
    #     atual = lst
    #     while atual is not None:
    #         if atual.info == n:
    #             atual = atual.ante
    #             return atual
    #         atual = atual.prox

    atual = lst
    while atual is not None:
        if atual.info == n:
            break
        atual = atual.prox
    atual = atual.prox

    primeira_parte = separa_primeira_parte(lst, n)

    return atual, primeira_parte

lst = None
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)
lst = insere_lista(lst, 70)
lst = insere_lista(lst, 80)
lst = insere_lista(lst, 90)
lst = insere_lista(lst, 100)
lista_imprimi(lst)
lst2, lst = separa(lst, 80)

print("--Primeira PARTE--")
lista_imprimi(lst)
print("--SEGUNDA PARTE--")
lista_imprimi(lst2)
