class Fila:
  def __init__(self, max):
      self.max = max
      self.n = 0
      self.ini = 0
      self.vet = []

def fila_cria(tam):
  f = Fila(tam)
  return f

def fila_cheia(f):
  return f.n == f.max

def fila_insere(f, v):
  if fila_cheia(f):
      print("Erro: capacidade da fila esgotou")
      return False
  fim = (f.ini + f.n) % f.max
  f.vet.insert(fim, v)
  f.n = f.n + 1

def fila_imprimi(f):
  contador = 0
  while contador != f.n:
    print(f.vet[contador])
    contador += 1

def fila_insere_inicio(f, v):
    if fila_cheia(f):
        print("Erro: capacidade da fila esgotou")
        return False
    prec = (f.ini - 1 + f.max) % f.max # insere elemento na posição precedente ao início
    f.vet.insert(prec, v)
    f.ini = prec # atualiza índice para novo início
    f.n = f.n + 1
    
def ordena_filas(f1, f2):
  contador = 0
  f3 = fila_cria(f1.n)

  while f1.n != contador:
    if f3.n == 0:
        fila_insere(f3, f1.vet[contador])
    else:
        contador2 = 0
        while contador2 != f3.n:
            if f1.vet[contador] < f3.vet[contador2]:
                f3.vet.insert(contador2, f1.vet[contador])
                f3.n += 1
                break 
            contador2 += 1

        if contador2 == f3.n:
            f3.vet.insert(contador2, f1.vet[contador])
            f3.n += 1
    contador += 1

  contador = 0
  while f2.n != contador:
    if f3.n == 0:
        fila_insere(f3, f2.vet[contador])
    else:
        contador2 = 0
        while contador2 != f3.n:
            if f2.vet[contador] < f3.vet[contador2]:
                f3.vet.insert(contador2, f2.vet[contador])
                f3.n += 1
                break 
            contador2 += 1

        if contador2 == f3.n:
            f3.vet.insert(contador2, f2.vet[contador])
            f3.n += 1
    contador += 1

  return f3

f1 = fila_cria(3)
f2 = fila_cria(4)

fila_insere(f1, 2)
fila_insere(f1, 4)
fila_insere(f1, 1)
print("F1")
fila_imprimi(f1)

fila_insere(f2, 7)
fila_insere(f2, 3)
fila_insere(f2, 9)
fila_insere(f2, 8)
print("\nF2")
fila_imprimi(f2)

f3 = ordena_filas(f1, f2)
print("\nF3")
fila_imprimi(f3)
