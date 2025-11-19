import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# nest_label[i] = current label of nest i (after swaps)
# Initially, nest i has label i
nest_label = list(range(N + 1))

# pigeon_nest[i] = the nest label where pigeon i currently is
# Initially, pigeon i is in nest i
pigeon_nest = list(range(N + 1))

for _ in range(Q):
    op = input().split()
    t = int(op[0])
    if t == 1:
        # Move pigeon a to nest b
        a, b = int(op[1]), int(op[2])
        pigeon_nest[a] = nest_label[b]
    elif t == 2:
        # Swap nests a and b (swap their labels)
        a, b = int(op[1]), int(op[2])
        nest_label[a], nest_label[b] = nest_label[b], nest_label[a]
    else:
        # Report the nest label of pigeon a
        a = int(op[1])
        print(pigeon_nest[a])