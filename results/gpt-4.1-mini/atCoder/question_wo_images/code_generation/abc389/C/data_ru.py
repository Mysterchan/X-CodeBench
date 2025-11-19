import sys
input = sys.stdin.readline

Q = int(input())

lengths = []
heads = []
offset = 0
start = 0  # index of the first snake in the queue

output = []

for _ in range(Q):
    query = input().split()
    t = int(query[0])
    if t == 1:
        l = int(query[1])
        if start == len(lengths):
            # queue empty
            head = 0
        else:
            # last snake index
            last_idx = len(lengths) - 1
            head = heads[last_idx] + lengths[last_idx]
        lengths.append(l)
        heads.append(head)
    elif t == 2:
        # remove first snake
        m = lengths[start]
        start += 1
        offset += m
    else:
        k = int(query[1])
        idx = start + k - 1
        # coordinate = stored head - offset
        coord = heads[idx] - offset
        output.append(str(coord))

print('\n'.join(output))