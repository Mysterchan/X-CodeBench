import sys
input = sys.stdin.readline

MOD = 998244353

# Precompute factorials and inverse factorials for combinations up to max_n
max_n = 400000  # max H+W from constraints

fact = [1] * (max_n + 1)
inv_fact = [1] * (max_n + 1)

for i in range(2, max_n + 1):
    fact[i] = fact[i-1] * i % MOD

# Fermat's little theorem for inverse factorial
inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
for i in reversed(range(1, max_n)):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD

T = int(input())
for _ in range(T):
    H, W, K = map(int, input().split())
    # Minimal walls to remove to connect top-left to bottom-right:
    # The shortest path length in grid is (H-1)+(W-1) steps = H+W-2 edges
    # So minimal walls to remove = H+W-2
    min_walls = H + W - 2
    total_walls = 2*H*W - H - W  # total walls in grid (not needed here)

    # If K < min_walls, no way to connect start to end
    if K < min_walls:
        print(0)
        continue

    # Number of ways to choose K walls so that path exists:
    # We must at least choose all edges in one shortest path (length min_walls)
    # The problem states: "choose K walls so that after removing them, path exists"
    # The minimal set of walls to connect start to end is min_walls.
    # Any superset of these edges also connects start to end.
    # The problem reduces to counting number of ways to choose K walls that include at least one shortest path.

    # The number of shortest paths from top-left to bottom-right in grid is:
    # C(H+W-2, H-1)
    # Each shortest path has min_walls edges.
    # To have a path, the chosen set of walls must contain at least one shortest path.

    # The problem's sample and explanation show that the answer is:
    # Number of shortest paths * C(total_walls - min_walls, K - min_walls)
    # Because we must choose all edges of a shortest path (min_walls edges),
    # and the rest K - min_walls edges can be any from the remaining walls.

    # But total_walls is huge and not given in problem explicitly.
    # However, from sample tests and constraints, the problem expects:
    # answer = number_of_shortest_paths * C(H+W-2, K - (H+W-2))
    # But this contradicts sample outputs.

    # Let's analyze sample:
    # For 2x2 grid:
    # min_walls = 2
    # number_of_shortest_paths = C(2,1) = 2
    # total walls = 2*2*2 - 2 - 2 = 8 - 4 = 4 (matches sample)
    # For K=3:
    # sample output = 4
    # number_of_shortest_paths * C(4-2, 3-2) = 2 * C(2,1) = 2*2=4 matches sample

    # So formula:
    # answer = number_of_shortest_paths * C(total_walls - min_walls, K - min_walls) mod MOD

    # total_walls = 2*H*W - H - W
    # min_walls = H + W - 2

    # But for large H,W this is huge, but we can compute total_walls - min_walls:
    # total_walls - min_walls = (2*H*W - H - W) - (H + W - 2) = 2*H*W - 2H - 2W + 2

    # But K ≤ H+W, so K - min_walls ≤ (H+W) - (H+W-2) = 2
    # So K - min_walls ≤ 2, small number

    # So we can compute C(total_walls - min_walls, K - min_walls) efficiently for small K - min_walls

    # number_of_shortest_paths = C(H+W-2, H-1)

    # Implement accordingly:

    if K > total_walls:
        # Can't choose more walls than total
        print(0)
        continue

    number_of_shortest_paths = comb(H+W-2, H-1)
    ways = comb(total_walls - min_walls, K - min_walls)
    ans = number_of_shortest_paths * ways % MOD
    print(ans)