import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, x, y, vx, vy = map(int, input().split())
        # 飞机初始点(x,y)在三角形内部，三角形顶点为(0,0),(0,n),(n,0)
        # 飞机速度(vx, vy)，均为正数

        # 飞机运动轨迹在折射反射后等价于在无限平铺的三角形中直线运动
        # 通过对称展开，将三角形映射到正方形[0,n]x[0,n]的镜像运动
        # 反射边界对应坐标轴的镜像反射
        # 逃离三角洲即到达顶点(0,0),(0,n),(n,0)
        # 在正方形中顶点对应四个点：(0,0),(0,n),(n,0),(n,n)
        # 但原三角形顶点只有前三个，(n,n)不属于原三角形顶点

        # 关键：飞机在三角形内运动，反射边界为三条边：
        # x=0, y=0, x+y=n
        # 反射后速度分量对应坐标轴反射：
        # x=0边反射vx -> -vx
        # y=0边反射vy -> -vy
        # x+y=n边反射速度向量关于该边的法线反射
        # 但通过对称展开，等价于在正方形[0,n]x[0,n]中，x,y坐标分别对0和n反射
        # 但要保证点始终满足x+y<=n，故需要对x,y做“折叠”映射

        # 解决方案：
        # 1. 将飞机运动映射到正方形[0,n]x[0,n]的镜像运动
        # 2. 飞机初始点(x,y)，速度(vx,vy)
        # 3. 飞机运动轨迹为：
        #    X(t) = x + vx * t
        #    Y(t) = y + vy * t
        # 4. 对X(t),Y(t)分别对2n取模并折叠：
        #    pos = p mod (2n)
        #    if pos > n: pos = 2n - pos
        # 5. 飞机逃离三角洲即到达顶点(0,0),(0,n),(n,0)
        #    在正方形中对应点(0,0),(0,n),(n,0)
        # 6. 计算t使得X(t),Y(t)等于顶点坐标
        # 7. 由于折叠，X(t)和Y(t)满足：
        #    X(t) = m_x * 2n ± target_x
        #    Y(t) = m_y * 2n ± target_y
        #    其中m_x,m_y为非负整数，±表示折叠后可能的两种情况
        # 8. 对每个顶点，尝试所有±组合，求t满足：
        #    t = (m_x * 2n ± target_x - x) / vx
        #    t = (m_y * 2n ± target_y - y) / vy
        #    两式相等且t>=0
        # 9. 找到最小的t，计算撞击次数：
        #    撞击次数 = m_x + m_y
        # 10. 如果无解，输出-1

        # 顶点列表
        vertices = [(0,0),(0,n),(n,0)]

        ans = -1
        for tx, ty in vertices:
            # ±组合
            for sx in [1,-1]:
                for sy in [1,-1]:
                    # 枚举m_x,m_y
                    # 由等式：
                    # (m_x*2n + sx*tx - x)/vx = (m_y*2n + sy*ty - y)/vy = t >= 0
                    # 设 t = T
                    # T*vx = m_x*2n + sx*tx - x
                    # T*vy = m_y*2n + sy*ty - y
                    # 两式相减：
                    # T*vx - T*vy = (m_x - m_y)*2n + sx*tx - sy*ty - (x - y)
                    # T*(vx - vy) = (m_x - m_y)*2n + sx*tx - sy*ty - (x - y)

                    # 令 A = 2n, B = sx*tx - sy*ty - (x - y)
                    # T*(vx - vy) = (m_x - m_y)*A + B

                    # 但m_x,m_y非负整数，且T = (m_x*2n + sx*tx - x)/vx
                    # 需要枚举m_x,m_y使得T相等且非负

                    # 由于m_x,m_y非负，且vx,vy,x,y,n均大，暴力枚举不可行
                    # 改用数学方法：

                    # 设:
                    # t = (m_x*2n + sx*tx - x)/vx
                    # t = (m_y*2n + sy*ty - y)/vy

                    # 两式相等:
                    # (m_x*2n + sx*tx - x)/vx = (m_y*2n + sy*ty - y)/vy
                    # 交叉相乘:
                    # vy*(m_x*2n + sx*tx - x) = vx*(m_y*2n + sy*ty - y)
                    # 2n*(vy*m_x - vx*m_y) = vx*(sy*ty - y) - vy*(sx*tx - x)

                    # 令:
                    # C = vx*(sy*ty - y) - vy*(sx*tx - x)
                    # 2n*(vy*m_x - vx*m_y) = C

                    # 设:
                    # a = vy
                    # b = -vx
                    # 方程:
                    # 2n*(a*m_x + b*m_y) = C

                    # 令:
                    # a*m_x + b*m_y = C/(2n)

                    # 需要C/(2n)为整数，否则无解

                    # 由于m_x,m_y非负整数，求解不定方程

                    # 先判断C是否能被2n整除
                    if C := vx*(sy*ty - y) - vy*(sx*tx - x):
                        if C % (2*n) != 0:
                            continue
                        rhs = C // (2*n)
                    else:
                        rhs = 0

                    # 方程: a*m_x + b*m_y = rhs
                    # a=vy>0, b=-vx<0
                    # m_x,m_y>=0

                    # 转为: vy*m_x - vx*m_y = rhs

                    # 枚举m_x，求m_y = (vy*m_x - rhs)/vx
                    # m_y必须为整数且>=0

                    # m_x >= 0
                    # m_y = (vy*m_x - rhs)/vx >= 0且整数

                    # m_y整数 => vy*m_x - rhs ≡ 0 mod vx

                    # 由于vx, vy大，枚举m_x不可行

                    # 使用扩展欧几里得求解不定方程

                    from math import gcd

                    g = gcd(vy, vx)
                    if rhs % g != 0:
                        continue
                    # 简化方程
                    a1 = vy // g
                    b1 = vx // g
                    c1 = rhs // g

                    # 求解 a1*m_x - b1*m_y = c1

                    # 扩展欧几里得求一组解
                    def extended_gcd(a,b):
                        if b==0:
                            return a,1,0
                        g,x1,y1 = extended_gcd(b,a%b)
                        x = y1
                        y = x1 - (a//b)*y1
                        return g,x,y

                    _, x0, y0 = extended_gcd(a1, b1)
                    x0 *= c1
                    y0 *= c1

                    # 通解:
                    # m_x = x0 + k*b1
                    # m_y = y0 + k*a1

                    # m_x,m_y >=0
                    # 求k范围

                    # m_x >=0 => x0 + k*b1 >=0 => k >= -x0/b1
                    # m_y >=0 => y0 + k*a1 >=0 => k >= -y0/a1

                    # k下界为 max(ceil(-x0/b1), ceil(-y0/a1))

                    from math import ceil

                    k_min = max(ceil(-x0 / b1), ceil(-y0 / a1))

                    # k_min为最小整数k使m_x,m_y非负

                    # 计算对应t:
                    m_x = x0 + k_min * b1
                    m_y = y0 + k_min * a1

                    # 计算t:
                    # t = (m_x*2n + sx*tx - x)/vx
                    numerator = m_x * 2 * n + sx * tx - x
                    if numerator < 0:
                        continue
                    if numerator % vx != 0:
                        continue
                    t = numerator / vx
                    if t < 0:
                        continue

                    # 验证另一式:
                    numerator_y = m_y * 2 * n + sy * ty - y
                    if numerator_y < 0:
                        continue
                    if numerator_y % vy != 0:
                        continue
                    t_y = numerator_y / vy
                    if abs(t - t_y) > 1e-14:
                        continue

                    # 找最小t
                    if ans == -1 or t < ans_t:
                        ans = m_x + m_y
                        ans_t = t

        print(ans)

solve()