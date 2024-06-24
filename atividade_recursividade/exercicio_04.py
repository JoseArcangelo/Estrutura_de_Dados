# 4. Faça uma função recursiva que calcule e escreva o valor de S:

##OBS: Essa questão não sei se fiz certo.

def s(n, d): 
  if n == 1 and d == 1:
        return 1 / 1
  else:
      return (n / d) + s(n - 2, d - 1)


numerador = 99
denominador = 50

resultado = s(numerador, denominador)
print(f"O valor de S é: {resultado}")
