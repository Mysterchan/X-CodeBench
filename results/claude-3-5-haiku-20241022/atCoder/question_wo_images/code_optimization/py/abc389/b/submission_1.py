X = int(input())

if X == 2:
    print(2)
else:
    N = 2
    current = 2
    while current < X:
        N += 1
        current *= N
    print(N)