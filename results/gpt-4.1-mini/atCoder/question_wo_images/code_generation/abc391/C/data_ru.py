import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# pigeon_pos[i] = current nest of pigeon i (1-based)
pigeon_pos = [0] * (N + 1)
# nest_count[i] = number of pigeons in nest i (1-based)
nest_count = [0] * (N + 1)

# Initially, pigeon i in nest i
for i in range(1, N + 1):
    pigeon_pos[i] = i
    nest_count[i] = 1

# count of nests with more than one pigeon
multi_pigeon_nests = 0

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        # Move pigeon P to nest H
        P = int(query[1])
        H = int(query[2])
        old_nest = pigeon_pos[P]

        # Decrement count in old nest
        old_count = nest_count[old_nest]
        nest_count[old_nest] = old_count - 1
        if old_count == 2:
            # old nest was multi-pigeon, now single pigeon
            multi_pigeon_nests -= 1

        # Increment count in new nest
        new_count = nest_count[H]
        nest_count[H] = new_count + 1
        if new_count == 1:
            # new nest was single pigeon, now multi-pigeon
            multi_pigeon_nests += 1

        # Update pigeon position
        pigeon_pos[P] = H

    else:
        # Query type 2: output number of nests with more than one pigeon
        print(multi_pigeon_nests)