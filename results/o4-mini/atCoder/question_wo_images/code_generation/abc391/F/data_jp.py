import sys
import threading
def main():
    import sys
    import heapq

    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    B = [int(next(it)) for _ in range(N)]
    C = [int(next(it)) for _ in range(N)]

    # Sort in descending order
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # We'll do a best‐first search in the 3D index space (i,j,k),
    # keeping a max‐heap of (value, code) with code packing (i,j,k) into one integer.
    #
    # code = (i << 36) | (j << 18) | k
    # to unpack:
    #   i = code >> 36
    #   j = (code >> 18) & mask
    #   k = code & mask
    #
    # N <= 2e5 < 2^18, so 18 bits per index is enough.

    mask = (1 << 18) - 1

    def pack(i, j, k):
        return (i << 36) | (j << 18) | k

    def unpack(code):
        i = code >> 36
        j = (code >> 18) & mask
        k = code & mask
        return i, j, k

    # Initial state (0,0,0)
    # value = A[0]*B[0] + B[0]*C[0] + C[0]*A[0]
    v0 = A[0]*B[0] + B[0]*C[0] + C[0]*A[0]
    code0 = pack(0, 0, 0)

    # max‐heap by storing negative values
    heap = [(-v0, code0)]
    visited = set()
    visited.add(code0)

    heappush = heapq.heappush
    heappop = heapq.heappop

    ans = None
    for _ in range(K):
        negv, code = heappop(heap)
        ans = -negv
        i, j, k = unpack(code)
        # push neighbors
        ni = i + 1
        if ni < N:
            c2 = pack(ni, j, k)
            if c2 not in visited:
                visited.add(c2)
                v2 = A[ni]*B[j] + B[j]*C[k] + C[k]*A[ni]
                heappush(heap, (-v2, c2))
        nj = j + 1
        if nj < N:
            c2 = pack(i, nj, k)
            if c2 not in visited:
                visited.add(c2)
                v2 = A[i]*B[nj] + B[nj]*C[k] + C[k]*A[i]
                heappush(heap, (-v2, c2))
        nk = k + 1
        if nk < N:
            c2 = pack(i, j, nk)
            if c2 not in visited:
                visited.add(c2)
                v2 = A[i]*B[j] + B[j]*C[nk] + C[nk]*A[i]
                heappush(heap, (-v2, c2))

    print(ans)

if __name__ == "__main__":
    main()