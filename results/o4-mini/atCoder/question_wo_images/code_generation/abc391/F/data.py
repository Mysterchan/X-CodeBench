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

    # Sort all arrays in descending order
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # A helper to compute the expression value for (i, j, k)
    def val(i, j, k):
        return A[i]*B[j] + B[j]*C[k] + C[k]*A[i]

    # We will run a best-first search on the 3D index space (i, j, k),
    # starting from (0, 0, 0) which gives the maximum value, and each step
    # we can increment i, j, or k to move to a strictly smaller value.
    #
    # Use a max-heap (by pushing negative values) and a visited set to avoid repeats.
    #
    # To compress (i, j, k) in the visited set we pack them into a single integer:
    #   key = (i << 36) | (j << 18) | k
    # since N <= 2e5 < 2^18.

    # The heap stores entries of the form: (-value, i, j, k)
    heap = []
    push = heapq.heappush
    pop = heapq.heappop

    # Visited set, packed indices
    visited = set()

    def pack(i, j, k):
        return (i << 36) | (j << 18) | k

    # Initialize with the top element (0,0,0)
    init_key = pack(0, 0, 0)
    visited.add(init_key)
    push(heap, (-val(0, 0, 0), 0, 0, 0))

    cnt = 0
    answer = None

    while heap:
        neg_v, i, j, k = pop(heap)
        cnt += 1
        # When we've popped the K-th largest, that's our answer
        if cnt == K:
            answer = -neg_v
            break
        # Otherwise, expand its 3 neighbors (i+1,j,k), (i,j+1,k), (i,j,k+1)
        ni = i + 1
        if ni < N:
            key = pack(ni, j, k)
            if key not in visited:
                visited.add(key)
                push(heap, (-val(ni, j, k), ni, j, k))
        nj = j + 1
        if nj < N:
            key = pack(i, nj, k)
            if key not in visited:
                visited.add(key)
                push(heap, (-val(i, nj, k), i, nj, k))
        nk = k + 1
        if nk < N:
            key = pack(i, j, nk)
            if key not in visited:
                visited.add(key)
                push(heap, (-val(i, j, nk), i, j, nk))

    # Print the result
    sys.stdout.write(str(answer))

if __name__ == "__main__":
    main()