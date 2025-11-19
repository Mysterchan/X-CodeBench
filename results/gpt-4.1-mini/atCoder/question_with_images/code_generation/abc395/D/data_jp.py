import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# pigeon[i]: current nest of pigeon i (1-based)
pigeon = list(range(N + 1))

# swap_flag[i]: 0 or 1, indicates if nest i is swapped with its partner
swap_flag = [0] * (N + 1)

for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        # 1 a b: move pigeon a to nest b
        _, a, b = op
        pigeon[a] = b
    elif op[0] == 2:
        # 2 a b: swap nests a and b
        _, a, b = op
        swap_flag[a] ^= 1
        swap_flag[b] ^= 1
    else:
        # 3 a: report current nest of pigeon a
        _, a = op
        c = pigeon[a]
        if swap_flag[c]:
            # find the other nest that c is swapped with
            # Since swap_flag[c] == 1, c is swapped with some nest
            # But we don't know which one directly.
            # However, from problem statement, swaps are always between two nests a,b
            # and swap_flag[a] and swap_flag[b] are toggled.
            # So if swap_flag[c] == 1, c is swapped with some nest d where swap_flag[d] == 1 and d != c.
            # But we don't have direct mapping from c to d.
            # To solve this, we can store pairs of swaps in a dictionary.
            # But that would be complicated and memory heavy.
            # Instead, we can store the partner nest for each nest that has been swapped odd times.
            # Let's maintain a dictionary to map swapped nests to their partners.

            # To implement this efficiently, we need to maintain a partner array.

            # So we need to change approach:
            # Maintain partner array: partner[i] = nest that i is swapped with if swap_flag[i] == 1, else i itself.

            # Let's implement this from the start.

            pass

# The above approach is incomplete because we cannot find the partner nest from swap_flag alone.

# Revised approach:

# Maintain an array partner where partner[i] = i initially.
# When we swap nests a and b, we swap partner[a] and partner[b].
# For each pigeon, its current nest is partner[pigeon[i]].

# For operation 1: move pigeon a to nest b => pigeon[a] = b
# For operation 2: swap nests a and b => swap partner[a] and partner[b]
# For operation 3: output partner[pigeon[a]]

partner = list(range(N + 1))

for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        _, a, b = op
        pigeon[a] = b
    elif op[0] == 2:
        _, a, b = op
        partner[a], partner[b] = partner[b], partner[a]
    else:
        _, a = op
        print(partner[pigeon[a]])