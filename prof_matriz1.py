#l = 3 #qtde de linhas da matriz
#c = 3 #qtde de colunas da matriz

def le_matriz(l,c):
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input(f'matriz[{i}][{j}]= ')))
        matriz.append(linha)
    return matriz

def printa_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

#def printa_matriz(matriz):
#    for i in matriz:
#        for j in i:
#            print(j, end=" ")
#        print()

def printa_matriz_col_par(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if coluna%2==0:
                print(matriz[linha][coluna], end=" ")
        print()

def printa_matriz_linha_impar(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if linha%2!=0:
                print(matriz[linha][coluna], end=" ")
            else:
                print('-', end=" ")
        print()

def printa_diagonal(matriz):
    for i in range(len(matriz)):
        print(matriz[i][i])

A = le_matriz(3,3)
print(A)
#printa_matriz(A)
#printa_matriz_linha_impar(A)
printa_diagonal(A)