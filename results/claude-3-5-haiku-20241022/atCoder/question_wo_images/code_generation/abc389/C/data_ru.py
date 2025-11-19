from collections import deque

Q = int(input())
queue = deque()
offset = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        l = query[1]
        if len(queue) == 0:
            queue.append((0, l))
        else:
            last_head, last_length = queue[-1]
            new_head = last_head + last_length
            queue.append((new_head, l))
    
    elif query[0] == 2:
        head, length = queue.popleft()
        offset += length
    
    else:  # query[0] == 3
        k = query[1]
        head, length = queue[k - 1]
        print(head - offset)