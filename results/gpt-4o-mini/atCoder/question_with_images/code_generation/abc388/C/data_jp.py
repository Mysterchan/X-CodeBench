def count_mirror_mochi(n, sizes):
    count = 0
    j = 0

    for i in range(n):
        while j < n and sizes[j] <= 2 * sizes[i]:
            j += 1
        count += (j - i - 1)

    return count

# 入力の読み込み
n = int(input())
sizes = list(map(int, input().split()))

# 鏡餅の種類数を計算して出力
print(count_mirror_mochi(n, sizes))