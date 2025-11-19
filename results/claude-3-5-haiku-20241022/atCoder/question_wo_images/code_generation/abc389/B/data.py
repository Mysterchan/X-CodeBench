X = int(input())

N = 2
factorial = 2

while factorial < X:
    N += 1
    factorial *= N

print(N)