from collections import defaultdict, deque

def solve():
    n = int(input())
    if n == 1:
        print(-1)
        return
    
    graph = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    degree = {i: len(graph[i]) for i in range(1, n + 1)}
    
    # Функция для подсчета размера поддерева с ограничением степени
    def subtree_size(root, parent):
        if degree[root] > 4:
            return 0
        
        size = 1
        for neighbor in graph[root]:
            if neighbor != parent:
                child_size = subtree_size(neighbor, root)
                if child_size == 0:
                    return 0
                size += child_size
        
        return size
    
    max_alkane = -1
    
    # Проверяем каждую вершину степени >= 4 как центральную
    for center in range(1, n + 1):
        if degree[center] < 4:
            continue
        
        # Считаем размеры всех поддеревьев от центра
        subtrees = []
        for neighbor in graph[center]:
            size = subtree_size(neighbor, center)
            if size > 0:
                subtrees.append(size)
        
        # Если можем выбрать хотя бы 4 поддерева
        if len(subtrees) >= 4:
            subtrees.sort(reverse=True)
            # Берем 4 самых больших поддерева
            total = 1 + sum(subtrees[:4])
            max_alkane = max(max_alkane, total)
    
    print(max_alkane)

solve()