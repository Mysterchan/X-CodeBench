N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# 创建一个结果数组
S = [0] * N

# 根据 P 数组找到每个人盯着的人的围裙数字
for i in range(N):
    S[i] = Q[P[i] - 1]

# 输出结果
print(' '.join(map(str, S)))