import sys
input = sys.stdin.readline

Q = int(input())
queue = []
offset = 0
head_index = 0  # index of the first snake in the queue

for _ in range(Q):
    query = input().split()
    t = int(query[0])
    if t == 1:
        l = int(query[1])
        if head_index == len(queue):
            # queue empty
            head_pos = 0
        else:
            last_head, last_len = queue[-1]
            head_pos = last_head + last_len
        queue.append((head_pos + offset, l))
    elif t == 2:
        # remove front snake
        head_pos, length = queue[head_index]
        offset += length
        head_index += 1
    else:
        k = int(query[1])
        head_pos, _ = queue[head_index + k - 1]
        print(head_pos - offset)