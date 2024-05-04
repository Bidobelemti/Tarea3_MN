# codigo en base al pseudocodigo planteado
## a.
n = 10
suma  = 0
for x in range(1,n+1):
    suma += 1/(x**2)
    print(1,"/",(x**2), end=" + ")
print('\n')

## b.
for x in range(n,0,-1):
    suma += 1/(x**2)
    print(1,"/",(x**2), end=" + ")

