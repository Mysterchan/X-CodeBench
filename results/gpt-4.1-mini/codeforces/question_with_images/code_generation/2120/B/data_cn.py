import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    count = 0
    for __ in range(n):
        dx, dy, x, y = map(int, input().split())
        # 球以45度角速度极快发射，且弹性反弹。
        # 经过反弹后，球的轨迹可视为在无限平铺的镜像桌面上直线运动。
        # 口袋坐标为(0,0),(0,s),(s,0),(s,s)。
        # 球最终会落入口袋当且仅当存在整数k，使得：
        # x + dx*t = k*s 或者 反弹后等效坐标为口袋坐标
        # 由于速度极大，球会在有限时间内到达某个口袋。
        # 通过“镜像法”，球的轨迹映射到无限平铺的桌面上，
        # 球的坐标在镜像桌面上为 (x + dx*t, y + dy*t)。
        # 球进洞等价于存在t，使得 x + dx*t 和 y + dy*t 同时等于某个口袋坐标。
        # 口袋坐标在镜像桌面上是所有 (m*s, n*s) 其中 m,n 为整数。
        # 因此，存在整数 k_x, k_y 使得：
        # x + dx*t = k_x * s
        # y + dy*t = k_y * s
        # 两式相减：
        # (x - y) + (dx - dy)*t = (k_x - k_y)*s
        # 由于 dx, dy ∈ {-1,1}，dx - dy ∈ {-2,0,2}
        # 若 dx == dy，则 dx - dy = 0，需 x - y = (k_x - k_y)*s，即 x ≡ y (mod s)
        # 若 dx != dy，则 dx - dy = ±2，t = ((k_x - k_y)*s - (x - y)) / (dx - dy)
        # t 必须为正整数。
        # 由于速度极大，t 可以非常大，只要存在满足条件的整数 k_x,k_y 即可。
        # 综上，判断条件简化为：
        # 若 dx == dy，判断 x % s == y % s
        # 若 dx != dy，判断 (x + y) % s == 0
        if dx == dy:
            if (x - y) % s == 0:
                count += 1
        else:
            if (x + y) % s == 0:
                count += 1
    print(count)