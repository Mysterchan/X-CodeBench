def solve_subarray(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # dp[i] = (operations, carry1, carry2)
    # carry1: 可以传递到i+1位置的值
    # carry2: 可以传递到i+2位置的值
    
    operations = 0
    carry1 = 0  # 从i-1传递来的
    carry2 = 0  # 从i-2传递来的
    
    for i in range(n):
        current = arr[i]
        
        # 当前位置可用的值
        available = current + carry1 + carry2
        
        # 尽可能配对（每次配对消耗2）
        pairs = available // 2
        operations += pairs
        
        # 剩余的值传递到下一个位置
        remainder = available % 2
        
        # 更新carry
        carry2 = carry1
        carry1 = remainder
    
    return operations

# 读取输入
n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    subarray = a[l-1:r]
    result = solve_subarray(subarray)
    print(result)