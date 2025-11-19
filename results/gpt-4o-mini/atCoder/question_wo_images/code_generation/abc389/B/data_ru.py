import sys

def find_factorial(N):
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    return factorial

X = int(sys.stdin.read().strip())
N = 2

while True:
    if find_factorial(N) == X:
        print(N)
        break
    N += 1