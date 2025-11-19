from collections import deque

Q = int(input())
snakes = deque()  # (length, head_position)
offset = 0  # offset to subtract from all positions

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        l = query[1]
        if not snakes:
            head_pos = 0
        else:
            last_length, last_head = snakes[-1]
            head_pos = last_head + last_length
        snakes.append((l, head_pos))
    
    elif query[0] == 2:
        removed_length, _ = snakes.popleft()
        offset += removed_length
    
    else:  # query[0] == 3
        k = query[1]
        length, head_pos = snakes[k - 1]
        print(head_pos - offset)