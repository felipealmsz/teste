def pascal_triangle(n):
    tri = []
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1, i):
            row[j] = tri[i-1][j-1] + tri[i-1][j]
        tri.append(row)
    return tri

n = int(input("Digite um número inteiro: "))
triangulo = pascal_triangle(n)

for i in range(n):
    grau = str(i).rjust(2)
    print(f"Grau {grau} do polinômio:", end=' ')
    print(' '*(n-i), end='')
    for j in range(i+1):
        print('{0:5}'.format(triangulo[i][j]), end='')
    print()
    