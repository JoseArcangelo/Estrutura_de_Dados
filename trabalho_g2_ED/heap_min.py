class heapBinary:
    def __init__(self):
        self.heap_list = []
        self.count = 0

def ordena_prioridade(heap, index):
    while index != 0:
        parent = (index - 1) // 2

        if heap.heap_list[index] < heap.heap_list[parent]:
            heap.heap_list[index], heap.heap_list[parent] = heap.heap_list[parent], heap.heap_list[index]
            index = parent
        else:
            break

def inserir(heap_min, valor):
    heap_min.count += 1
    heap_min.heap_list.append(valor)
    ordena_prioridade(heap_min, heap_min.count - 1)
    return heap_min

def heapify_down(heap, index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap.count and heap.heap_list[left] < heap.heap_list[smallest]:
        smallest = left

    if right < heap.count and heap.heap_list[right] < heap.heap_list[smallest]:
        smallest = right

    if smallest != index:
        heap.heap_list[index], heap.heap_list[smallest] = heap.heap_list[smallest], heap.heap_list[index]
        heapify_down(heap, smallest)

def remover(heap_min):
    if heap_min.count == 0:
        return heap_min
    
    heap_min.heap_list[0], heap_min.heap_list[-1] = heap_min.heap_list[-1], heap_min.heap_list[0]
    min_value = heap_min.heap_list.pop()
    heap_min.count -= 1
    
    if heap_min.count > 0:
        heapify_down(heap_min, 0)
    
    return heap_min

def valor_minimo(heap_min):
    return heap_min.heap_list[0] if heap_min.count > 0 else None

heap_min = heapBinary()
heap_min = inserir(heap_min, 10)
heap_min = inserir(heap_min, 9)
heap_min = inserir(heap_min, 8)
heap_min = inserir(heap_min, 7)
heap_min = inserir(heap_min, 6)
heap_min = inserir(heap_min, 5)

print("Heap após inserções:", heap_min.heap_list)

heap_min = remover(heap_min)
print("Heap após remover o mínimo:", heap_min.heap_list)

menor_valor = valor_minimo(heap_min)
print("Menor valor atual:", menor_valor)
