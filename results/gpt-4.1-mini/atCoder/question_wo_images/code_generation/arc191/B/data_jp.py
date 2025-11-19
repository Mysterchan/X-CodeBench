import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    # 条件: X XOR N = X % N
    # X = q*N + r (0 <= r < N)
    # X XOR N = r
    # (q*N + r) XOR N = r
    # (q*N) XOR N XOR r = r
    # (q*N) XOR N = 0
    # (q*N) XOR N = (q*N) + N - 2*((q*N) & N)
    # 0 = (q*N) + N - 2*((q*N) & N)
    # 2*((q*N) & N) = (q*N) + N
    # 2*((q*N) & N) - (q*N) = N
    # (q*N) & N = (N + q*N)/2
    # 2*((q*N) & N) = N + q*N
    # 2*((q*N) & N) - q*N = N
    # 2*((q*N) & N) - q*N = N

    # ここで、q*N と N のビットANDは N のビットの位置に依存する。
    # N のビットが立っている位置を考えると、q*N のビットは q のビットを N のビット位置にシフトしたもの。
    # q*N & N = N & (q*N) = N & (q*N)
    # N のビットが立っている位置に q*N のビットが立っている必要がある。

    # 解析すると、N のビットが立っている位置に q のビットが立っていないと成り立たない。
    # つまり、q のビットは N のビットが立っていない位置にしか立てない。

    # よって、q & N = 0 である必要がある。

    # q & N = 0 の q の個数は 2^{bit_count(0ビットの数)} である。

    # K 番目に小さい X は q と r で表せる。
    # r = X % N = X XOR N
    # r は 0 <= r < N で、X XOR N = r なので、X = q*N + r
    # q & N = 0
    # q のビットは N のビットが立っていない位置にしか立てない。

    # q のビットは N の0ビットの位置に対応し、q の値はそのビットで表される。
    # K 番目に小さい X は q = K-1 の q & N = 0 を満たす q の中での K-1 番目の値。

    # q のビットは N の0ビットの位置にしか立てないので、
    # K-1 を N の0ビットの位置にビットを埋め込むことで q を復元できる。

    # まず N のビット長を求める
    bit_len = N.bit_length()
    zero_positions = []
    for i in range(bit_len):
        if (N & (1 << i)) == 0:
            zero_positions.append(i)

    # q の最大値は 2^{len(zero_positions)} - 1
    max_q = (1 << len(zero_positions)) - 1
    if K - 1 > max_q:
        print(-1)
        continue

    q = 0
    k = K - 1
    for i, pos in enumerate(zero_positions):
        if (k >> i) & 1:
            q |= (1 << pos)

    # X = q*N + r
    # r = X XOR N = X % N = r
    # r = X XOR N = r
    # r = X % N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r
    # r = X XOR N = r

    # r = X XOR N = r
    # r = X % N
    # X XOR N = r
    # X = q*N + r
    # (q*N + r) XOR N = r
    # (q*N) XOR N XOR r = r
    # (q*N) XOR N = 0
    # これは q & N = 0 で満たされているので r = 0

    # よって r = 0
    r = 0
    X = q * N + r
    print(X)