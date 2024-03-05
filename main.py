def matrizes(l,c):
    matriz = []
    for i in range(l):
        linha = []

        for j in range(c):
            linha.append(int(input(f'matriz({i})({j}): ')))
        matriz.append(linha)

    return matriz

def print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")

        print()

D = matrizes(2,2)
E = matrizes(2,2)

printar = D, E
print_matriz(printar)