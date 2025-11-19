import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# pigeon_to_nest[i] = nest where pigeon i currently is
pigeon_to_nest = list(range(N + 1))  # 1-based indexing

# nest_mapping[i] = current label of nest i (after swaps)
nest_mapping = list(range(N + 1))  # 1-based indexing

for _ in range(Q):
    op = input().split()
    t = int(op[0])
    if t == 1:
        a, b = int(op[1]), int(op[2])
        # Move pigeon a to nest b
        pigeon_to_nest[a] = b
    elif t == 2:
        a, b = int(op[1]), int(op[2])
        # Swap nests a and b labels
        nest_mapping[a], nest_mapping[b] = nest_mapping[b], nest_mapping[a]
    else:
        a = int(op[1])
        # Output the label of the nest where pigeon a currently is
        print(nest_mapping[pigeon_to_nest[a]])