import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# nest_label[i]: the current label of the nest that was originally nest i
nest_label = list(range(N + 1))  # 1-based indexing

# pigeon_nest[i]: the original nest index where pigeon i currently is
pigeon_nest = list(range(N + 1))  # initially pigeon i in nest i

for _ in range(Q):
    op = input().split()
    t = int(op[0])
    if t == 1:
        a, b = int(op[1]), int(op[2])
        # Move pigeon a to nest b (original nest index b)
        pigeon_nest[a] = b
    elif t == 2:
        a, b = int(op[1]), int(op[2])
        # Swap the labels of nests a and b
        nest_label[a], nest_label[b] = nest_label[b], nest_label[a]
    else:
        a = int(op[1])
        # Report the label of the nest where pigeon a currently is
        print(nest_label[pigeon_nest[a]])