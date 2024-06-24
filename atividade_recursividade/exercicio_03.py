# 3. Implemente uma função recursiva que, dados dois números inteiros x e n,
# calcula o valor de x elevado na n.

def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n - 1)

x = int(input("Informe o valor de x: "))
n = int(input("Informe o valor de n: "))
resultado = potencia(x, n)
print(f"{x} elevado na {n} é igual a: {resultado}")
