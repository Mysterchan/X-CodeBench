import sys

MOD = 998244353

h, w = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
q, x, y = map(int, sys.stdin.readline().split())
x -= 1
y -= 1

# Precompute factors
def precompute_factorials(max_n, mod):
    fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i-1] * i % mod
    return fact

def mod_inv(a, p):
    return pow(a, p - 2, p)

fact = precompute_factorials(h + w, MOD)

# Compute number of paths from top-left to (h, w)
def count_paths(h, w):
    return fact[h + w - 2] * mod_inv(fact[h - 1], MOD) % MOD * mod_inv(fact[w - 1], MOD) % MOD

# Path counts at the start
ans = 0
def calculate_paths():
    paths = 0
    # Iterate through grid and find all products
    for i in range(h):
        for j in range(w):
            val = grid[i][j]
            if val > 0:
                paths += val * count_paths(i + 1, j + 1) % MOD
                paths %= MOD
    return paths

ans = calculate_paths()

# Update grid and paths for each query
output = []
for _ in range(q):
    direction, new_value = sys.stdin.readline().split()
    new_value = int(new_value)

    # Move in the specified direction
    if direction == 'U':
        x -= 1
    elif direction == 'D':
        x += 1
    elif direction == 'L':
        y -= 1
    elif direction == 'R':
        y += 1

    # Update grid cell A[x][y]
    old_value = grid[x][y]
    grid[x][y] = new_value

    # Update the answer
    prod_paths = count_paths(h - x, w - y) * count_paths(x + 1, y + 1) % MOD
    ans = (ans - old_value * prod_paths % MOD + new_value * prod_paths % MOD) % MOD
    output.append(ans)

print('\n'.join(map(str, output)))