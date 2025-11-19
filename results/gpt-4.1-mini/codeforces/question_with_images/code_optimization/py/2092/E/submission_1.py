import sys
input = sys.stdin.readline

MOD = 10**9 + 7

def mod_pow(base, exp, mod):
    result = 1
    cur = base % mod
    while exp > 0:
        if exp & 1:
            result = (result * cur) % mod
        cur = (cur * cur) % mod
        exp >>= 1
    return result

def solve():
    n, m, k = map(int, input().split())
    # We will store constraints as parity relations on (x+y) and color
    # color(x,y) = color parity + (x+y) parity mod 2
    # We want to check if the given painted cells are consistent with this relation.
    # If consistent, answer = 2^(number of unpainted cells - 1)
    # else 0

    # We'll use a DSU-like approach on parity classes:
    # Actually, the problem reduces to checking if all given cells satisfy:
    # color_i ^ (x_i + y_i) mod 2 = constant (0 or 1)
    # If all equal, answer = 2^(unpainted_cells - 1)
    # else 0

    # Let's compute parity for each painted cell:
    # val_i = c_i ^ ((x_i + y_i) & 1)
    # All val_i must be equal for consistency.

    vals = []
    for _ in range(k):
        x, y, c = map(int, input().split())
        vals.append(c ^ ((x + y) & 1))

    # Check if all vals are equal
    if len(set(vals)) > 1:
        print(0)
        return

    unpainted = n * m - k
    # Number of ways = 2^(unpainted - 1) mod MOD
    # Because the parity condition fixes one bit of freedom.

    if unpainted == 0:
        # All cells painted, and consistent parity => only 1 way (the given painting)
        print(1)
        return

    ans = mod_pow(2, unpainted - 1, MOD)
    print(ans)

t = int(input())
for _ in range(t):
    solve()