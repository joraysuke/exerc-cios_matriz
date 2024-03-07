def ex2_matriz(l,c):
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input(f'Matriz({i})({j})= ')))
        matriz.append(linha)
    return matriz

def ex2_print_matrizes(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

def ex2_soma_matrizes(matriz1,matriz2):
    C = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            linha.append(matriz1[i][j]+matriz2[i][j])
        C.append(linha)
    return C

A = ex2_matriz(3,2)
B = ex2_matriz(3,2)
soma = ex2_soma_matrizes(A,B)
ex2_print_matrizes(soma)



