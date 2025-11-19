import sys
input = sys.stdin.readline
MOD = 998244353

# Precompute factorials and inverse factorials for combinations
MAX = 5000
fact = [1] * (MAX+1)
inv_fact = [1] * (MAX+1)
for i in range(2, MAX+1):
    fact[i] = fact[i-1] * i % MOD

def modinv(x):
    return pow(x, MOD-2, MOD)

inv_fact[MAX] = modinv(fact[MAX])
for i in range(MAX-1, 0, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, k):
    if k > n or k < 0:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    # The tree is rooted at 0, with nodes 0..n
    # p[i] is parent of node i+1 (1-based indexing for p)
    # We want to find the depth of each node to determine the path length from root to node d_i
    # Because the tree is rooted at 0, and p_i < i, we can compute depth easily

    depth = [0]*(n+1)
    for i in range(1, n+1):
        depth[i] = depth[p[i-1]] + 1

    # Each chip i can move on edges from root to d_i
    # The path length for chip i is depth[d_i]
    # The chip starts on edge (0,1) (depth 1)
    # The chip can move down to edges on path to d_i and back up, but cannot go beyond d_i

    # Key insight:
    # The chips can be rearranged only by swapping adjacent chips of the same color on the same edge.
    # Moving chips down and up edges can reorder chips of different colors only by moving them apart.
    # But chips of different colors cannot be swapped directly.
    #
    # The problem reduces to counting the number of permutations of chips on edge (0,1) after all moves,
    # respecting the constraints:
    # - The relative order of chips of the same color that cannot be swapped is fixed.
    # - Chips can only be permuted within their color blocks.
    #
    # However, the movement range restricts chips to edges on the path from root to d_i.
    # Since the tree is a chain from 0 to 1 to ... to n (because p_i < i and p_1=0),
    # the path from root to d_i is just nodes 0->1->...->d_i.
    #
    # The chips start on edge (0,1) (depth 1).
    # A chip with movement range depth[d_i] can move down to edge at depth d_i and back.
    #
    # The problem is equivalent to:
    # - We have chips with movement ranges (depth[d_i]).
    # - We want to count the number of permutations of chips on edge (0,1) after all moves,
    #   where chips can be reordered by swapping adjacent chips of the same color on the same edge,
    #   and by moving chips down and up edges within their movement range.
    #
    # The final order is constrained by the colors and movement ranges.
    #
    # The solution is to group chips by their movement range.
    # Chips with smaller movement range cannot be moved below chips with larger movement range on edge (0,1),
    # because they cannot go down to edges beyond their range and come back.
    #
    # So the chips are partitioned by their movement range.
    # The final order on edge (0,1) is a concatenation of groups sorted by movement range.
    #
    # Within each group (same movement range), chips can be permuted arbitrarily,
    # but only by swapping adjacent chips of the same color.
    #
    # Swapping adjacent chips of the same color means the order of chips of different colors inside the group is fixed,
    # but chips of the same color can be permuted arbitrarily.
    #
    # So for each group:
    # - Count how many black and white chips.
    # - The number of permutations inside the group is:
    #   (number of ways to interleave black and white chips preserving relative order of colors)
    #   * (permutations of black chips among themselves)
    #   * (permutations of white chips among themselves)
    #
    # The number of ways to interleave black and white chips preserving relative order of colors is:
    # comb(total_in_group, black_in_group)
    #
    # Multiply all groups' results to get the final answer.

    # Group chips by movement range
    from collections import defaultdict
    groups = defaultdict(list)
    for i in range(m):
        groups[depth[d[i]]] .append(i)

    # Sort groups by movement range (depth)
    sorted_keys = sorted(groups.keys())

    ans = 1
    for key in sorted_keys:
        group = groups[key]
        blacks = sum(1 for i in group if c[i] == 0)
        whites = len(group) - blacks
        # ways to interleave blacks and whites preserving relative order of colors
        ways_interleave = comb(blacks + whites, blacks)
        # permutations of blacks and whites among themselves
        ways_black = fact[blacks]
        ways_white = fact[whites]
        ans = ans * ways_interleave % MOD
        ans = ans * ways_black % MOD
        ans = ans * ways_white % MOD

    print(ans % MOD)