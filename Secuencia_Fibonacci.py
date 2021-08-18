# calculo de sucecion dependiendo si e mayor o menor
def SecF(n):
    if n < 2:
        return n
    else:
        return SecF(n-1) + SecF(n-2)
n = int(input('esciba el cantidad sucecion: '))
# muestra listado numerico segun cantidad de sucecion escrita en n 
for x in range(n):
    print(SecF(x))