from collections import deque

Q = int(input())
queue = deque()  # stores lengths of snakes
offset = 0  # cumulative offset to subtract from all positions
cumsum = 0  # cumulative sum of lengths (for absolute positioning)

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        # Add snake of length L to the end
        L = query[1]
        queue.append(L)
        cumsum += L
    elif query[0] == 2:
        # Remove snake from front
        removed_length = queue.popleft()
        offset += removed_length
    else:
        # Query k-th snake's head position
        k = query[1]
        # Calculate position of k-th snake
        pos = 0
        for i in range(k - 1):
            pos += queue[i]
        print(pos)