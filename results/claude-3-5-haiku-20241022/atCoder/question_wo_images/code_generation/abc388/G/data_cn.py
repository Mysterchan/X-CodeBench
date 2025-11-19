def solve_query(A, L, R):
    # 获取区间内的麻糬（转换为0-indexed）
    mochis = A[L-1:R]
    n = len(mochis)
    
    # 二分搜索最大配对数
    left, right = 0, n // 2
    
    while left < right:
        mid = (left + right + 1) // 2
        
        # 检查是否可以配对mid个鏡餅
        # 贪心策略：从最小的开始，尽量配对
        used = [False] * n
        pairs = 0
        
        for i in range(n):
            if used[i]:
                continue
            # 找第一个可以放在当前麻糬上的麻糬
            for j in range(i + 1, n):
                if not used[j] and mochis[i] * 2 <= mochis[j]:
                    used[i] = True
                    used[j] = True
                    pairs += 1
                    break
        
        if pairs >= mid:
            left = mid
        else:
            right = mid - 1
    
    return left

# 读取输入
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())
    print(solve_query(A, L, R))