import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

Q = int(data[0])
queries = data[1:]

snake_queue = deque()
offset = 0
results = []

for query in queries:
    parts = list(map(int, query.split()))
    if parts[0] == 1:
        l = parts[1]
        head = (snake_queue[-1][0] + snake_queue[-1][1] if snake_queue else 0) + offset
        snake_queue.append((head, l))
    elif parts[0] == 2:
        length_to_remove = snake_queue.popleft()[1]
        offset += length_to_remove
    elif parts[0] == 3:
        k = parts[1] - 1
        head_position = snake_queue[k][0] - offset
        results.append(str(head_position))

print("\n".join(results))