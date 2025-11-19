import sys
import heapq

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # まず A_i * B_j + B_j * C_k + C_k * A_i = (A_i + C_k) * B_j + C_k * A_i
    # しかしこの形は複雑なので、元の形のまま考える。
    # ただし、計算量を減らすために、まず A_i * B_j の組み合わせを考え、
    # それに C_k * (B_j + A_i) を加える形に分解できる。
    # しかしそれも複雑なので、以下の方法をとる。

    # 1. AとBの組み合わせで A_i*B_j を計算し、上位K個を求める。
    # 2. それらの上位K個に対して、C_kを加えて計算する。
    # 3. つまり、(A_i*B_j) + B_j*C_k + C_k*A_i = A_i*B_j + C_k*(B_j + A_i)
    # ここで、B_j + A_i は固定なので、C_kを掛けて加算する。

    # まず、A_i*B_j の上位K個を求める。
    # Nが大きいので、全探索は無理。ヒープを使って上位K個を求める。

    # A, Bは降順ソート済み
    # (i,j)の組み合わせで A[i]*B[j] の上位K個を求める

    heap = []
    visited = set()
    # heapは最大ヒープにしたいので、値のマイナスを入れる
    # 初期は (A[0]*B[0], 0, 0)
    heapq.heappush(heap, (-(A[0]*B[0]), 0, 0))
    visited.add((0,0))

    AB_top = []
    for _ in range(min(K, N*N)):
        val, i, j = heapq.heappop(heap)
        AB_top.append((-val, i, j))
        if i+1 < N and (i+1, j) not in visited:
            heapq.heappush(heap, (-(A[i+1]*B[j]), i+1, j))
            visited.add((i+1, j))
        if j+1 < N and (i, j+1) not in visited:
            heapq.heappush(heap, (-(A[i]*B[j+1]), i, j+1))
            visited.add((i, j+1))

    # 次に、C_k*(B_j + A_i) を加算する
    # B_j + A_i は B[j] + A[i]
    # これも上位K個を求める必要があるが、N^2は大きいので同様にヒープで上位K個を求める

    # まず、B_j + A_i の組み合わせの上位K個を求める
    # A, Bは降順なので、B_j + A_i も降順で探索可能

    heap = []
    visited = set()
    heapq.heappush(heap, (-(A[0] + B[0]), 0, 0))
    visited.add((0,0))

    AB_sum_top = []
    for _ in range(min(K, N*N)):
        val, i, j = heapq.heappop(heap)
        AB_sum_top.append(-val)
        if i+1 < N and (i+1, j) not in visited:
            heapq.heappush(heap, (-(A[i+1] + B[j]), i+1, j))
            visited.add((i+1, j))
        if j+1 < N and (i, j+1) not in visited:
            heapq.heappush(heap, (-(A[i] + B[j+1]), i, j+1))
            visited.add((i, j+1))

    # Cは降順ソート済み

    # ここで、求めたい値は
    # A_i*B_j + C_k*(B_j + A_i)
    # AB_top: (A_i*B_j, i, j)
    # AB_sum_top: B_j + A_i の上位K個（ただしi,jは異なる組み合わせなので注意）
    # しかし、AB_topとAB_sum_topは別の組み合わせであり、i,jが一致しない可能性がある。
    # なので、AB_sum_topはB_j + A_iの値の上位K個のリストとして使うのは誤り。

    # したがって、AB_sum_topは使えない。

    # 別のアプローチを考える。

    # 元の式は A_i*B_j + B_j*C_k + C_k*A_i
    # = A_i*B_j + C_k*(B_j + A_i)

    # ここで、(B_j + A_i) は i,jの組み合わせに依存する。
    # つまり、i,j,kの3重ループで計算する必要がある。

    # しかしN^3は無理。

    # 代わりに、A_i*B_j と B_j + A_i の組み合わせを同時に扱う必要がある。

    # そこで、(i,j)の組み合わせを上位K個に絞る。
    # AB_topは (A_i*B_j, i, j) の上位K個。

    # これらの組み合わせに対して、C_kを掛けて加算する。

    # つまり、値は AB_top_val + C_k * (B_j + A_i)

    # ここで、(B_j + A_i) は i,jで決まる。

    # なので、AB_topに (val, i, j) と (B_j + A_i) をセットで持つ。

    # その後、C_kを掛けて加算する。

    # これをkについてもヒープで上位K個を求める。

    # 具体的には、(AB_top_val + C[0]*(B_j + A_i), idx_ab=0, idx_c=0) を初期にヒープに入れ、
    # 次に idx_cを増やしていく。

    # これで上位K個を求める。

    # 実装：

    # AB_top: list of (val, i, j)
    # For each, compute B_j + A_i

    # heapに (-value, idx_ab, idx_c) を入れる

    heap = []
    visited = set()

    # precompute B_j + A_i for AB_top
    AB_sum = [B[j] + A[i] for _, i, j in AB_top]

    # 初期化
    # value = AB_top_val + C[0] * AB_sum
    for idx_ab, (val, i, j) in enumerate(AB_top):
        value = val + C[0] * AB_sum[idx_ab]
        heapq.heappush(heap, (-(value), idx_ab, 0))
        visited.add((idx_ab, 0))

    ans = None
    for _ in range(K):
        val, idx_ab, idx_c = heapq.heappop(heap)
        ans = -val
        if idx_c + 1 < N:
            next_val = AB_top[idx_ab][0] + C[idx_c+1] * AB_sum[idx_ab]
            if (idx_ab, idx_c+1) not in visited:
                heapq.heappush(heap, (-(next_val), idx_ab, idx_c+1))
                visited.add((idx_ab, idx_c+1))

    print(ans)

if __name__ == "__main__":
    main()