# 6. Faça um programa que implemente a busca binária de um valor v em um
# vetor ordenado vet de tamanho 10. A função deve retornar a posição onde o
# elemento se encontra. Caso não exista, retornar falso.

def busca_binaria(vet, v, inf, sup):
    if inf > sup:
        return False  

    meio = (inf + sup) // 2

    if vet[meio] == v:
        return meio
    elif vet[meio] > v:
        return busca_binaria(vet, v, inf, meio - 1)
    else:
        return busca_binaria(vet, v, meio + 1, sup)  

l = []
for i in range(1, 11):
  l.append(i)

v = int(input("Informe o valor que deseja procurar: "))
resultado = busca_binaria(l, v, 0, len(l) - 1)
print(f"O valor {v} se enconrtra na posição: {resultado} do vetor.")
