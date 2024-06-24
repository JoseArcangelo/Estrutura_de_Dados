# 1. Implemente uma função recursiva produto(n) que calcula o produto dos n
# primeiros números inteiros positivos.
def produto(n):
  if n == 1:
    return 1
  return n * produto(n - 1)

n = int(input("Informe um número: "))
resultado = produto(n)
print(" o produto dos n primeiros números inteiros positivos é: ", resultado)
