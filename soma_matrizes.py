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

def soma_matrizes(matriz, matriz2):
    C = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[0])):
            linha.append(matriz[i][j] + matriz2[i][j])
        C.append(linha)

    return C


A = matriz_inicial(2,2)
B = matriz_inicial(2,2)

inicial = soma_matrizes(A, B)
print_matriz(inicial)