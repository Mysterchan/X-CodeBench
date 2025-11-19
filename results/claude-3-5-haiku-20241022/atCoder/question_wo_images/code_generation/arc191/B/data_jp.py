def solve(N, K):
    # X ^ N == X % N を満たすXを見つける
    # X = qN + r (0 <= r < N) と表すと、X % N = r
    # X ^ N = (qN + r) ^ N が r と等しい必要がある
    
    # Nのビット長を取得
    bit_len = N.bit_length()
    
    # 相性の良い数を格納するリスト
    compatible = []
    
    # qの値を試す (0から十分大きい値まで)
    # X = qN + r で、r < N なので、q を増やしていく
    # ただし、効率的に探索するため、ビットパターンを考慮
    
    # X ^ N = X % N
    # X = qN + r とすると、
    # (qN + r) ^ N = r
    
    # 効率的な方法: X を N の倍数 + 余りの形で考える
    # X = qN + r で、0 <= r < N
    # (qN + r) ^ N = r を満たす必要がある
    
    # ビット演算の性質から、qN ^ N = qN ^ N
    # (qN + r) ^ N = (qN ^ N) ^ r (一般には成り立たないが、特定の条件下で)
    
    # より直接的なアプローチ:
    # Xを小さい順に生成していく
    # X = qN + r の形で、qとrを変えながら条件をチェック
    
    # 最大でも2^30程度のqまでチェックすれば十分
    max_q = min(K * 2, 1 << (31 - bit_len + 1)) if bit_len < 31 else K * 2
    
    for q in range(max_q):
        base = q * N
        for r in range(N):
            X = base + r
            if X > 0 and (X ^ N) == r:
                compatible.append(X)
                if len(compatible) >= K:
                    compatible.sort()
                    return compatible[K - 1]
    
    if len(compatible) >= K:
        compatible.sort()
        return compatible[K - 1]
    else:
        return -1

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(solve(N, K))