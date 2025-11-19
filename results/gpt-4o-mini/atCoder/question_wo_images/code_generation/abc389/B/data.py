import sys

def find_n_for_factorial(x):
    n = 1
    factorial = 1

    while factorial < x:
        n += 1
        factorial *= n

    return n if factorial == x else None

if __name__ == "__main__":
    x = int(sys.stdin.read().strip())
    result = find_n_for_factorial(x)
    print(result)