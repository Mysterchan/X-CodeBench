from collections import deque

Q = int(input())
queue = deque()  # Each element is (head_position, length)
offset = 0  # Cumulative length of removed snakes

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        # Type 1: Add snake
        l = query[1]
        if not queue:
            head_pos = 0
        else:
            last_head, last_length = queue[-1]
            head_pos = last_head + last_length
        queue.append((head_pos, l))
    
    elif query[0] == 2:
        # Type 2: Remove front snake
        head_pos, length = queue.popleft()
        offset += length
    
    else:  # query[0] == 3
        # Type 3: Query k-th snake
        k = query[1]
        head_pos, length = queue[k - 1]
        print(head_pos - offset)