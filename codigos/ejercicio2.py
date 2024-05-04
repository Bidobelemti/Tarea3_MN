from decimal import Decimal
import math as m

bandera = False
n = 1
max_error = 10**(-3)


while bandera == False:
    suma = 0
    for i in range(1,n):
        numerador = Decimal((-1)**(i+1)) * Decimal(1**(2*i-1))
        denominador = Decimal(2*i - 1)
        termino = (numerador / denominador)
        suma += termino
    error = abs(Decimal(m.pi) - 4 * suma)
    n += 1
    if error < max_error:
        bandera = True

print(f"Número de iteraciones: {n}")
print(f"Valor aproximado de pi: {4 * suma}")