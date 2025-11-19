import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

Q = int(data[0])
queries = data[1:]

snake_queue = deque()
current_offset = 0
outputs = []

for query in queries:
    parts = list(map(int, query.split()))
    if parts[0] == 1:  # Type 1: Add a snake
        l = parts[1]
        if not snake_queue:
            head_position = 0
        else:
            head_position = snake_queue[-1][0] + snake_queue[-1][1]
        snake_queue.append((head_position, l))
    
    elif parts[0] == 2:  # Type 2: Remove the front snake
        removed_length = snake_queue[0][1]
        current_offset += removed_length
        snake_queue.popleft()

    elif parts[0] == 3:  # Type 3: Query the head position
        k = parts[1] - 1  # zero-based index
        head_position = snake_queue[k][0] - current_offset
        outputs.append(head_position)

sys.stdout.write('\n'.join(map(str, outputs)) + '\n')