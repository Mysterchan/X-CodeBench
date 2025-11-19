N, K = map(int, input().split())

# 总步数
steps = 2 * N - 2

# 当前位置
r, c = 1, 1

res = []

for _ in range(steps):
    # 如果已经在最后一行，只能向右
    if r == N:
        res.append('R')
        c += 1
        continue
    # 如果已经在最后一列，只能向下
    if c == N:
        res.append('D')
        r += 1
        continue

    # 计算向下移动的路径数（从下方格子到终点的路径数）
    # 计算组合数 C(a, b) = number of ways to arrange moves
    # 这里用动态规划计算组合数
    # 但N最大100，组合数不会溢出64位整数

    # 计算从 (r+1, c) 到 (N, N) 的路径数
    down_remain = (N - (r + 1)) + (N - c)
    down_ways = 1
    # 计算组合数 C(down_remain, N - (r + 1))
    # 组合数 C(n, k) = n! / (k! * (n-k)!)
    # 用乘法计算避免大数阶乘
    k1 = N - (r + 1)
    n1 = down_remain
    if k1 < 0 or k1 > n1:
        down_ways = 0
    else:
        # 计算组合数
        c_val = 1
        for i in range(1, k1 + 1):
            c_val = c_val * (n1 - i + 1) // i
        down_ways = c_val

    # 计算从 (r, c+1) 到 (N, N) 的路径数
    right_remain = (N - r) + (N - (c + 1))
    k2 = N - r
    n2 = right_remain
    if k2 < 0 or k2 > n2:
        right_ways = 0
    else:
        c_val = 1
        for i in range(1, k2 + 1):
            c_val = c_val * (n2 - i + 1) // i
        right_ways = c_val

    # 根据题意：
    # 如果两者访问次数相等，选向下
    # 访问次数 = 之前练习中该格被访问次数
    # 访问次数 = 之前练习数 - 该方向路径数
    # 因为之前练习数 = K-1
    # 访问次数下 = (K-1) - down_ways
    # 访问次数右 = (K-1) - right_ways
    # 比较访问次数即比较 down_ways 和 right_ways
    # 访问次数少的方向对应路径数多的方向
    # 选择访问次数少的方向 == 选择路径数多的方向
    # 如果相等，选向下

    if down_ways >= right_ways:
        res.append('D')
        r += 1
    else:
        res.append('R')
        c += 1

print(''.join(res))