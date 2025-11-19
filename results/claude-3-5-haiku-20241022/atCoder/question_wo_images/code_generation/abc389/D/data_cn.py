R = int(input())

count = 0
# 只需要检查第一象限和坐标轴，利用对称性
# 对于每个正方形(i,j)，四个角点是(i±0.5, j±0.5)
# 正方形完全在圆内意味着所有四个角都在圆内
# 最远的角距离原点sqrt((|i|+0.5)^2 + (|j|+0.5)^2) <= R

# 由于对称性，我们可以只计算i>=0, j>=0的情况
# 然后根据对称性计算总数

# 当i=0, j=0时，四个角点距离都是sqrt(0.5^2 + 0.5^2) = sqrt(0.5)
# 最远角点距离是sqrt((i+0.5)^2 + (j+0.5)^2)

max_coord = R + 1

for i in range(max_coord):
    for j in range(max_coord):
        # 对于正方形(i,j)，检查最远的角点
        max_dist_sq = (i + 0.5) ** 2 + (j + 0.5) ** 2
        
        if max_dist_sq <= R * R:
            # 根据对称性计算贡献
            if i == 0 and j == 0:
                count += 1
            elif i == 0:
                count += 2  # (0,j) 和 (0,-j)
            elif j == 0:
                count += 2  # (i,0) 和 (-i,0)
            else:
                count += 4  # (i,j), (i,-j), (-i,j), (-i,-j)
        elif j == 0:
            # 如果j=0时都不满足，更大的j也不会满足
            break

print(count)