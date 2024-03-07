def ex1_matriz(l,c):
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input(f'Matriz ({i})({j})= ')))
        matriz.append(linha)
    return matriz

#def ex1_print_matriz(matriz):
#    for i in range(len(matriz)):
#        for j in range(len(matriz[0])):
#            print(matriz[i][j], end=" ")
#        print()

def ex1_coluna_par(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j % 2 == 0:
                print(matriz[i][j], end=" ")
        print()

def ex1_print_diagonal(matriz):
    for i in range(len(matriz)):
        print(matriz[i][i])

A = ex1_matriz(4,2)
print(A)
coluna = ex1_coluna_par(A)
ex1_print_diagonal(coluna)