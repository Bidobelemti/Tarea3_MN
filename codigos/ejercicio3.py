from decimal import Decimal
import math as m

def app_pi():
    term1 = 16 * m.atan(1/5)
    term2 = 4 * m.atan(1/239)
    pi_approx = term1 - term2
    return pi_approx

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
    error = abs(Decimal(app_pi()) - 4 * suma)
    n += 1
    if error < max_error:
        bandera = True

print(f"Número de iteraciones: {n}")
print(f"Valor aproximado de pi: {4 * suma}")