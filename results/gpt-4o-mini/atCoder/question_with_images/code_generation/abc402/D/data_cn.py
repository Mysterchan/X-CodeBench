def count_intersections(N, M, lines):
    # 将线段的端点转换为0-based索引
    segments = [(min(A - 1, B - 1), max(A - 1, B - 1)) for A, B in lines]
    
    # 记录每条线的交点
    intersections = 0
    
    # 使用双重循环检查每对线段是否相交
    for i in range(M):
        for j in range(i + 1, M):
            a1, b1 = segments[i]
            a2, b2 = segments[j]
            # 检查线段是否相交
            if (a1 < a2 < b1 < b2) or (a2 < a1 < b2 < b1):
                intersections += 1
    
    return intersections

# 读取输入
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
lines = [tuple(map(int, line.split())) for line in data[1:M + 1]]

# 输出结果
print(count_intersections(N, M, lines))