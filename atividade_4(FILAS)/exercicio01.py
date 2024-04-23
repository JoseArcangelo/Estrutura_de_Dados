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

f = Fila(10)
fila_insere(f, 10)
fila_insere(f, 20)
fila_imprimi(f)
