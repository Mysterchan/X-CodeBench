from collections import deque

def solve():
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(input().strip())
    
    # Для каждой пары (i, j) найдем кратчайший путь с палиндромной меткой
    result = [[-1] * n for _ in range(n)]
    
    for start in range(n):
        for end in range(n):
            if start == end:
                result[start][end] = 0
                continue
            
            # BFS с состоянием (текущая вершина, маска палиндрома, длина пути)
            # Маска палиндрома: битовая маска букв с нечетным количеством
            visited = {}
            queue = deque([(start, 0, 0)])  # (вершина, маска, длина)
            visited[(start, 0)] = 0
            
            min_length = -1
            
            while queue:
                curr, mask, length = queue.popleft()
                
                # Если достигли конечной вершины с валидным палиндромом
                if curr == end:
                    # Палиндром: не более одной буквы с нечетным количеством
                    if bin(mask).count('1') <= 1:
                        if min_length == -1 or length < min_length:
                            min_length = length
                        continue
                
                # Прекращаем, если уже нашли ответ и текущий путь не короче
                if min_length != -1 and length >= min_length:
                    continue
                
                # Перебираем все исходящие ребра
                for next_v in range(n):
                    edge = graph[curr][next_v]
                    if edge == '-':
                        continue
                    
                    # Обновляем маску (переключаем бит для этой буквы)
                    char_bit = 1 << (ord(edge) - ord('a'))
                    new_mask = mask ^ char_bit
                    new_length = length + 1
                    
                    # Ограничение на длину пути для избежания бесконечных циклов
                    if new_length > 2 * n:
                        continue
                    
                    state = (next_v, new_mask)
                    
                    # Проверяем, посещали ли мы это состояние с меньшей длиной
                    if state not in visited or visited[state] > new_length:
                        visited[state] = new_length
                        queue.append((next_v, new_mask, new_length))
            
            result[start][end] = min_length
    
    # Вывод результата
    for row in result:
        print(' '.join(map(str, row)))

solve()