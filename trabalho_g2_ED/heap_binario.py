# heap minimo
class heapBinary:
    def __init__(self):
        self.heap_list = [] 
        self.count = 0
        self.min = None

def ordena_prioridade(heap, tamanho):
    while tamanho != 0:
        parent = tamanho // 2 

        if heap.heap_list[tamanho] < heap.heap_list[parent]:
            heap.heap_list[tamanho], heap.heap_list[parent] = heap.heap_list[parent], heap.heap_list[tamanho]
        tamanho -= 1
    heap.min = heap.heap_list[0]

def inserir(heap_min, valor):
    heap_min.count += 1
    heap_min.heap_list.append(valor)
    if heap_min.count == 1:
        return heap_min
    ordena_prioridade(heap_min, heap_min.count - 1)
    return heap_min

def remover(heap_min):
    print(heap_min.heap_list)

    heap_min.heap_list[0], heap_min.heap_list[-1] = heap_min.heap_list[-1], heap_min.heap_list[0]
    
    print(heap_min.heap_list)
    heap_min.heap_list.pop(-1)
    
    print(heap_min.heap_list)
    
    heap_min.count -= 1
    ordena_prioridade(heap_min, heap_min.count - 1)
    return heap_min

def valor_minimo(heap_min):
    return heap_min.min

heap_min = heapBinary()
heap_min = inserir(heap_min,10)
heap_min = inserir(heap_min,9)
heap_min = inserir(heap_min,8)
heap_min = inserir(heap_min,7)
heap_min = inserir(heap_min,6)
heap_min = inserir(heap_min,5)

# heap_min = remover(heap_min)
print(heap_min.heap_list)
heap_min = remover(heap_min)

# heap_min = remover(heap_min)
print(heap_min.heap_list)

menor_valor = valor_minimo(heap_min)
print(menor_valor)


