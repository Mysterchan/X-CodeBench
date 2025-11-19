from collections import deque

def solve():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(input().strip())
    
    # Build adjacency list
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] != '-':
                adj[i].append((j, graph[i][j]))
    
    # For each pair (i, j), find shortest palindrome path
    result = [[-1] * N for _ in range(N)]
    
    for start in range(N):
        for end in range(N):
            if start == end:
                result[start][end] = 0
                continue
            
            # BFS with state (front_node, back_node, front_string, back_string)
            # We build palindrome from both ends
            visited = {}
            queue = deque()
            
            # Initial state: start from 'start', work backwards from 'end'
            queue.append((start, end, "", ""))
            visited[(start, end, "", "")] = 0
            
            min_length = float('inf')
            
            while queue:
                front, back, front_str, back_str = queue.popleft()
                current_len = visited[(front, back, front_str, back_str)]
                
                if current_len >= min_length:
                    continue
                
                # Try extending from front
                for next_front, label in adj[front]:
                    new_front_str = front_str + label
                    
                    # Check if we can match with back
                    if next_front == back and new_front_str == back_str[::-1]:
                        min_length = min(min_length, current_len + 1)
                    
                    # Check if front_str matches beginning of reversed back_str
                    rev_back = back_str[::-1]
                    if len(new_front_str) <= len(rev_back):
                        if rev_back.startswith(new_front_str):
                            state = (next_front, back, new_front_str, back_str)
                            if state not in visited or visited[state] > current_len + 1:
                                visited[state] = current_len + 1
                                queue.append(state)
                    elif len(new_front_str) > len(rev_back):
                        if new_front_str.startswith(rev_back):
                            state = (next_front, back, new_front_str, back_str)
                            if state not in visited or visited[state] > current_len + 1:
                                visited[state] = current_len + 1
                                queue.append(state)
                
                # Try extending from back (going backwards)
                for prev_back, label in adj[back]:
                    new_back_str = label + back_str
                    
                    # Check if we can match with front
                    if front == prev_back and front_str == new_back_str[::-1]:
                        min_length = min(min_length, current_len + 1)
                    
                    # Check if back_str (reversed) matches beginning of front_str
                    rev_new_back = new_back_str[::-1]
                    if len(rev_new_back) <= len(front_str):
                        if front_str.startswith(rev_new_back):
                            state = (front, prev_back, front_str, new_back_str)
                            if state not in visited or visited[state] > current_len + 1:
                                visited[state] = current_len + 1
                                queue.append(state)
                    elif len(rev_new_back) > len(front_str):
                        if rev_new_back.startswith(front_str):
                            state = (front, prev_back, front_str, new_back_str)
                            if state not in visited or visited[state] > current_len + 1:
                                visited[state] = current_len + 1
                                queue.append(state)
            
            if min_length != float('inf'):
                result[start][end] = min_length
    
    for row in result:
        print(' '.join(map(str, row)))

solve()