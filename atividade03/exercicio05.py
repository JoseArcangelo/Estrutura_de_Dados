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

def verificar(p, palavra):
	palavra_verificar = ""
	while p.n != 0:
		v = pilha_pop(p)
		palavra_verificar += v
	if palavra_verificar == palavra:
		return True
	return False

p = pilha_cria(5)
palavra = str(input("Informe a palavra: "))
for i in palavra:
	pilha_push(p, i)

print(verificar(p, palavra))
