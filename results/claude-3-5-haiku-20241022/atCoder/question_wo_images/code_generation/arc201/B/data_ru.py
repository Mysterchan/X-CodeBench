def solve():
    T = int(input())
    
    for _ in range(T):
        N, W = map(int, input().split())
        items = []
        for _ in range(N):
            X, Y = map(int, input().split())
            items.append((X, Y))
        
        # Группируем предметы по весу (X)
        groups = {}
        for X, Y in items:
            if X not in groups:
                groups[X] = []
            groups[X].append(Y)
        
        # Для каждой группы сортируем по убыванию ценности и берем префиксные суммы
        processed = []
        for X in sorted(groups.keys()):
            values = sorted(groups[X], reverse=True)
            weight = 1 << X  # 2^X
            prefix_sum = 0
            group_items = []
            for v in values:
                prefix_sum += v
                group_items.append((weight, prefix_sum))
            processed.append((X, group_items))
        
        # DP с использованием битов веса
        max_value = 0
        
        # Используем рекурсию с мемоизацией или перебор
        # Так как X_i < 60, можем представить выбор как битовую маску
        
        def dp(idx, remaining_weight):
            if idx == len(processed) or remaining_weight == 0:
                return 0
            
            X, group_items = processed[idx]
            weight = 1 << X
            
            # Не берем ничего из этой группы
            result = dp(idx + 1, remaining_weight)
            
            # Берем k предметов из этой группы
            for k, (total_weight, total_value) in enumerate(group_items, 1):
                if total_weight <= remaining_weight:
                    result = max(result, total_value + dp(idx + 1, remaining_weight - total_weight))
                else:
                    break
            
            return result
        
        # Оптимизация: используем итеративный подход
        # DP состояние: для каждого веса храним максимальную ценность
        # Но W слишком большое, поэтому используем другой подход
        
        # Представим W в двоичном виде и решим задачу
        dp_states = {0: 0}  # {использованный_вес: максимальная_ценность}
        
        for X, group_items in processed:
            new_states = {}
            for used_weight, value in dp_states.items():
                # Не берем предметы из этой группы
                if used_weight not in new_states or new_states[used_weight] < value:
                    new_states[used_weight] = value
                
                # Берем k предметов
                for k, (total_weight, total_value) in enumerate(group_items, 1):
                    new_weight = used_weight + total_weight
                    if new_weight <= W:
                        new_value = value + total_value
                        if new_weight not in new_states or new_states[new_weight] < new_value:
                            new_states[new_weight] = new_value
                    else:
                        break
            
            dp_states = new_states
        
        max_value = max(dp_states.values()) if dp_states else 0
        print(max_value)

solve()