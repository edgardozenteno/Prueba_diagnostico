# solicitar el ingreso de n para sumar los impares desde 0
total = 0
n = int(input('ingrese numero: '))
lista_numeros = []
# condicionar bucle si el rango incluye impares
for i in range(0, n + 1):
    if i % 2 == 1:
      lista_numeros.append(i)
      total += i
# arrojar resultados mostrando lista de rango hasta n y suma de los impares contenidos
print(f'lista numeros de 0 a {n} es: {lista_numeros}')
print('la suma de los impares de 0 a {} es: {}' .format (n, total))

