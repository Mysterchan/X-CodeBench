import sys
input = sys.stdin.readline
MOD = 998244353

# Precompute factorials for up to 2*10^5 (max n)
MAXN = 2 * 10**5
fact = [1] * (MAXN + 1)
for i in range(2, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # After gravity sort, the final layout is determined by the sorted p
    # The final layout is a "staircase" of blocks with heights sorted(p)
    # The colors in each column after gravity are the colors of the blocks stacked
    # from bottom to top, which correspond to the colors of the p_i's sorted by p_i ascending.

    # Sort p and c by p ascending
    pc = sorted(zip(p, c), key=lambda x: x[0])
    # Extract colors in order of sorted p
    sorted_c = [x[1] for x in pc]

    # The problem asks: how many pairs (p', c') produce the same final layout?
    # The final layout is uniquely determined by the multiset of colors in each column.
    # Since p' is a permutation, the heights are distinct integers 1..n in some order.
    # The final layout after gravity is the same if and only if the colors in the sorted order
    # of p' are the same multiset of colors in each "height" position.

    # The key insight:
    # The final layout fixes the multiset of colors at each height.
    # The number of (p', c') pairs that produce the same layout is:
    # - The number of permutations p' that produce the same final layout (which is the number of permutations of p)
    #   because the final layout depends only on sorted p.
    # - For each group of equal p_i (which is impossible since p is a permutation, so all distinct),
    #   the colors can be permuted arbitrarily.
    # But since p is a permutation, all p_i are distinct, so the only freedom is permuting p.

    # However, the problem states that the original pair (p, c) is always counted.
    # The final layout fixes the colors in the sorted order of p.
    # So the number of pairs (p', c') is the number of permutations of p that keep the same color sequence after sorting by p'.
    # This means the colors must be the same sequence after sorting p'.

    # Since p is a permutation, the only way to get the same final layout is to permute p arbitrarily,
    # but the colors must be rearranged accordingly to keep the final layout the same.
    # So the number of pairs is the number of permutations of p that keep the color sequence the same after sorting by p'.

    # This is equivalent to counting the number of permutations of p that keep the color sequence sorted by p the same.
    # Since p is a permutation, the sorted order of p is fixed (1..n).
    # So the color sequence sorted by p is fixed.
    # The only way to get the same final layout is to permute p so that the color sequence sorted by p is the same.
    # This means the colors must be constant on the cycles of the permutation.

    # The problem reduces to counting the number of permutations p' such that
    # the color sequence sorted by p' is the same as sorted_c.

    # Since p is a permutation, the final layout is determined by sorted p.
    # The number of pairs (p', c') is the product of factorials of the counts of equal colors in sorted_c,
    # because we can permute the positions of equal colors arbitrarily.

    # So the answer is the product of factorials of the counts of each color in sorted_c.

    from collections import Counter
    color_counts = Counter(sorted_c)
    ans = 1
    for v in color_counts.values():
        ans = (ans * fact[v]) % MOD

    print(ans)