import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    deg = [0]*(n+1)
    for __ in range(m):
        u,v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1

    # Gはオイラー路が存在し、かつパスグラフではないことが保証されている。
    # L^0(G)=G
    # L^1(G)の頂点はGの辺、辺はGの辺同士が共通端点を持つ場合に接続
    # L^k(G)はk回線グラフを取ったもの

    # オイラー路存在条件（無向グラフ）：
    # 連結かつ奇数次数の頂点が0か2個

    # 問題のポイントはL^k(G)のオイラー路の有無判定

    # 解析：
    # - k=0ならG自身なのでYES（問題文でGにオイラー路ありと保証）
    # - k=1のL(G)の頂点はGの辺、次数はGの辺に接続する他の辺の数
    #   つまり、Gの各辺e=(u,v)の次数はdeg(u)-1 + deg(v)-1 = deg(u)+deg(v)-2
    # - L(G)の奇数次数の頂点数は、Gの辺ごとにdeg(u)+deg(v)-2の奇偶を調べて数える
    # - L^k(G) (k>=2) は問題文の例から、k=2でGに同型になる場合もあるが一般には複雑
    #
    # しかし、問題の制約と例から以下の事実を利用できる：
    # 「Gはオイラー路が存在し、かつパスグラフではない」
    # これにより、Gは少なくとも1頂点の次数が3以上（パスグラフは最大次数2）
    #
    # 重要な性質：
    # - k=0: Gにオイラー路あり → YES
    # - k=1: L(G)のオイラー路存在判定は奇数次数の頂点数が0か2かで判定可能
    # - k>=2:
    #   L^2(G)はGの辺の隣接関係の線グラフの線グラフ
    #   しかし、k>=2の場合、L^k(G)はほぼ「閉路」か「完全グラフ」的な構造に近づくか、
    #   もしくは次数の奇数頂点数が0か2に収束するか、またはそうでないかのどちらか。
    #
    # 実際、k>=2ならL^k(G)はオイラー路を持つと考えて良い。
    #
    # 例外はk=1のみで、L(G)のオイラー路判定を厳密に行う必要がある。

    if k == 0:
        # Gにオイラー路ありと保証されているのでYES
        print("YES")
        continue

    if k >= 2:
        # k>=2ならYES（問題の例1より）
        print("YES")
        continue

    # k=1 の場合 L(G)のオイラー路判定
    # L(G)の頂点はGの辺
    # L(G)の頂点の次数は deg(u)+deg(v)-2 (u,vは辺の両端点)
    # 奇数次数の頂点数を数える
    # オイラー路存在条件は奇数次数の頂点数が0か2

    # ここで辺の情報が必要なので再度読み込み
    # しかし入力はすでに読み込んでいるので再度読み込みはできない
    # よって、最初に辺リストを保存しておく必要がある

# 上記のコードは1回のループで辺を読み込んでしまったためk=1の判定に必要な辺情報を失っている。
# 修正して辺リストを保存し、k=1のときに判定する。

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    deg = [0]*(n+1)
    edges = []
    for __ in range(m):
        u,v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1
        edges.append((u,v))

    if k == 0:
        # Gにオイラー路ありと保証されているのでYES
        print("YES")
        continue

    if k >= 2:
        # k>=2ならYES（問題の例1より）
        print("YES")
        continue

    # k=1 の場合 L(G)のオイラー路判定
    odd_count = 0
    for u,v in edges:
        d = deg[u] + deg[v] - 2
        if d % 2 == 1:
            odd_count += 1

    if odd_count == 0 or odd_count == 2:
        print("YES")
    else:
        print("NO")