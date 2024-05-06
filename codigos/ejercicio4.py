def suma_producto(a, b):
  n = len(a)
  suma = 0
  contador_sumas = 0
  contador_multiplicaciones = 0

  for i in range(1, n + 1):
    for j in range(1, i + 1):
      contador_multiplicaciones += 1
      producto = a[i - 1] * b[j - 1]
      contador_sumas += 1
      suma += producto

  return suma, contador_sumas, contador_multiplicaciones

a = [1, 2, 3, 10, 12]
b = [2, 3, 4, 5,4,2,3]
suma, cant_sumas, cant_multiplicaciones = suma_producto(a, b)
print(f"Suma: {suma}")
print(f"Cantidad de sumas: {cant_sumas}")
print(f"Cantidad de multiplicaciones: {cant_multiplicaciones}")
