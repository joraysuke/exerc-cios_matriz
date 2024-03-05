def Re2_matriz(l,c):
    matriz = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(int(input(f'Matriz ({i}) ({j}): ')))
        matriz.append(linha)
    return matriz

def Re2_print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()

H = Re2_matriz(2,2)
I = Re2_matriz(2,2)

Re2 = H, I
Re2_print_matriz(Re2)