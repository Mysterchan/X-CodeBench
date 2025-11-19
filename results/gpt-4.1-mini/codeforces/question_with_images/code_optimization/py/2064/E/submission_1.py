import sys
input = sys.stdin.readline
mod = 998244353

# Precompute factorials and inverse factorials for up to 2*10^5
MAX = 2 * 10**5 + 10
fact = [1] * (MAX)
inv_fact = [1] * (MAX)

def modinv(a, m=mod):
    return pow(a, m-2, m)

for i in range(2, MAX):
    fact[i] = fact[i-1] * i % mod
inv_fact[MAX-1] = modinv(fact[MAX-1])
for i in range(MAX-2, 0, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % mod

def nCr(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % mod * inv_fact[n-r] % mod

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # After gravity sort, the final layout is a staircase of heights 1..n
    # The final layout is sorted by p_i ascending, so p' must be sorted ascending: p' = [1..n]
    # The colors in each column correspond to the colors of the blocks stacked in that column.
    # The problem reduces to counting the number of ways to permute the colors c such that
    # the final layout is the same.

    # The final layout is formed by stacking columns of heights 1..n.
    # The color sequence in the final layout is:
    # For column j (1-based), the colors are the colors of the blocks from rows n-j+1 to n in that column.
    # But since p' is sorted ascending, the final layout is fixed:
    # The bottom row has color c_i where p_i = n (the largest p_i)
    # The row above has colors corresponding to p_i = n-1, etc.

    # So the final layout colors can be represented as a list of length n:
    # final_colors[i] = color of block at row i in the final layout (from top to bottom)
    # This is the color of the block with p_i = i+1 in the original array.

    # Let's build an array pos_of_p: pos_of_p[x] = index i where p[i] = x
    pos_of_p = [0]*(n+1)
    for i in range(n):
        pos_of_p[p[i]] = i

    # final_colors[i] = c[pos_of_p[i+1]]
    final_colors = [c[pos_of_p[i+1]] for i in range(n)]

    # The problem reduces to counting the number of permutations p' and arrays c' that produce the same final layout.
    # Since p' must be a permutation of 1..n, and the final layout is fixed,
    # the only freedom is to permute the colors within blocks of equal height.

    # But since p is a permutation, all p_i are distinct, so all heights are distinct.
    # So the only way to get the same final layout is to permute the colors of blocks with the same height.
    # Since all heights are distinct, the only way is to permute colors of blocks with the same height = 1 element each.

    # However, the problem states that the final layout is formed by stacking columns of heights 1..n,
    # and the colors in each column are the colors of the blocks stacked in that column.

    # The key insight is that the final layout is a matrix with columns 1..n, where column j has height j,
    # and the colors in column j are the colors of the blocks with p_i >= j.

    # So for each height h from 1 to n, the blocks with p_i >= h form the column h.
    # The colors in column h are the colors of blocks with p_i >= h.

    # Let's group blocks by their p_i values:
    # For each height h, the set of blocks with p_i = h is exactly one block (since p is a permutation).
    # So the colors in column h are the colors of blocks with p_i >= h.

    # The final layout colors in column h from bottom to top are c_i where p_i >= h,
    # sorted by p_i ascending (since columns are stacked from bottom to top).

    # The problem reduces to counting the number of permutations of p and c that produce the same final layout,
    # which is equivalent to counting the number of ways to permute the colors within blocks of the same height.

    # Since all p_i are distinct, the only freedom is permuting colors of blocks with the same height,
    # but each height corresponds to exactly one block, so no permutations possible.

    # However, the problem's sample input 2 shows that if all colors are the same, the answer is n! (all permutations of p).

    # So the answer is:
    # - If all colors in final_colors are the same, answer = n! (all permutations of p)
    # - Else, answer = 1 (only the original pair (p,c))

    # Check if all colors in final_colors are equal
    first_color = final_colors[0]
    if all(color == first_color for color in final_colors):
        print(fact[n] % mod)
    else:
        print(1)