import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    A = list(map(int, data[1:]))

    # Any two numbers always form a geometric progression.
    if n <= 2:
        print("Yes")
        return

    # Common ratio as a reduced fraction p/q = A[1]/A[0].
    p, q = A[1], A[0]
    g = math.gcd(p, q)
    p //= g
    q //= g

    # Check A[i] * q == A[i-1] * p for all i.
    for i in range(1, n):
        if A[i] * q != A[i - 1] * p:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()