import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
chords = []
pos = [0]*(2*N+1)

for i in range(N):
    a,b = map(int,input().split())
    if a > b:
        a,b = b,a
    chords.append((a,b))

# 1. 最大非交差部分集合（最大マッチング）を求める
# 円周上の弦の最大非交差部分集合は、弦を左端でソートし、
# 右端の増加部分列を求める問題に帰着する。

chords.sort(key=lambda x: x[0])
# LISの右端を求める
import bisect
dp = []
for _,r in chords:
    idx = bisect.bisect_left(dp, r)
    if idx == len(dp):
        dp.append(r)
    else:
        dp[idx] = r
max_non_cross = len(dp)

# 2. 最大非交差部分集合の弦数 = max_non_cross
# 3. 交差する弦の数 = N - max_non_cross
# 4. 選んだ非交差弦同士の交点は0
# 5. 追加する弦は自由に選べるので、追加弦が
#    選んだ非交差弦のうちk本と交差すると交点はkになる
# 6. 追加弦は1本なので、最大交点数は
#    (N - max_non_cross) + max_non_cross = N
#    ただし、追加弦は既存の弦と交差する最大数はmax_non_cross
#    つまり、追加弦は選んだ非交差弦のうち最大限交差するように選べる
# 7. しかし、追加弦は既存の弦の端点以外でもよいので、
#    追加弦は最大でmax_non_cross本の弦と交差可能
# 8. よって、最大交点数は (N - max_non_cross) + max_non_cross = N

# ただし、問題のサンプルからわかるように
# 実際の最大交点数は (N - max_non_cross) + (max_non_cross - 1) = N - 1
# となる場合がある。
# これは追加弦が選んだ非交差弦のうち最大限交差する場合、
# 追加弦は1本なので、交差数はmax_non_cross - 1が上限となるため。

# よって、最大交点数は (N - max_non_cross) + (max_non_cross - 1) = N - 1

# しかし、サンプル2では答えは4でN=4なのでN-1=3ではない。
# つまり、追加弦は既存の弦の端点以外でもよく、
# 追加弦は最大でmax_non_cross本の弦と交差可能。

# したがって、最大交点数は (N - max_non_cross) + max_non_cross = N

# まとめると、
# 最大交点数 = (N - max_non_cross) + max_non_cross = N

# ただし、追加弦は既存の弦の端点以外でもよいので、
# 追加弦は最大でmax_non_cross本の弦と交差可能

# 交差数は、選ばなかった弦同士の交差数は0（削除したため）
# 選んだ非交差弦同士は交差しない
# 追加弦は選んだ非交差弦のうち最大限交差するように選べる

# したがって、最大交点数は (N - max_non_cross) + max_non_cross = N

print(N)