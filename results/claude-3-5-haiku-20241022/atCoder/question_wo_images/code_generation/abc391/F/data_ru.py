import heapq

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    # Сортируем массивы в порядке убывания
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    
    # Используем max-heap для поиска K-го максимального значения
    # В Python heapq - это min-heap, поэтому используем отрицательные значения
    heap = []
    visited = set()
    
    # Начинаем с максимального возможного значения (0, 0, 0)
    initial_val = A[0] * B[0] + B[0] * C[0] + C[0] * A[0]
    heapq.heappush(heap, (-initial_val, 0, 0, 0))
    visited.add((0, 0, 0))
    
    count = 0
    result = 0
    
    while heap and count < K:
        neg_val, i, j, k = heapq.heappop(heap)
        result = -neg_val
        count += 1
        
        if count == K:
            break
        
        # Добавляем соседей
        neighbors = [
            (i + 1, j, k),
            (i, j + 1, k),
            (i, j, k + 1)
        ]
        
        for ni, nj, nk in neighbors:
            if ni < N and nj < N and nk < N and (ni, nj, nk) not in visited:
                val = A[ni] * B[nj] + B[nj] * C[nk] + C[nk] * A[ni]
                heapq.heappush(heap, (-val, ni, nj, nk))
                visited.add((ni, nj, nk))
    
    print(result)

solve()