def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    
    # Создаем массив позиций: pos[value] = index
    pos = [0] * (N * K + 1)
    for i in range(N * K):
        pos[P[i]] = i
    
    # Строим граф циклов перестановки
    visited = [False] * (N * K)
    cycles = []
    
    for start in range(N * K):
        if visited[start]:
            continue
        
        cycle = []
        current = start
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            # Куда должен попасть элемент на позиции current
            target_value = current + 1  # позиция current должна содержать значение current+1
            current = pos[target_value]
        
        if len(cycle) > 1:
            cycles.append(cycle)
    
    total_score = 0
    
    # Для каждого цикла находим максимальное количество баллов
    for cycle in cycles:
        cycle_len = len(cycle)
        
        # Проверяем, можно ли разбить цикл на подциклы с расстоянием N
        # Группируем позиции по их остатку от деления на N
        groups = {}
        for idx in cycle:
            remainder = idx % N
            if remainder not in groups:
                groups[remainder] = []
            groups[remainder].append(idx)
        
        # Для каждой группы с одинаковым остатком можем получить баллы
        # Если в группе k элементов, нужно k-1 операций для их сортировки
        # и все они дают баллы (расстояние кратно N)
        group_score = 0
        for remainder, positions in groups.items():
            if len(positions) > 1:
                group_score += len(positions) - 1
        
        # Минимальное количество операций для цикла длины L: L-1
        # Но нам нужно учесть структуру групп
        min_ops = cycle_len - 1
        
        # Количество групп
        num_groups = len(groups)
        
        # Если все элементы цикла в одной группе (по mod N), 
        # то все операции дают баллы
        if num_groups == 1:
            total_score += cycle_len - 1
        else:
            # Оптимальная стратегия: минимизировать операции без баллов
            # Нужно min_ops операций, максимум group_score из них дают баллы
            # Нам нужно соединить num_groups компонент
            # Минимум нужно num_groups - 1 операций между разными группами
            # Остальные операции могут быть внутри групп (дают баллы)
            non_scoring_ops = num_groups - 1
            scoring_ops = min_ops - non_scoring_ops
            total_score += scoring_ops
    
    print(total_score)

solve()