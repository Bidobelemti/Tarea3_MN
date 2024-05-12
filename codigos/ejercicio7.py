from decimal import Decimal

x = 0.25
ec_derecha = Decimal((1+2*x)/(1+x+x**(2)))
print(ec_derecha)
n = 1
bandera = False
suma = 0
while bandera == False:
    diferencia = 0
    num = Decimal(n*(1*x**(2**(n-1)-1)))-Decimal((2*x**(2**(n)-1)))
    den = Decimal(1-x**(2**(n-1))+x**(2**(n)))
    termino = num / den
    suma += termino
    diferencia = abs(ec_derecha-suma)
    n += 1
    if diferencia < 1e-6:
        bandera = True
print(suma)