import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    LR = [tuple(map(int, input().split())) + (i,) for i in range(N)]
    # LR: (L_i, R_i, i)

    # 交差判定:
    # 人iと人jの区間(L_i,R_i)と(L_j,R_j)が交差するとは、
    # (L_i < L_j < R_i < R_j) または (L_j < L_i < R_j < R_i)
    # 交差する人同士は席の順序を逆にしないと不満度が増える。
    # つまり、交差する人同士は席順で逆転してはいけない。

    # 交差関係をグラフの辺として考え、辺 (i,j) は「iとjは交差している」ことを示す。
    # 交差している人同士は席順で逆転しないようにしなければならない。

    # 交差している人同士の席順は、L_iの昇順に並べるのが不満度最小かつ辞書順最小になる。

    # したがって、交差している人同士はL_iの昇順で並べる制約がある。
    # これを満たす席順Pを求める。

    # 交差している人同士はL_iの昇順で並べる必要があるので、
    # 交差している人同士の部分集合ごとにL_iの昇順で並べる。

    # 交差していない人同士は席順に制約なし。
    # つまり、交差グラフの連結成分ごとにL_iの昇順で並べ、
    # それらの成分を辞書順最小に並べる。

    # 連結成分の並べ方は、各成分の最小L_iをキーに昇順に並べると辞書順最小になる。

    # 実装手順:
    # 1. 交差判定でグラフを作る
    # 2. 連結成分を求める
    # 3. 各成分内をL_i昇順に並べる
    # 4. 成分を最小L_iで昇順に並べる
    # 5. それらを連結して答えとする

    # 交差判定はO(N^2)で可能(N<=500)

    graph = [[] for _ in range(N)]
    for i in range(N):
        L1, R1, _ = LR[i]
        for j in range(i+1, N):
            L2, R2, _ = LR[j]
            # 交差判定
            if (L1 < L2 < R1 < R2) or (L2 < L1 < R2 < R1):
                graph[i].append(j)
                graph[j].append(i)

    visited = [False]*N
    components = []

    def dfs(s):
        stack = [s]
        comp = []
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            comp.append(u)
            for w in graph[u]:
                if not visited[w]:
                    stack.append(w)
        return comp

    for i in range(N):
        if not visited[i]:
            comp = dfs(i)
            components.append(comp)

    # 各成分内をL_i昇順に並べる
    for i in range(len(components)):
        components[i].sort(key=lambda x: LR[x][0])

    # 成分を最小L_iで昇順に並べる
    components.sort(key=lambda comp: LR[comp[0]][0])

    # 答えを作る
    ans = []
    for comp in components:
        ans.extend(comp)

    # ansは人のインデックス(0-based)
    # 出力は1-based
    print(*[x+1 for x in ans])