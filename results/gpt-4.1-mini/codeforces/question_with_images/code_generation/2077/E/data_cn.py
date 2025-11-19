import sys
input = sys.stdin.readline
MOD = 998244353

# 根據題意與示例分析，f(b) = max(b) - min(b)
# 因為折疊與染料操作可視為將條帶重疊，最終黑暗度為各位置的最大值與最小值差距決定所需操作數。
# 因此題目化為計算所有子陣列的 max - min 之和。

# 使用單調棧分別計算所有子陣列中元素作為最大值和最小值的貢獻，然後相減。

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # 計算所有子陣列中元素作為最大值的貢獻和
        max_stack = []
        max_contrib = 0
        left = [0]*n
        right = [0]*n

        # 找左邊第一個比a[i]大的位置 (嚴格大)
        for i in range(n):
            while max_stack and a[max_stack[-1]] <= a[i]:
                max_stack.pop()
            left[i] = max_stack[-1] if max_stack else -1
            max_stack.append(i)

        max_stack.clear()
        # 找右邊第一個比a[i]大的位置 (嚴格大)
        for i in range(n-1, -1, -1):
            while max_stack and a[max_stack[-1]] < a[i]:
                max_stack.pop()
            right[i] = max_stack[-1] if max_stack else n
            max_stack.append(i)

        max_sum = 0
        for i in range(n):
            max_sum += a[i] * (i - left[i]) * (right[i] - i)
            max_sum %= MOD

        # 計算所有子陣列中元素作為最小值的貢獻和
        min_stack = []
        left = [0]*n
        right = [0]*n

        # 找左邊第一個比a[i]小的位置 (嚴格小)
        for i in range(n):
            while min_stack and a[min_stack[-1]] >= a[i]:
                min_stack.pop()
            left[i] = min_stack[-1] if min_stack else -1
            min_stack.append(i)

        min_stack.clear()
        # 找右邊第一個比a[i]小的位置 (嚴格小)
        for i in range(n-1, -1, -1):
            while min_stack and a[min_stack[-1]] > a[i]:
                min_stack.pop()
            right[i] = min_stack[-1] if min_stack else n
            min_stack.append(i)

        min_sum = 0
        for i in range(n):
            min_sum += a[i] * (i - left[i]) * (right[i] - i)
            min_sum %= MOD

        ans = (max_sum - min_sum) % MOD
        print(ans)

if __name__ == "__main__":
    solve()