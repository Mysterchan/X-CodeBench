from collections import deque

Q = int(input())
snakes = deque()  # Each element is (length, head_position)
offset = 0  # Cumulative offset due to type 2 queries

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        # Type 1: Add snake with length l
        l = query[1]
        if not snakes:
            head_pos = 0
        else:
            last_length, last_head = snakes[-1]
            head_pos = last_head + last_length
        snakes.append((l, head_pos))
    
    elif query[0] == 2:
        # Type 2: Remove front snake
        removed_length, _ = snakes.popleft()
        offset += removed_length
    
    else:  # query[0] == 3
        # Type 3: Output head position of k-th snake
        k = query[1]
        length, head_pos = snakes[k - 1]
        print(head_pos - offset)