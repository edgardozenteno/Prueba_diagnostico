# solicitar el ingreso de n para sumar los impares desde un minimo a maximo
total = 0
i = int(input('ingrese numero minimo: '))
fn = int(input('ingrese numero maximo: '))
# condicionar el rango que incluye impares
while i < fn:
    if i % 2 == 1:
        total += i
    i += 0 + 1

# arrojar resultados mostrando lista de rango  n-min a n-max
print('la suma de los impares es: ', total)