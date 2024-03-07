def Re3_matriz(l,c):
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input(f'matriz [{i}][{j}]= ')))
        matriz.append(linha)
    return matriz

def Re3_print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

J = Re3_matriz(3,3)

print(J)
Re3_print_matriz(J)