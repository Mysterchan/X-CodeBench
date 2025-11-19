def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Найдем первую подпоследовательность
    first_indices = []
    j = 0
    for i in range(N):
        if j < M and A[i] == B[j]:
            first_indices.append(i)
            j += 1
    
    # Если не нашли даже одну подпоследовательность
    if len(first_indices) < M:
        print("No")
        return
    
    # Найдем вторую подпоследовательность, отличную от первой
    second_indices = []
    j = 0
    for i in range(N):
        if j < M and A[i] == B[j]:
            # Пытаемся взять другой индекс, если возможно
            if i != first_indices[j]:
                second_indices.append(i)
                j += 1
            elif j > 0 or i < N - 1:
                # Проверим, можем ли мы отложить выбор
                # Ищем следующее вхождение B[j]
                found_later = False
                for k in range(i + 1, N):
                    if A[k] == B[j]:
                        found_later = True
                        break
                
                if found_later:
                    # Пропускаем текущий элемент
                    continue
                else:
                    # Вынуждены взять текущий
                    second_indices.append(i)
                    j += 1
            else:
                second_indices.append(i)
                j += 1
    
    # Более надежный подход: жадно найти первую, затем жадно найти вторую с хотя бы одним отличием
    first = []
    j = 0
    for i in range(N):
        if j < M and A[i] == B[j]:
            first.append(i)
            j += 1
    
    if len(first) < M:
        print("No")
        return
    
    # Пытаемся найти вторую подпоследовательность, которая отличается хотя бы в одной позиции
    for diff_pos in range(M):
        second = []
        j = 0
        for i in range(N):
            if j < M and A[i] == B[j]:
                if j == diff_pos:
                    # В этой позиции пытаемся взять другой индекс
                    if i != first[j]:
                        second.append(i)
                        j += 1
                else:
                    second.append(i)
                    j += 1
        
        if len(second) == M and second != first:
            print("Yes")
            return
    
    print("No")

solve()