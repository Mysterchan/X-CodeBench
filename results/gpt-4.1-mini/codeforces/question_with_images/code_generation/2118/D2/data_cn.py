import sys
import bisect
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    d = list(map(int, input().split()))
    q = int(input())
    a = list(map(int, input().split()))

    # 预处理：计算每个红绿灯的状态周期中的红灯时间点 mod k
    # 红灯时间点为 t ≡ d_i (mod k)
    # 由于每秒移动一格，且每秒检查当前位置红灯状态，红灯时会转向。
    # 关键是判断从起点出发，是否会被红灯转向形成循环，还是最终离开区间。

    # 观察：
    # 1. 只有在红灯位置且时间 t 满足 t % k == d_i 时才转向。
    # 2. 时间 t = 步数，从起点出发，步数即为移动的格数。
    # 3. 方向初始为向右（+1）。
    # 4. 每秒：
    #    - 若当前位置有红灯且 (t % k == d_i)，转向（方向 *= -1）
    #    - 然后移动一步（pos += direction）

    # 目标：判断是否在 10^100 秒内离开区间 [p[0], p[-1]]。

    # 由于区间极大，模拟不可行。
    # 需要利用周期性和区间结构。

    # 关键点：
    # - 只有在红灯位置且时间满足条件时才转向。
    # - 转向会导致可能在区间内来回。
    # - 如果能找到一个方向，且从起点出发不会被红灯阻挡，最终会离开区间。
    # - 否则会陷入循环。

    # 方案：
    # 对每个红灯，计算其“红灯时间点” d_i。
    # 对于起点 a_i，考虑两种方向：
    #   - 向右走，遇到的第一个红灯位置 >= a_i
    #   - 向左走，遇到的第一个红灯位置 <= a_i
    # 判断是否会被红灯转向阻挡。

    # 由于转向只发生在红灯且时间满足条件，且时间 = 步数，
    # 我们可以预先计算每个红灯位置 p_i 对应的时间 t % k = (start_time + steps) % k，
    # 其中 steps = abs(p_i - start_pos)

    # 具体：
    # 对于起点 a_i，初始方向为 +1，时间 t=0。
    # 走向右边：
    #   找第一个红灯位置 p_j >= a_i
    #   计算 steps = p_j - a_i
    #   时间 t = steps
    #   若 t % k == d_j，则转向，方向变为 -1，继续向左走。
    #   否则继续向右走，直到离开区间。

    # 类似地，向左走：
    #   找第一个红灯位置 p_j <= a_i
    #   计算 steps = a_i - p_j
    #   时间 t = steps
    #   若 t % k == d_j，则转向，方向变为 +1，继续向右走。
    #   否则继续向左走，直到离开区间。

    # 由于转向可能多次发生，形成循环。
    # 但题目中 k 和 n 总和较大，不能模拟。
    # 观察发现：
    # - 转向只发生在红灯位置且时间满足条件。
    # - 由于时间 t = 步数，且每次转向后方向反转，路径在区间内来回。
    # - 如果在某个方向上没有红灯阻挡，必定会离开区间。
    # - 如果两边都被红灯阻挡且形成循环，则不会离开。

    # 因此，我们只需判断：
    # - 从起点向右走，是否会遇到红灯且时间满足转向条件。
    # - 从起点向左走，是否会遇到红灯且时间满足转向条件。
    # - 如果两边都被阻挡，则不会离开。
    # - 否则会离开。

    # 具体实现：
    # 对每个查询 a_i：
    # 1. 找右边第一个红灯位置 idx_r = bisect_left(p, a_i)
    #    若 idx_r < n:
    #       steps = p[idx_r] - a_i
    #       if steps % k == d[idx_r]: right_blocked = True
    #       else right_blocked = False
    #    else right_blocked = False (无红灯阻挡)
    #
    # 2. 找左边第一个红灯位置 idx_l = bisect_right(p, a_i) - 1
    #    若 idx_l >= 0:
    #       steps = a_i - p[idx_l]
    #       if steps % k == d[idx_l]: left_blocked = True
    #       else left_blocked = False
    #    else left_blocked = False (无红灯阻挡)
    #
    # 3. 如果左右都阻挡，则输出 NO，否则 YES。

    # 该判断基于：
    # - 如果两边都被红灯阻挡，且转向条件满足，则会在区间内来回，永远不会离开。
    # - 否则至少有一边可以直接离开。

    # 注意：起点本身如果是红灯且 t=0 满足转向条件，也会转向。
    # 但 t=0，步数=0，只有当 a_i 是红灯位置且 0 % k == d_i 才转向。
    # 这会影响方向初始值。
    # 但由于方向初始为向右，转向后变向左，判断时考虑即可。

    # 但题目中起点不一定是红灯位置，且转向后方向反转。
    # 由于我们只判断是否会离开，方向初始向右，转向后方向反转。
    # 只要两边都阻挡，才不会离开。

    # 处理起点是否为红灯：
    # 如果起点是红灯且 t=0 % k == d_i，方向反转，初始方向为左。
    # 这会影响判断。
    # 因此，先判断起点是否为红灯且 t=0 满足转向条件：
    # 如果是，初始方向为左，否则为右。

    # 根据初始方向，判断对应方向是否阻挡：
    # 如果初始方向为右，判断右边阻挡；
    # 如果初始方向为左，判断左边阻挡。

    # 但题目中每秒先判断红灯转向再移动。
    # 起点 t=0，先判断是否转向。
    # 所以初始方向可能是左或右。

    # 综上：
    # - 判断起点是否为红灯且 t=0 满足转向条件，确定初始方向。
    # - 判断初始方向对应方向是否阻挡。
    # - 判断反方向是否阻挡。
    # - 如果两边都阻挡，则 NO，否则 YES。

    # 实现：

    pos_to_idx = {}
    for i, pos in enumerate(p):
        pos_to_idx[pos] = i

    for start in a:
        # 判断起点是否为红灯且 t=0 满足转向条件
        if start in pos_to_idx and (0 % k) == d[pos_to_idx[start]]:
            direction = -1  # 向左
        else:
            direction = 1  # 向右

        # 判断右边阻挡
        idx_r = bisect.bisect_left(p, start)
        right_blocked = False
        if idx_r < n:
            steps = p[idx_r] - start
            if steps % k == d[idx_r]:
                right_blocked = True

        # 判断左边阻挡
        idx_l = bisect.bisect_right(p, start) - 1
        left_blocked = False
        if idx_l >= 0:
            steps = start - p[idx_l]
            if steps % k == d[idx_l]:
                left_blocked = True

        # 根据初始方向判断是否会离开
        # 如果初始方向阻挡，则会转向，方向反转
        # 如果两边都阻挡，则不会离开
        if direction == 1:
            # 初始向右
            if right_blocked and left_blocked:
                print("NO")
            else:
                print("YES")
        else:
            # 初始向左
            if left_blocked and right_blocked:
                print("NO")
            else:
                print("YES")