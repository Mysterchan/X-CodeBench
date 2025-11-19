def dfs(node, parent, current_sum, a, graph, results):
    # 交互和を計算する
    current_sum += a[node - 1] if parent is None or (parent is not None and (node - parent) % 2 != 0) else -a[node - 1]
    
    # 現在のノードの脅威を設定
    results[node - 1] = current_sum
    
    # 子ノードに対してDFSを呼び出し
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, current_sum, a, graph, results)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results_list = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index].split()))
        index += 1
        
        graph = [[] for _ in range(n + 1)]
        
        for __ in range(n - 1):
            v, u = map(int, data[index].split())
            graph[v].append(u)
            graph[u].append(v)
            index += 1
            
        results = [0] * n
        dfs(1, None, 0, a, graph, results)
        
        results_list.append(" ".join(map(str, results)))
    
    print("\n".join(results_list))

if __name__ == "__main__":
    main()