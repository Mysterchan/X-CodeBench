import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    # Count number of set bits in n
    c = bin(n).count('1')
    total = 1 << c  # total compatible numbers

    if k > total:
        print(-1)
        continue

    # Positions of set bits in n
    set_bits = []
    for i in range(31):
        if (n >> i) & 1:
            set_bits.append(i)

    # Construct the k-th compatible number
    # The compatible numbers correspond to all subsets of set bits of n,
    # with bits outside n's set bits fixed as in n.
    # The k-th smallest corresponds to k-1 as bitmask over set bits.
    k -= 1
    res = n
    for i, pos in enumerate(set_bits):
        if (k >> i) & 1:
            res ^= (1 << pos)
    print(res)