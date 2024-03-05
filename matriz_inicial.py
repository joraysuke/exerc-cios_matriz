def matriz_inicial(l,c):
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input(f'Matriz [{i}] [{j}]: ')))
        matriz.append(linha)

    return matriz

def print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")

        print()

A = matriz_inicial(2,2)
B = matriz_inicial(2,2)

inicial = A, B
print_matriz(inicial)