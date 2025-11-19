import sys
input = sys.stdin.readline

Q = int(input())
heads = []
lengths = []
offset = 0
start = 0  # index of the first snake in the queue

for _ in range(Q):
    query = input().split()
    t = int(query[0])
    if t == 1:
        l = int(query[1])
        if start == len(heads):
            # queue empty
            head = 0
        else:
            # last snake's head + length
            head = heads[-1] + lengths[-1]
        heads.append(head)
        lengths.append(l)
    elif t == 2:
        # remove first snake
        m = lengths[start]
        offset += m
        start += 1
    else:
        k = int(query[1])
        idx = start + k - 1
        print(heads[idx] - offset)