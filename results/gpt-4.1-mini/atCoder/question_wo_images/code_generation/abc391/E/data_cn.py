import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
A = sys.stdin.readline().strip()

# 预处理：将字符串转为整数列表，方便处理
A_list = list(map(int, A))

# dp(l, r) 返回一个字典 {v: min_changes}，表示区间[l,r)经过N次操作后最终值为v(0或1)的最小修改次数
# 这里区间长度必为3^k
def dp(l, r):
    length = r - l
    if length == 1:
        # 叶子节点，只有一个元素
        val = A_list[l]
        return {0: 0 if val == 0 else 1, 1: 0 if val == 1 else 1}
    else:
        # 分成3段
        third = length // 3
        left = dp(l, l + third)
        mid = dp(l + third, l + 2 * third)
        right = dp(l + 2 * third, r)

        res = {0: float('inf'), 1: float('inf')}

        # 对于最终值v，考虑三段的多数值组合
        # 多数值是0的组合：
        # (0,0,0), (0,0,1), (0,1,0), (1,0,0)
        # 多数值是1的组合：
        # (1,1,1), (1,1,0), (1,0,1), (0,1,1)

        # 枚举所有8种组合，计算对应的总代价，更新res[v]
        for a in (0,1):
            for b in (0,1):
                for c in (0,1):
                    # 计算多数值
                    s = a + b + c
                    majority = 1 if s >= 2 else 0
                    cost = left[a] + mid[b] + right[c]
                    if cost < res[majority]:
                        res[majority] = cost
        return res

res = dp(0, 3**N)

# A'_1 是最终值，原始值是经过N次操作得到的多数值
# 题目要求改变最终值，即从res中选择与原最终值相反的最小修改次数
# 先计算原最终值
def get_final_value(arr):
    cur = arr
    length = len(cur)
    while length > 1:
        next_arr = []
        for i in range(0, length, 3):
            s = cur[i] + cur[i+1] + cur[i+2]
            next_arr.append(1 if s >= 2 else 0)
        cur = next_arr
        length = len(cur)
    return cur[0]

orig_final = get_final_value(A_list)

# 输出改变最终值所需的最小修改次数
print(res[1 - orig_final])