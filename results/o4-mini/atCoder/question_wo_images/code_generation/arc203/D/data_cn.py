import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 计算初始相邻不同对数
cnt = 0
for i in range(N - 1):
    if A[i] != A[i + 1]:
        cnt += 1

for _ in range(Q):
    i = int(input()) - 1
    # 翻转 A[i]
    old_val = A[i]
    A[i] ^= 1
    new_val = A[i]

    # 检查 i-1 和 i 的边界
    if i > 0:
        if A[i - 1] != old_val:
            cnt -= 1
        if A[i - 1] != new_val:
            cnt += 1

    # 检查 i 和 i+1 的边界
    if i < N - 1:
        if old_val != A[i + 1]:
            cnt -= 1
        if new_val != A[i + 1]:
            cnt += 1

    print(cnt + 1)