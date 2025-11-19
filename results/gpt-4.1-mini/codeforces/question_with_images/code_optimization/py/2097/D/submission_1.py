import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()
    t = input().strip()

    # Find the smallest odd divisor q of n
    q = n
    while q % 2 == 0:
        q //= 2

    # If q == n, then no splitting is possible, just check equality
    if q == n:
        print("Yes" if s == t else "No")
        return

    # Number of blocks of length q
    blocks = n // q

    # Count parity of ones in each block for s and t
    # We only need parity because operations are mod 2 linear
    s_parity = [0] * blocks
    t_parity = [0] * blocks

    for i in range(n):
        s_parity[i // q] ^= (s[i] == '1')
        t_parity[i // q] ^= (t[i] == '1')

    # Sort parities to compare vector spaces (basis sets)
    s_parity.sort()
    t_parity.sort()

    print("Yes" if s_parity == t_parity else "No")

t = int(input())
for _ in range(t):
    solve()