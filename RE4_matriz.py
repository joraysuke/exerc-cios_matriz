def Re4_matriz(l,c):
    matriz =[]
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input(f'Matriz({i}) ({j}): ' )))
        matriz.append(linha)
    return matriz

def Re4_print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

I = Re4_matriz(2,2)
Re4_print_matriz(I)

