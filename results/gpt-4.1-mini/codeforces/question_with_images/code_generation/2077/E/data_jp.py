import sys
input = sys.stdin.readline
MOD = 998244353

# 問題の f(b) は、b の最大値が操作回数の最小値であることが知られている（折りたたみと染料の操作で最大値分の操作が必要かつ十分）
# よって f(b) = max(b)
# 求めるのは全ての部分列の max の総和

# ここで、a の長さの合計が 2*10^5 なので O(n^2) は無理
# 部分列の最大値の総和は「部分列の最大値の総和問題」として知られており、
# スタックを用いた単調増加スタックで O(n) で計算可能

# アルゴリズム：
# 1. 単調増加スタックを用意
# 2. i を左から右に走査
# 3. スタックのトップの値が a[i] 以下ならポップしつつ、ポップした要素の影響を減らす
# 4. スタックに (a[i], count) をプッシュし、count は a[i] が最大値となる部分列の数
# 5. 各ステップで a[i] * count を足し合わせていく
# 6. これを全てのテストケースで行い、結果を出力

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    stack = []
    res = 0
    total = 0
    for x in a:
        count = 1
        while stack and stack[-1][0] <= x:
            val, c = stack.pop()
            count += c
            total -= val * c
        stack.append((x, count))
        total += x * count
        res += total
    print(res % MOD)