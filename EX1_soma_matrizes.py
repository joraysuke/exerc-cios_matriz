def ex1_matriz(l,c):
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input(f'Matriz ({i})({j})= ')))
        matriz.append(linha)
    return matriz

def ex1_print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

def ex1_soma_matriz(matriz1, matriz2):
    C = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            linha.append(matriz1[i][j]+matriz2[i][j])
        C.append(linha)
    return C

A = ex1_matriz(3,2)
B = ex1_matriz(3,2)
soma= ex1_soma_matriz(A,B)
ex1_print_matriz(soma)
