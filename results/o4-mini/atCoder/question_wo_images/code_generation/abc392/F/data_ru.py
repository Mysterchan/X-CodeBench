import sys
import threading
def main():
    import sys
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    P = list(map(int, data[1:1+n]))
    size = n
    tree = [1] * (size + 1)
    for i in range(1, size + 1):
        j = i + (i & -i)
        if j <= size:
            tree[j] += tree[i]
    A = [0] * size
    bitmask = 1 << (size.bit_length() - 1)
    for idx_i in range(size, 0, -1):
        k = P[idx_i - 1]
        pos = 0
        b = bitmask
        while b:
            nxt = pos + b
            if nxt <= size and tree[nxt] < k:
                k -= tree[nxt]
                pos = nxt
            b >>= 1
        idx = pos + 1
        A[idx - 1] = idx_i
        j = idx
        while j <= size:
            tree[j] -= 1
            j += (j & -j)
    out = ' '.join(map(str, A))
    sys.stdout.write(out)

if __name__ == "__main__":
    main()