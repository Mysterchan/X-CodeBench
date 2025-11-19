def can_reach(N, M, A, B, bad_ranges):
    # Создаем список плохих интервалов
    bad = bad_ranges
    
    # BFS с оптимизацией
    from collections import deque
    
    # Если плохих интервалов нет, проверяем просто достижимость
    if M == 0:
        print("Yes")
        return
    
    # Проверяем, можем ли мы достичь N с позиции pos
    queue = deque([1])
    visited = {1}
    
    # Для больших N используем более умный подход
    # Проверяем критические позиции: начало и конец плохих интервалов
    critical_positions = set([1, N])
    for L, R in bad:
        if L - 1 > 0:
            critical_positions.add(L - 1)
        critical_positions.add(R + 1)
    
    # Добавляем позиции, достижимые одним прыжком от критических
    extra_positions = set()
    for pos in critical_positions:
        for i in range(A, B + 1):
            if pos + i <= N:
                extra_positions.add(pos + i)
            if pos - i > 0:
                extra_positions.add(pos - i)
    
    critical_positions.update(extra_positions)
    
    # Функция проверки, является ли позиция плохой
    def is_bad(pos):
        for L, R in bad:
            if L <= pos <= R:
                return True
        return False
    
    while queue:
        pos = queue.popleft()
        
        if pos == N:
            print("Yes")
            return
        
        # Пробуем все возможные прыжки
        for jump in range(A, B + 1):
            next_pos = pos + jump
            
            if next_pos > N:
                break
            
            if next_pos in visited:
                continue
            
            if is_bad(next_pos):
                continue
            
            # Оптимизация: если next_pos не критическая, пропускаем промежуточные
            if next_pos not in critical_positions and next_pos < N:
                # Проверяем, можем ли мы перепрыгнуть через эту область
                can_skip = False
                for future_jump in range(A, B + 1):
                    future_pos = next_pos + future_jump
                    if future_pos > N:
                        break
                    if future_pos in critical_positions or future_pos == N:
                        can_skip = True
                        break
                
                if not can_skip:
                    continue
            
            visited.add(next_pos)
            queue.append(next_pos)
    
    print("No")

# Чтение входных данных
N, M, A, B = map(int, input().split())
bad_ranges = []
for _ in range(M):
    L, R = map(int, input().split())
    bad_ranges.append((L, R))

can_reach(N, M, A, B, bad_ranges)