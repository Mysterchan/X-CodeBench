def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Разделяем элементы на фиксированные и -1
    fixed_A = []
    fixed_B = []
    wild_A_count = 0
    wild_B_count = 0
    
    for i in range(n):
        if A[i] == -1:
            wild_A_count += 1
        else:
            fixed_A.append(A[i])
        
        if B[i] == -1:
            wild_B_count += 1
        else:
            fixed_B.append(B[i])
    
    # Проверяем все возможные суммы S
    possible_sums = set()
    
    # Суммы из фиксированных пар
    for i in range(n):
        if A[i] != -1 and B[i] != -1:
            possible_sums.add(A[i] + B[i])
    
    # Если нет фиксированных пар, можем выбрать любую сумму
    if not possible_sums:
        # Пробуем разные суммы на основе фиксированных элементов
        for a in fixed_A:
            for b in fixed_B:
                possible_sums.add(a + b)
        
        # Если все элементы -1, любая сумма >= 0 работает
        if not possible_sums:
            print("Yes")
            return
    
    # Для каждой возможной суммы проверяем, можно ли её достичь
    for S in possible_sums:
        if can_achieve_sum(n, A, B, S):
            print("Yes")
            return
    
    print("No")

def can_achieve_sum(n, A, B, S):
    # Собираем требования для каждой позиции
    needs_A = []  # значения A, которые нужны (когда B фиксирован)
    needs_B = []  # значения B, которые нужны (когда A фиксирован)
    wilds = 0     # позиции где оба -1
    
    for i in range(n):
        if A[i] == -1 and B[i] == -1:
            wilds += 1
        elif A[i] == -1:
            # Нужно A[i] = S - B[i]
            need = S - B[i]
            if need < 0:
                return False
            needs_A.append(need)
        elif B[i] == -1:
            # Нужно B[i] = S - A[i]
            need = S - A[i]
            if need < 0:
                return False
            needs_B.append(need)
        else:
            # Оба фиксированы
            if A[i] + B[i] != S:
                return False
    
    # Собираем доступные значения A (не включая те, что уже использованы в фикс. парах)
    available_A = []
    for i in range(n):
        if A[i] != -1 and B[i] == -1:
            available_A.append(A[i])
    
    # Проверяем, можем ли мы удовлетворить needs_A из available_A
    from collections import Counter
    avail_count = Counter(available_A)
    need_count = Counter(needs_A)
    
    # Проверяем каждое требуемое значение
    for val, cnt in need_count.items():
        if avail_count[val] < cnt:
            return False
        avail_count[val] -= cnt
    
    # Оставшиеся available_A должны быть размещены в wild позициях
    remaining_A = sum(avail_count.values())
    
    # Аналогично для B
    available_B = []
    for i in range(n):
        if B[i] != -1 and A[i] == -1:
            available_B.append(B[i])
    
    avail_B_count = Counter(available_B)
    need_B_count = Counter(needs_B)
    
    for val, cnt in need_B_count.items():
        if avail_B_count[val] < cnt:
            return False
        avail_B_count[val] -= cnt
    
    remaining_B = sum(avail_B_count.values())
    
    # Проверяем wild позиции
    # У нас есть wilds позиций и remaining_A + remaining_B элементов для размещения
    # Они должны совпадать
    if remaining_A + remaining_B == wilds:
        return True
    
    return False

solve()