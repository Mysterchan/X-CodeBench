N = int(input())
ranges = []
for _ in range(N):
    L, R = map(int, input().split())
    ranges.append((L, R))

Q = int(input())
queries = [int(input()) for _ in range(Q)]

# 用于计算在所有比赛中评分增加次数的助力数组
increment_count = [0] * (500001)

# 记录评分区间的变化
for L, R in ranges:
    increment_count[L] += 1
    if R + 1 < len(increment_count):
        increment_count[R + 1] -= 1

# 计算准确的增量评分
for i in range(1, len(increment_count)):
    increment_count[i] += increment_count[i - 1]

results = []
for X in queries:
    results.append(X + increment_count[X])

# 输出结果
print("\n".join(map(str, results)))