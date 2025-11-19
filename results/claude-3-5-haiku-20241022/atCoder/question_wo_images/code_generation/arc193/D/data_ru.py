def solve():
    n = int(input())
    a = input().strip()
    b = input().strip()
    
    # Получаем позиции фигур и целевых позиций
    pieces = [i for i in range(n) if a[i] == '1']
    targets = [i for i in range(n) if b[i] == '1']
    
    # Если количество фигур меньше количества целей, невозможно
    if len(pieces) < len(targets):
        return -1
    
    m = len(targets)
    k = len(pieces)
    
    # Для каждого возможного сопоставления k фигур к m целям
    # нам нужно выбрать m фигур из k
    min_ops = float('inf')
    
    # Перебираем все возможные способы выбрать m фигур из k
    from itertools import combinations
    
    for selected_indices in combinations(range(k), m):
        selected_pieces = [pieces[i] for i in selected_indices]
        
        # Проверяем, можем ли мы сопоставить выбранные фигуры с целями
        # Оптимальное сопоставление: i-я выбранная фигура идет к i-й цели
        valid = True
        ops = 0
        
        # Для каждой пары (фигура, цель) вычисляем операции
        for i in range(m):
            piece_pos = selected_pieces[i]
            target_pos = targets[i]
            
            # Минимальное количество операций для перемещения фигуры
            # от piece_pos к target_pos - это просто расстояние
            ops += abs(piece_pos - target_pos)
        
        min_ops = min(min_ops, ops)
    
    return min_ops if min_ops != float('inf') else -1

t = int(input())
for _ in range(t):
    print(solve())