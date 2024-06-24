# 5. Considere um sistema numérico que não tenha a operação de adição
# implementada e que você disponha somente dos operadores (funções)
# sucessor e predecessor. Então, pede-se para escrever uma função recursiva
# que calcule a soma de dois números x e y através desses dois operadores:
# sucessor e predecessor.

def calcula_soma(x, y):
    if y == 0:
        return x
    else:
        return calcula_soma(x + 1, y - 1)

# Testando a função soma
x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))
resultado = calcula_soma(x, y)
print(f"A soma de {x} e {y} é: {resultado}")
