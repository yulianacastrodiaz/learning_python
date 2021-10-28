"""
Script en Python que calcula  y muestra la suma de dos matrices
cuadradas (misma cantidad de filas y columnas) generadas aleatoriamente.
Utilizar compresión de listas para generar las matrices de forma aleatoria.
"""

from random import randint

N = 3

print(f"Programa que calcula la suma de matrices de tamaño {N}x{N}")

m1 = [[randint(1, 50) for k in range(N)] for j in range(N)]
m2 = [[randint(1, 50) for k in range(N)] for j in range(N)]
"""resultado = [[0] * N for i in range(N)]

for fila in range(N):
    print(fila, " soy fila")
    for columna in range(N):
        print(columna, " Soy columna")
        resultado[fila][columna] = m1[fila][columna] + m2[fila][columna]
"""
resultado = [
    [m1[fila][columna] + m2[fila][columna] for columna in range(N)] for fila in range(N)
]
print(m1)
print(m2)
print(resultado)
