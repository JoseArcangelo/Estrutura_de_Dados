class Pilha:
	def __init__(self, max):
		self.max = max
		self.n = 0 		# vet[n] = primeira posição livre do vetor
		self.vet = []

def pilha_cria(n):
	p = Pilha(n) # pilha com até n elementos
	p.n = 0 # inicia com zero elementos
	return p

def pilha_push(p, v):
	if p.n == p.max:
		print("Push error: Capacidade da pilha estorou")
		return False
	# insere na prox. posição livre
	p.vet.insert(p.n, v)
	p.n = p.n + 1
	
def pilha_imprimi(p):
	contador = 0
	while contador != p.n:
		print(p.vet[contador])
		contador += 1
    
p = pilha_cria(5)
pilha_push(p, 1)
pilha_push(p, 2)
pilha_push(p, 3)
pilha_push(p, 4)
pilha_push(p, 5)

pilha_imprimi(p)
