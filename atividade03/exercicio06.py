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
	
def pilha_pop(p):
	if p.n == 0:
		print("Pop error: pilha vazia!")
		return False
	v = p.vet[p.n - 1]
	p.n = p.n - 1
	return v

def concatena_pilhas(p1, p2):
	l_aux = []
	while p2.n != 0:
		v = pilha_pop(p2)
		l_aux.insert(0, v)

	for i in l_aux:
		pilha_push(p1, i)

p1 =  pilha_cria(10)
p2 = pilha_cria(10)
pilha_push(p1, 1.0)
pilha_push(p1, 4.5)
pilha_push(p1, 2.1)

pilha_push(p2, 9.8)
pilha_push(p2, 3.1)
pilha_push(p2, 7.2)

concatena_pilhas(p1, p2)
print(p1.vet[p1.n - 1])
