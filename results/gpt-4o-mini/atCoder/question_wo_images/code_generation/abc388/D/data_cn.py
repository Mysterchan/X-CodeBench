N = int(input())
A = list(map(int, input().split()))

# 统计成年外星人数量
B = [0] * N

# 逐年计算
for i in range(N):
    # 成年后的人会送礼物
    if i > 0:
        gift = sum(1 for x in A if x > 0)  # 在i年后成年，统计当前有石头的外星人数量
        A = [max(0, A[j] - 1) for j in range(N)]  # 每个外星人减少一颗石头
        A[i] += gift  # 赠送额外石头
    B[i] = A[i]

print(' '.join(map(str, B)))