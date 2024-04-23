class Fila:
  def __init__(self, max):
      self.max = max
      self.n = 0
      self.ini = 0
      self.vet = []

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

def combina_filas(f_res, f1, f2):
  contador = 0
  while contador != f1.max:
      fila_insere(f_res, f1.vet[contador])
      fila_insere(f_res, f2.vet[contador])
      contador += 1
    
f1 = Fila(3)
f2 = Fila(3)
f_res = Fila(f1.max + f2.max)
fila_insere(f1, 2.1)
fila_insere(f1, 4.5)
fila_insere(f1, 1.0)
print("F1")
fila_imprimi(f1)

fila_insere(f2, 7.2)
fila_insere(f2, 3.1)
fila_insere(f2, 9.8)
print("\nF2")
fila_imprimi(f2)

combina_filas(f_res, f1, f2)
print("\nF_res")
fila_imprimi(f_res)
