def solve():
    N, M = map(int, input().split())
    
    # Читаем черные ребра
    black_edges = set()
    for _ in range(M):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        black_edges.add((u, v))
    
    # Общее количество ребер в полном графе
    total_edges = N * (N - 1) // 2
    
    # Ключевое наблюдение: операция переворачивает 3 ребра треугольника
    # Это означает, что четность количества черных ребер меняется на 1 или -1 (mod 2)
    # при каждой операции (переворачиваем 3 ребра, изменение четности на 1)
    
    # Текущее количество черных ребер
    current_black = M
    
    # Максимум возможных черных ребер зависит от четности
    # Если текущая четность совпадает с четностью total_edges, 
    # можем достичь total_edges
    # Иначе можем достичь total_edges - 1
    
    if current_black % 2 == total_edges % 2:
        max_black = total_edges
    else:
        max_black = total_edges - 1
    
    print(max_black)

solve()