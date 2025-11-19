n = int(input())
a = list(map(int, input().split()))

# dp[i][j] = 处理前i个元素后，S中有j个元素时的最大和
# 由于j最多为i，我们可以用字典优化空间
INF = float('-inf')

# 当前状态: dp[length] = max_sum
prev = {0: 0}

for i in range(n):
    curr = {}
    for length, sum_val in prev.items():
        # 操作1: 添加 a[i]
        new_length = length + 1
        new_sum = sum_val + a[i]
        if new_length not in curr or curr[new_length] < new_sum:
            curr[new_length] = new_sum
        
        # 操作2: 删除最后一个元素（如果length > 0）
        if length > 0:
            new_length = length - 1
            # 删除操作不改变sum，但我们需要知道删除哪个元素
            # 这里有个问题：我们不知道最后一个元素是什么
            # 需要重新思考状态定义
            pass
    
    prev = curr

# 重新思考：需要记录序列S的实际内容
# 使用dp[i][状态] 其中状态包含S的内容

# 更好的方法：动态规划记录可能的序列
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(idx, s_tuple):
    if idx == n:
        return sum(s_tuple)
    
    s = list(s_tuple)
    
    # 操作1: 添加a[idx]
    s1 = s + [a[idx]]
    res1 = solve(idx + 1, tuple(s1))
    
    # 操作2: 删除最后元素（如果可以）
    res2 = INF
    if len(s) > 0:
        s2 = s[:-1]
        res2 = solve(idx + 1, tuple(s2))
    
    return max(res1, res2)

print(solve(0, ()))