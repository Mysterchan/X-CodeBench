import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    output_lines = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        a_list = list(map(int, data[index:index+n]))
        index += n
        
        graph = defaultdict(list)
        for _ in range(n-1):
            u = int(data[index])
            v = int(data[index+1])
            index += 2
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)

        def dfs(node, par):
            visited[node] = True
            parent[node] = par
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    children[node].append(neighbor)
                    dfs(neighbor, node)

        dfs(1, 0)  # Start DFS from root node which is 1
        
        def compute_paths():
            size = [0] * (n + 1)
            base = [0] * (n + 1)
            count = [0] * (n + 1)
            
            def post_order(node):
                size[node] = 1
                base[node] = a_list[node - 1]
                for child in children[node]:
                    size[node] += post_order(child)
                    base[node] += base[child]
                
                if base[node] > 0:
                    flag = all(base[child] == 0 for child in children[node])
                    count[node] = 1 if flag else 0
                else:
                    count[node] = 0
                
                return size[node]

            paths_count = 0
            post_order(1)  # Fill out size and base arrays
            
            for node in range(1, n + 1):
                paths_count += count[node]

            return paths_count
        
        global_k = compute_paths()
        output_lines.append(str(global_k))

        q = int(data[index])
        index += 1

        inverted = [0] * (n + 1)

        for _ in range(q):
            v = int(data[index])
            index += 1

            stack = [v]
            while stack:
                u = stack.pop()
                inverted[u] ^= 1
                for child in children[u]:
                    if child != parent[u]:  # Avoid traversing backwards
                        stack.append(child)

            # Update dangling paths
            global_k = compute_paths()
            output_lines.append(str(global_k))

    sys.stdout.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    main()