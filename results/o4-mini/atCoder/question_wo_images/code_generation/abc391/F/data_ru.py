import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    K = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    B = [int(next(it)) for _ in range(n)]
    C = [int(next(it)) for _ in range(n)]
    # sort descending
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    # special case n == 1
    if n == 1:
        v = A[0]*B[0] + B[0]*C[0] + C[0]*A[0]
        print(v)
        return
    # compute bit widths for encoding triples
    bits = max(1, (n-1).bit_length())
    SK = 1
    SJ = 1 << bits
    SI = 1 << (2 * bits)
    # max-heap via min-heap of negative values
    import heapq
    heap = []
    visited = set()
    # initial triple (0,0,0)
    key0 = 0
    f0 = A[0]*B[0] + B[0]*C[0] + C[0]*A[0]
    visited.add(key0)
    heapq.heappush(heap, (-f0, key0))
    cnt = 0
    out = None
    while heap:
        negf, key = heapq.heappop(heap)
        f = -negf
        cnt += 1
        if cnt == K:
            out = f
            break
        # decode i,j,k
        # i = key >> (2*bits)
        # j = (key >> bits) & ((1<<bits)-1)
        # k = key & ((1<<bits)-1)
        i = key >> (2 * bits)
        tmp = key - (i << (2 * bits))
        j = tmp >> bits
        k = tmp - (j << bits)
        # neighbor (i+1, j, k)
        ni = i + 1
        if ni < n:
            k1 = key + SI
            if k1 not in visited:
                visited.add(k1)
                # compute f
                a = A[ni]; b = B[j]; c = C[k]
                nf = a*b + b*c + c*a
                heapq.heappush(heap, (-nf, k1))
        # neighbor (i, j+1, k)
        nj = j + 1
        if nj < n:
            k2 = key + SJ
            if k2 not in visited:
                visited.add(k2)
                a = A[i]; b = B[nj]; c = C[k]
                nf = a*b + b*c + c*a
                heapq.heappush(heap, (-nf, k2))
        # neighbor (i, j, k+1)
        nk = k + 1
        if nk < n:
            k3 = key + SK
            if k3 not in visited:
                visited.add(k3)
                a = A[i]; b = B[j]; c = C[nk]
                nf = a*b + b*c + c*a
                heapq.heappush(heap, (-nf, k3))
    # print result
    print(out)

if __name__ == "__main__":
    main()