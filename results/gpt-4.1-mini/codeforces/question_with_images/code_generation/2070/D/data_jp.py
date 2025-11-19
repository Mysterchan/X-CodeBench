import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
MOD = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    # 親配列から子リストを作成
    children = [[] for __ in range(n+1)]
    for i, par in enumerate(p, start=2):
        children[par].append(i)

    # 根は1
    # dp[v]: 頂点vを訪れる有効な頂点列の数
    # 根は自由に子を選べるので、dp[v] = 1 + ∏(1 + dp[c]) (cはvの子)
    # 1は「vだけ訪れる列」
    # 子の部分は、子の訪問列を選ぶか選ばないかの組み合わせ

    def dfs(v):
        res = 1
        for c in children[v]:
            res *= (1 + dfs(c))
            res %= MOD
        return res

    ans = dfs(1) % MOD
    print(ans)