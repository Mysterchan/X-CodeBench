import sys
input = sys.stdin.readline

MOD = 10**9 + 7

# Explanation:
# The board is a bipartite graph with cells colored by parity of (x+y).
# Edges connect cells of different parity.
# The parity of the number of edges with different colors depends on the parity of the XOR of colors on the two partitions.
#
# Let:
#   - color(i,j) = color of cell (i,j)
#   - parity(i,j) = (i+j) % 2
#
# The number of edges with different colors mod 2 equals:
#   sum over edges of (color(u) XOR color(v)) mod 2
#
# Since edges connect cells of different parity, this sum mod 2 equals:
#   (sum of colors on parity 0 cells) XOR (sum of colors on parity 1 cells)
#
# We want this XOR to be 0 (even number of edges with different colors).
#
# Given some fixed cells, we have constraints:
#   For each fixed cell (x,y,c):
#     If parity(x,y) = 0, then sum0 XOR sum1 = 0 => sum0 = sum1
#     If parity(x,y) = 1, then sum0 XOR sum1 = 0 => sum0 = sum1
#
# Actually, the condition is:
#   sum0 XOR sum1 = 0
#
# But fixed cells impose constraints on sum0 and sum1:
#   sum0 = XOR of all fixed colors on parity 0 cells
#   sum1 = XOR of all fixed colors on parity 1 cells
#
# For the XOR of edges to be even:
#   sum0 XOR sum1 = 0 => sum0 = sum1
#
# If sum0 != sum1, no solution.
#
# If sum0 == sum1, then the number of ways to paint the green cells is:
#   2^(number_of_green_cells - 1)
#
# Because the colors of one parity determine the other parity to satisfy sum0 = sum1.
#
# Number of green cells = total cells - k
# total cells = n*m
#
# Since n,m can be large, we use pow with modulo.
#
# Steps:
# 1. Compute XOR of fixed colors on parity 0 cells (sum0)
# 2. Compute XOR of fixed colors on parity 1 cells (sum1)
# 3. If sum0 != sum1 => 0
# 4. Else answer = 2^(n*m - k - 1) mod MOD

def mod_pow(base, exp, mod):
    result = 1
    cur = base % mod
    while exp > 0:
        if exp & 1:
            result = (result * cur) % mod
        cur = (cur * cur) % mod
        exp >>= 1
    return result

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    sum0 = 0
    sum1 = 0
    for __ in range(k):
        x, y, c = map(int, input().split())
        if (x + y) % 2 == 0:
            sum0 ^= c
        else:
            sum1 ^= c

    if sum0 != sum1:
        print(0)
        continue

    total_cells = n * m
    green_cells = total_cells - k
    if green_cells == 0:
        # All cells fixed and sum0 == sum1, only 1 way (the fixed coloring)
        print(1)
        continue

    # Number of ways = 2^(green_cells - 1) mod MOD
    ans = mod_pow(2, green_cells - 1, MOD)
    print(ans)