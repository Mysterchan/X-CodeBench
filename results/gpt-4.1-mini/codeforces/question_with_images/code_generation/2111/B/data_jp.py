import sys
input = sys.stdin.readline

# フィボナッチ数列の定義に従い、f_1=1, f_2=2, f_i=f_{i-1}+f_{i-2}
# n <= 10 なので事前に計算しておく
MAX_N = 10
fib = [0]*(MAX_N+1)
fib[1] = 1
fib[2] = 2
for i in range(3, MAX_N+1):
    fib[i] = fib[i-1] + fib[i-2]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cubes = fib[1:n+1]

    # キューブは大きい順に積む必要があるので降順に並べる
    cubes.sort(reverse=True)

    # キューブの最大辺長
    max_side = cubes[0]
    # キューブの高さ合計
    total_height = sum(cubes)

    res = []
    for __ in range(m):
        w, l, h = map(int, input().split())
        # 箱の底面はw*lで、キューブの最大辺長以下でなければならない
        # キューブは辺に平行に置くので、底面のどちらかの辺がmax_side以上必要
        # つまり、箱の幅と長さのどちらかがmax_side以上であること
        # また高さは積み重ねた高さの合計以上必要
        if (w >= max_side and l >= max_side) and h >= total_height:
            res.append('1')
        else:
            res.append('0')
    print(''.join(res))