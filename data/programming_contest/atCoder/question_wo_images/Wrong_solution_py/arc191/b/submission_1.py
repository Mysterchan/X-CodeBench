def solve():
    N, K = map(int, input().split())
    zero_bits = []
    i = 0
    while 1 << i <= N:
        if (N >> i) & 1 == 0:
            zero_bits.append(i)
        i += 1

    K -= 1
    if 1 << len(zero_bits) < K:
        print(-1)
        return
    for i, b in enumerate(zero_bits):
        if (K >> i) & 1:
            N |= 1 << b
    print(N)

T = int(input())
for _ in range(T): solve()