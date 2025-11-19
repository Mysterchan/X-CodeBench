import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

N, M = map(int, sys.stdin.readline().split())
Ps = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 各頂点について、M個の順列での位置を記録
pos = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        pos[i][Ps[i][j]-1] = j

# 頂点u,vの間に辺を張れるか判定する関数
# 条件: どの順列においても、u,vの間の弧に他の頂点が入らないこと
# つまり、u,vの間の区間に他の頂点が入らない（交差しない）こと
def can_edge(u, v):
    if u > v:
        u, v = v, u
    for i in range(M):
        pu, pv = pos[i][u], pos[i][v]
        if pu > pv:
            pu, pv = pv, pu
        # 頂点u,vの間に他の頂点が入っていないか
        # 頂点u,vの間の区間に他の頂点が入ると交差する可能性がある
        # つまり、u,vの間の区間に他の頂点が入っているとダメ
        # ここで、u,vの間の区間は[pu+1, pv-1]
        # 他の頂点wのpos[i][w]がこの区間に入っているかチェック
        # ただしwはu,v以外
        # もし入っていたらFalse
        # 逆に、u,vの間の区間に他の頂点が入っていなければTrue
        # これを全てのiで満たす必要がある
        # ここで、u,vの間の区間に他の頂点が入っているかどうかを
        # 頂点wのpos[i][w]で判定する
        # しかしNが最大500なので全頂点チェックしても間に合う
        for w in range(N):
            if w == u or w == v:
                continue
            pw = pos[i][w]
            if pu < pw < pv:
                return False
    return True

# 辺の候補を列挙
edges = []
for u in range(N):
    for v in range(u+1, N):
        if can_edge(u, v):
            edges.append((u, v))

# 辺の候補で作れる木の数を求める問題に帰着
# 頂点数N, 辺集合edgesで、全域木の数を求める
# これは行列木定理を使う

# 行列木定理のためのラプラシアン行列を作成
L = [[0]*N for _ in range(N)]
for u, v in edges:
    L[u][u] += 1
    L[v][v] += 1
    L[u][v] -= 1
    L[v][u] -= 1

# 行列木定理: ラプラシアン行列の任意の1行1列を削除した行列の行列式が
# そのグラフの全域木の数になる

# 行列式をMODで計算する関数
def det_mod(mat, mod):
    n = len(mat)
    res = 1
    for i in range(n):
        pivot = -1
        for j in range(i, n):
            if mat[j][i] % mod != 0:
                pivot = j
                break
        if pivot == -1:
            return 0
        if i != pivot:
            mat[i], mat[pivot] = mat[pivot], mat[i]
            res = (-res) % mod
        res = (res * mat[i][i]) % mod
        inv = pow(mat[i][i], mod-2, mod)
        for j in range(i+1, n):
            if mat[j][i] % mod != 0:
                factor = (mat[j][i] * inv) % mod
                for k in range(i, n):
                    mat[j][k] = (mat[j][k] - factor * mat[i][k]) % mod
    return res % mod

# (N-1)x(N-1)の部分行列を作る
mat = [row[1:] for row in L[1:]]

# 行列式を計算して出力
print(det_mod(mat, MOD))