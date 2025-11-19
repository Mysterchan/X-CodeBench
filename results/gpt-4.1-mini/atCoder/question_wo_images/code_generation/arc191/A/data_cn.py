import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(input().strip())
T = list(input().strip())

# 對 S 進行排序，從小到大，方便從最小的開始替換
S.sort()

# 對 T 進行排序，從大到小，優先使用最大的數字替換 S 中較小的數字
T.sort(reverse=True)

i = 0  # S 的索引，從最小的開始替換
j = 0  # T 的索引，從最大的開始使用

while i < N and j < M:
    if S[i] < T[j]:
        S[i] = T[j]
        i += 1
        j += 1
    else:
        # 如果 S[i] >= T[j]，表示後面的 S[i] 也不會比 T[j] 小，停止替換
        break

# 將結果排序回原本的數字順序（因為題目要求最大整數，排序後的 S 即為最大整數）
S.sort(reverse=True)

print("".join(S))