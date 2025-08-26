# main.py

# Función de ordenamiento (Bubble Sort)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# Definimos una matriz 3x3 de ejemplo
matriz = [
    [9, 2, 7],
    [4, 6, 1],
    [8, 3, 5]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar (ejemplo: segunda fila, índice 1)
fila_a_ordenar = 1
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)