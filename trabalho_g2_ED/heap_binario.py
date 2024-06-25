#heap maximo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.pai = None

class MaxHeap:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

def inserir(heap, valor):
    novo_nodo = Nodo(valor)
    if heap.raiz is None:
        heap.raiz = novo_nodo
    else:
        inserir_na_posicao_correta(heap.raiz, novo_nodo)
        heapify_up(novo_nodo, heap)
    heap.tamanho += 1
    return heap

def inserir_na_posicao_correta(atual, novo_nodo):
    fila = [atual]
    while fila:
        atual = fila.pop(0)
        if not atual.esq:
            atual.esq = novo_nodo
            novo_nodo.pai = atual
            return
        else:
            fila.append(atual.esq)
        if not atual.dir:
            atual.dir = novo_nodo
            novo_nodo.pai = atual
            return
        else:
            fila.append(atual.dir)

def heapify_up(nodo, heap):
    while nodo.pai and nodo.valor > nodo.pai.valor:
        nodo.valor, nodo.pai.valor = nodo.pai.valor, nodo.valor
        nodo = nodo.pai

def extrair_maximo(heap):
    if not heap.raiz:
        return None
    
    valor_maximo = heap.raiz.valor
    if heap.tamanho == 1:
        heap.raiz = None
    else:
        ultimo_nodo = obter_ultimo_elemento(heap)
        heap.raiz.valor = ultimo_nodo.valor
        if ultimo_nodo.pai.esq == ultimo_nodo:
            ultimo_nodo.pai.esq = None
        else:
            ultimo_nodo.pai.dir = None
        heapify_down(heap.raiz, heap)
    heap.tamanho -= 1
    return valor_maximo

def obter_ultimo_elemento(heap):
    fila = [heap.raiz]
    ultimo_nodo = None
    while fila:
        ultimo_nodo = fila.pop(0)
        if ultimo_nodo.esq:
            fila.append(ultimo_nodo.esq)
        if ultimo_nodo.dir:
            fila.append(ultimo_nodo.dir)
    return ultimo_nodo

def heapify_down(nodo, heap):
    while nodo.esq or nodo.dir:
        if nodo.dir and nodo.dir.valor > nodo.esq.valor:
            filho_maior = nodo.dir
        else:
            filho_maior = nodo.esq
        if nodo.valor < filho_maior.valor:
            nodo.valor, filho_maior.valor = filho_maior.valor, nodo.valor
            nodo = filho_maior
        else:
            break

heap = MaxHeap()
inserir(heap, 10)
inserir(heap, 20)
inserir(heap, 5)

print(extrair_maximo(heap))  
print(extrair_maximo(heap))  
print(extrair_maximo(heap))


