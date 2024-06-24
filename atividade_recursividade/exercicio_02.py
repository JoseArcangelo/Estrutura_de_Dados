# 2. Faça uma função recursiva que imprima na tela os valores que estão
# dentro de um intervalo informado pelo usuário.

def imprimir(min, max):
  min += 1
  if min == max:
    return
  print(min)
  imprimir(min, max)

min = int(input("Informe o min: "))
max = int(input("Informe o máx: "))
imprimir(min, max)
