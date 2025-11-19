import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 初始 sumA 為 A 中所有為1的 C_i 之和
sumA = 0
for i in range(N):
    if A[i] == 1:
        sumA += C[i]

total_cost = 0

# 對每個位置 i，若 A[i] != B[i]，則必須翻轉
# 翻轉後，A[i] = 1 - A[i]
# 翻轉成本為當前 sumA
# 翻轉後更新 sumA
for i in range(N):
    if A[i] != B[i]:
        total_cost += sumA
        if A[i] == 1:
            sumA -= C[i]
        else:
            sumA += C[i]
        A[i] = 1 - A[i]

print(total_cost)