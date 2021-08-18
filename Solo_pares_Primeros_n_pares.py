
# generar los N numeros primeros numeros pares a partir del 0
def contar_pares(n = 100):
    pares = []
    
    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        
        numero += 1 
    
    return pares
# solicita el numero de pares que necesita mediante entrada en caso de cumplirese mostrara la cantidad
# en este caso pares positivos, 
n = int(input('esciba el numero: '))

if n >= 0:
    pares = contar_pares(n)

    print(pares)
    print('Cantidad de pares:', len(pares))
else:
    print('escriba un numero')
