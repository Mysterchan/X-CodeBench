import sys
input = sys.stdin.readline

# 預先計算 Fibonacci 立方體邊長 f_i (1-based)
# f_1=1, f_2=2, f_i=f_{i-1}+f_{i-2}
max_n = 10
fib = [0]*(max_n+1)
fib[1], fib[2] = 1, 2
for i in range(3, max_n+1):
    fib[i] = fib[i-1] + fib[i-2]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cubes = fib[1:n+1]

    # 計算所有立方體的底面面積和高度總和
    # 底面積 = max(f_i)^2 (因為必須放在底部或其他立方體上，且較大立方體不能放在較小立方體上)
    # 但題目中立方體必須堆疊，且較大立方體不能放在較小立方體上
    # 因此立方體必須從最大到最小依序堆疊，底面積至少要能放最大立方體
    # 高度為所有立方體邊長和
    max_side = max(cubes)
    total_height = sum(cubes)

    res = []
    for __ in range(m):
        w, l, h = map(int, input().split())
        # 盒子底面必須能放下最大立方體（邊長 max_side）
        # 盒子高度必須能放下所有立方體堆疊高度 total_height
        if (w >= max_side and l >= max_side and h >= total_height) or (w >= max_side and h >= max_side and l >= total_height) or (l >= max_side and h >= max_side and w >= total_height):
            # 盒子可以旋轉，故三個維度中任兩個維度要能放最大立方體邊長，剩下的維度要能放總高度
            # 只要存在一種排列方式符合即可
            res.append('1')
        else:
            res.append('0')
    print(''.join(res))