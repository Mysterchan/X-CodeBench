import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

Q = int(data[0])
queue = deque()
total_offset = 0
results = []

for i in range(1, Q + 1):
    query = list(map(int, data[i].split()))
    
    if query[0] == 1:
        length = query[1]
        head_position = (queue[-1][0] + queue[-1][1]) if queue else 0
        queue.append((head_position, length))
        
    elif query[0] == 2:
        head, length = queue.popleft()
        total_offset += length
        
    elif query[0] == 3:
        k = query[1] - 1
        head_position, _ = queue[k]
        results.append(head_position - total_offset)

print('\n'.join(map(str, results)))