from sys import stdin, stdout
from collections import defaultdict, deque

input = stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1
output = []

for _ in range(t):
    n, m, q = map(int, data[index].split())
    index += 1
    
    # Initialize graph and color state
    graph = defaultdict(list)
    color = [0] * (n + 1)  # 0=blue, 1=red

    # Read edges
    for _ in range(m):
        u, v = map(int, data[index].split())
        graph[u].append(v)
        index += 1

    # Prepare to answer queries
    queries = []
    
    for _ in range(q):
        x, u = map(int, data[index].split())
        queries.append((x, u))
        index += 1

    # Function to determine if Cry wins starting from node u
    def cry_wins(start):
        if color[start] == 1:  # If the starting node is red
            return False
        if not graph[start]:  # No outgoing edges
            return True
        
        winning_states = [False] * (n + 1)
        
        # Topological sort to calculate the win states
        indegree = [0] * (n + 1)
        for u in graph:
            for v in graph[u]:
                indegree[v] += 1

        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            if color[node] == 1:  # Red node
                winning_states[node] = False
            else:
                # Check if all outgoing edges lead to winning states for River
                all_to_river = True
                for next_node in graph[node]:
                    if not winning_states[next_node]:  # If there's a path leading to Cry winning
                        all_to_river = False
                        break
                winning_states[node] = not all_to_river
            
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        
        return winning_states[start]

    for x, u in queries:
        if x == 1:  # Update color
            color[u] = 1  # Make it red
        else:  # Check if Cry wins from node u
            output.append("YES" if cry_wins(u) else "NO")

stdout.write("\n".join(output) + "\n")