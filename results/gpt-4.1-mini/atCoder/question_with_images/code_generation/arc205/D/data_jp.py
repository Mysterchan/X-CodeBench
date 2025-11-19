import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    p = list(map(int, input().split())) if N > 1 else []

    # 木の構築
    children = [[] for _ in range(N+1)]
    for i, parent in enumerate(p, start=2):
        children[parent].append(i)

    # dp[u][0]: uを黒にしない場合の最大ペア数
    # dp[u][1]: uを黒にする場合の最大ペア数
    # uを黒にする場合はuの子は黒にできない（ペアにできない）
    # uを黒にしない場合は子は自由にできる
    def dfs(u):
        dp0 = 0  # uを黒にしない場合
        dp1 = 0  # uを黒にする場合

        # 子のdpを集める
        child_dp = []
        for c in children[u]:
            c0, c1 = dfs(c)
            child_dp.append((c0, c1))

        # uを黒にしない場合は子は自由にできるので子の最大値を足す
        for c0, c1 in child_dp:
            dp0 += max(c0, c1)

        # uを黒にする場合は子は黒にできないので子はdp[c][0]のみ
        for c0, _ in child_dp:
            dp1 += c0

        # uを黒にする場合はuはペアの片方になるので
        # uのペア相手はuの祖先でも子孫でもない白の頂点
        # 問題の条件よりuを黒にする場合はuの子は黒にできないが
        # uの親や兄弟は黒にできる
        # しかしuを黒にするだけではペアはできない
        # ペアは(u,v)でu<vかつuはvの祖先でない
        # このdpは最大独立集合のような考え方で
        # 実際のペア数はdpの合計の半分になる

        # ここでdp1はuを黒にした場合の最大ペア数ではなく
        # uを黒にした場合の最大「黒頂点数」のようなもの
        # なのでdpは黒頂点数の最大値を求めている

        # したがって、uを黒にする場合はu自身が黒頂点1つ分
        # dp1 += 1
        dp1 += 1

        return dp0, dp1

    dp0, dp1 = dfs(1)
    # dpは黒頂点数の最大値
    # ペアは黒頂点2つで1ペアなので最大ペア数は黒頂点数//2
    ans = max(dp0, dp1) // 2
    results.append(str(ans))

print('\n'.join(results))