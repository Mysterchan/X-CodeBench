from collections import deque

def solve():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(input().strip())
    
    # For each (i, j) pair, find shortest palindromic path
    result = [[-1] * N for _ in range(N)]
    
    for start in range(N):
        for end in range(N):
            if start == end:
                result[start][end] = 0
                continue
            
            # BFS with state: (current_vertex, left_string, right_string, length)
            # left_string: unmatched chars from left
            # right_string: unmatched chars from right (stored in reverse)
            queue = deque([(start, "", "", 0)])
            visited = {(start, "", "")}
            found = False
            
            while queue and not found:
                curr, left, right, length = queue.popleft()
                
                # Try all outgoing edges
                for next_v in range(N):
                    if graph[curr][next_v] == '-':
                        continue
                    
                    c = graph[curr][next_v]
                    new_length = length + 1
                    
                    # Try matching with right side
                    if right and right[-1] == c:
                        new_left = left
                        new_right = right[:-1]
                    else:
                        new_left = left + c
                        new_right = right
                    
                    # Check if we reached target with palindrome
                    if next_v == end and new_left == new_right[::-1]:
                        result[start][end] = new_length
                        found = True
                        break
                    
                    state = (next_v, new_left, new_right)
                    if state not in visited and len(new_left) + len(new_right) <= 50:
                        visited.add(state)
                        queue.append((next_v, new_left, new_right, new_length))
                
                if found:
                    break
    
    for row in result:
        print(' '.join(map(str, row)))

solve()