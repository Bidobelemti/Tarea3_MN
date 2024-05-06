a = [1,2,3,4,5,6,7,8,9,10]
suma = 0
for i in range(len(a)-1,-1,-1):
    suma += a[i]
    print(a[i], end=' ')
print('\n',suma)
