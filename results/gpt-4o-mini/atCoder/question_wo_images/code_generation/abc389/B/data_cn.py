import sys

X = int(sys.stdin.read().strip())

def find_n_from_factorial(x):
    n = 1
    factorial = 1
    
    while factorial < x:
        n += 1
        factorial *= n
    
    return n

result = find_n_from_factorial(X)
print(result)