import sys
import threading
def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    P = list(map(int, input().split()))
    # Fenwick Tree for counts of empty slots
    size = N
    tree = [0] * (size + 1)
    # initialize tree with all ones: tree[i] = i & -i
    for i in range(1, size + 1):
        tree[i] = i & -i
    def fenw_add(i, delta):
        # add delta at position i
        while i <= size:
            tree[i] += delta
            i += i & -i
    # find smallest idx such that prefix sum >= k
    def fenw_kth(k):
        idx = 0
        bit_mask = 1 << (size.bit_length() - 1)
        while bit_mask:
            t = idx + bit_mask
            if t <= size and tree[t] < k:
                idx = t
                k -= tree[t]
            bit_mask >>= 1
        return idx + 1
    ans = [0] * (size + 1)
    # process from N down to 1
    for i in range(N, 0, -1):
        k = P[i-1]
        pos = fenw_kth(k)
        ans[pos] = i
        # mark pos as filled (remove from empty slots)
        fenw_add(pos, -1)
    # output
    out = sys.stdout
    out.write(" ".join(map(str, ans[1:])))
if __name__ == "__main__":
    main()