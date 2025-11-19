X = int(input())

N = 1
fact = 1
while fact < X:
    N += 1
    fact *= N

print(N)