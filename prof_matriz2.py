import random

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

def soma_matriz(matriz1,matriz2):
    C = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            linha.append(matriz1[i][j]+matriz2[i][j])
        C.append(linha)
    return C

def transposta(matriz):
    mt = []
    for i in range(len(matriz[0])):
        linha = []
        for j in range(len(matriz)):
            linha.append(matriz[j][i])
        mt.append(linha)
    return mt

def prod_interno(v,w):
    soma = 0
    for i in range(len(v)):
        soma += v[i]*w[i]
    return soma

def multiplica_matriz(A,B):
    C = []
    for i in range(len(A)):
        linha = []
        for j in range(len(B[0])):
            linha.append( prod_interno(A[i], transposta(B)[j]) )
        C.append(linha)
    return C


A = le_matriz(2,2)
printa_matriz(A)

B = le_matriz(2,2)
printa_matriz(B)

print()
D = transposta(B)
printa_matriz(D)

print()
MULT = multiplica_matriz(A,B)
printa_matriz(MULT)
# print()
# printa_matriz(D)
#printa_matriz(A)
#B = le_matriz(2,2)
#printa_matriz(B)
#
#SOMA = soma_matriz(A,B)
#printa_matriz(SOMA)
