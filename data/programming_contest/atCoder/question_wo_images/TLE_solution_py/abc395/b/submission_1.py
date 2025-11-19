n = int(input())
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append('#')
    matriz.append(linha)
    
def ponto(matriz, n, k):
    for i in range(k, n - k):
        for j in range(k, n - k):
            matriz[i][j] = '.'
    return matriz

def velha(matriz, n, k):
    for i in range(k, n - k):
        for j in range(k, n - k):
            matriz[i][j] = '#'
    return matriz

k = 0
if n % 2 == 0: 
    k = 0
    while True:
        velha(matriz, n, k)
        k += 1
        ponto(matriz, n, k)
        k += 1
        
        if k == n: break  
else: 
    k = 1
    while True:
        ponto(matriz, n, k)
        k += 1
        velha(matriz, n, k)
        k += 1
        
        if k == n: break

for i in range(n):
    linha = matriz[i]
    st = ''
    for j in range(n):
        st += linha[j]
    print(st)