def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        people = []
        for i in range(N):
            L, R = map(int, input().split())
            people.append((L, R, i))
        
        # Попробуем жадный подход с лексикографической минимизацией
        assigned = [0] * N
        used_seats = [False] * (N + 1)
        
        # Сортируем людей по времени прихода
        sorted_people = sorted(range(N), key=lambda i: people[i][0])
        
        for person_idx in sorted_people:
            L, R, orig_idx = people[person_idx]
            
            best_seat = -1
            min_dissatisfaction = float('inf')
            
            # Пробуем каждое доступное место
            for seat in range(1, N + 1):
                if used_seats[seat]:
                    continue
                
                # Вычисляем недовольство, если назначить этому человеку это место
                dissatisfaction = 0
                
                # Недовольство других людей
                for other_idx in range(N):
                    if assigned[other_idx] == 0:
                        continue
                    other_seat = assigned[other_idx]
                    if other_seat >= seat:
                        continue
                    
                    L_other, R_other, _ = people[other_idx]
                    
                    # Человек person_idx проходит через other_seat в моменты L и R
                    # Проверяем, находится ли это в интервале (L_other, R_other)
                    if L_other < L < R_other:
                        dissatisfaction += 1
                    if L_other < R < R_other:
                        dissatisfaction += 1
                
                # Недовольство текущего человека
                for other_idx in range(N):
                    if assigned[other_idx] == 0:
                        continue
                    other_seat = assigned[other_idx]
                    if other_seat >= seat:
                        continue
                    
                    L_other, R_other, _ = people[other_idx]
                    
                    # Другой человек проходит через seat в моменты L_other и R_other
                    # Проверяем, находится ли это в интервале (L, R)
                    if L < L_other < R:
                        dissatisfaction += 1
                    if L < R_other < R:
                        dissatisfaction += 1
                
                if dissatisfaction < min_dissatisfaction or (dissatisfaction == min_dissatisfaction and (best_seat == -1 or seat < best_seat)):
                    min_dissatisfaction = dissatisfaction
                    best_seat = seat
            
            assigned[person_idx] = best_seat
            used_seats[best_seat] = True
        
        print(' '.join(map(str, assigned)))

solve()