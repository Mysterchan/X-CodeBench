import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for __ in range(n)]

    row_max = [max(row) for row in a]
    col_max = [max(a[i][j] for i in range(n)) for j in range(m)]

    # 找出行最大值的最大值和次大值及其索引
    max_row_val = max(row_max)
    max_row_idx = [i for i, v in enumerate(row_max) if v == max_row_val]
    second_max_row_val = max((v for v in row_max if v < max_row_val), default=-1)

    # 找出列最大值的最大值和次大值及其索引
    max_col_val = max(col_max)
    max_col_idx = [j for j, v in enumerate(col_max) if v == max_col_val]
    second_max_col_val = max((v for v in col_max if v < max_col_val), default=-1)

    # 初始答案为减1后最大值不变的情况
    ans = max(max_row_val, max_col_val)

    # 尝试所有最大行和最大列的组合
    # 对于每个组合，计算减1后矩阵的最大值
    # 减1后，行r和列c的元素都减1
    # 最大值可能出现在：
    # 1) 行r或列c的最大值减1
    # 2) 其他行或列的最大值不变
    # 3) 交叉点a[r][c]减2（因为行和列都减1）
    # 需要考虑交叉点减2的情况，可能使最大值更小

    for r in max_row_idx:
        for c in max_col_idx:
            # 交叉点减2
            cross_val = a[r][c] - 2

            # 行r最大值减1
            row_val = row_max[r] - 1

            # 列c最大值减1
            col_val = col_max[c] - 1

            # 其他行最大值（除了r）
            other_row_max = max_row_val if row_max[r] != max_row_val else second_max_row_val
            # 其他列最大值（除了c）
            other_col_max = max_col_val if col_max[c] != max_col_val else second_max_col_val

            # 最大值是这些值的最大值
            cur_max = max(cross_val, row_val, col_val, other_row_max, other_col_max)
            ans = min(ans, cur_max)

    print(ans)