import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

Q = int(data[0])
queries = data[1:]

queue = deque()
head_coordinates = []
offset = 0
results = []

for query in queries:
    parts = list(map(int, query.split()))
    if parts[0] == 1:
        l = parts[1]
        if not queue:
            head_coordinates.append(0)
        else:
            head_coordinates.append(head_coordinates[-1] + queue[-1])
        queue.append(l)
        
    elif parts[0] == 2:
        m = queue.popleft()
        offset += m
    
    elif parts[0] == 3:
        k = parts[1] - 1
        results.append(head_coordinates[k] - offset)

print('\n'.join(map(str, results)))