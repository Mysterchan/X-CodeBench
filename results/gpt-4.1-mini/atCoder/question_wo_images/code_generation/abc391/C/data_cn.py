import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# pos[pigeon] = current hole of pigeon p
pos = list(range(N + 1))  # 1-based indexing

# count[h] = number of pigeons in hole h
count = [1] * (N + 1)
count[0] = 0  # unused

multi_count = 0  # number of holes with more than one pigeon

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        _, P, H = query
        P = int(P)
        H = int(H)
        old_h = pos[P]

        # Remove pigeon P from old hole
        old_c = count[old_h]
        count[old_h] = old_c - 1
        if old_c == 2:
            # old hole was multi, now single
            multi_count -= 1

        # Add pigeon P to new hole
        new_c = count[H]
        count[H] = new_c + 1
        if new_c == 1:
            # new hole was single, now multi
            multi_count += 1

        pos[P] = H

    else:
        # query type 2
        print(multi_count)