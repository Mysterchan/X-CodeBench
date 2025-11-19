def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

Q = int(input())
removed = []

for _ in range(Q):
    A, B = map(int, input().split())
    removed.append(A)
    
    # 使用容斥原理計算有多少數字被移除
    n = len(removed)
    
    # 二分搜索第 B 小的數字
    left, right = 1, B * 10
    
    while left < right:
        mid = (left + right) // 2
        
        # 計算 [1, mid] 中有多少數字沒被移除
        total = mid
        
        # 使用容斥原理計算被移除的數字數量
        excluded = 0
        for mask in range(1, 1 << n):
            current_lcm = 1
            bit_count = 0
            
            for i in range(n):
                if mask & (1 << i):
                    bit_count += 1
                    current_lcm = lcm(current_lcm, removed[i])
                    if current_lcm > mid:
                        break
            
            if current_lcm <= mid:
                count = mid // current_lcm
                if bit_count % 2 == 1:
                    excluded += count
                else:
                    excluded -= count
        
        remaining = total - excluded
        
        if remaining < B:
            left = mid + 1
        else:
            right = mid
    
    print(left)