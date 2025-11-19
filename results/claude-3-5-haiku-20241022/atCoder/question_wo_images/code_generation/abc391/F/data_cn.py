import heapq

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    # 对数组排序（降序）
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    
    # 使用最大堆找第K大的值
    # 堆中存储: (-value, i, j, k)
    heap = []
    visited = set()
    
    # 初始值：最大的组合
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
        
        # 尝试扩展到相邻的组合
        neighbors = [
            (i + 1, j, k),
            (i, j + 1, k),
            (i, j, k + 1)
        ]
        
        for ni, nj, nk in neighbors:
            if ni < N and nj < N and nk < N and (ni, nj, nk) not in visited:
                visited.add((ni, nj, nk))
                val = A[ni] * B[nj] + B[nj] * C[nk] + C[nk] * A[ni]
                heapq.heappush(heap, (-val, ni, nj, nk))
    
    print(result)

solve()