t = int(input())
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    # 矩形尺寸已满足 l3 ≤ l2 ≤ l1 且 b3 ≤ b2 ≤ b1，且不可旋转

    # 总面积
    total_area = l1*b1 + l2*b2 + l3*b3

    # 目标正方形边长必须是整数且面积等于总面积
    side = int(total_area**0.5)
    if side*side != total_area:
        print("NO")
        continue

    # 尝试排列方式：
    # 1. 三个矩形竖直叠加，宽度相同且等于side，高度和为side
    if l1 == l2 == l3 == side and b1 + b2 + b3 == side:
        print("YES")
        continue

    # 2. 三个矩形水平并排，高度相同且等于side，宽度和为side
    if b1 == b2 == b3 == side and l1 + l2 + l3 == side:
        print("YES")
        continue

    # 3. 先放最大矩形，剩下两个矩形拼接在旁边或下面形成正方形
    # 3.1 最大矩形在左，剩余两个竖直叠加在右边
    # 条件：l1 == side，b1 < side，且右边两个矩形宽度为 side - b1，高度和为 side
    if l1 == side and b1 < side:
        if l2 == l3 == side - b1 and b2 + b3 == side:
            print("YES")
            continue

    # 3.2 最大矩形在上，剩余两个水平并排在下面
    # 条件：b1 == side，l1 < side，且下面两个矩形高度为 side - l1，宽度和为 side
    if b1 == side and l1 < side:
        if b2 == b3 == side - l1 and l2 + l3 == side:
            print("YES")
            continue

    print("NO")