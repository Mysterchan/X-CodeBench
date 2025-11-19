import sys
import threading
def main():
    import sys, heapq
    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Sort descending
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # Max-heap via negative values
    hq = []
    # code(i,j,k) = (i<<36)|(j<<18)|k, since N < 2^18
    VIS = set()
    def code(i,j,k):
        return (i<<36)|(j<<18)|k

    # initial triple (0,0,0)
    val000 = A[0]*B[0] + B[0]*C[0] + C[0]*A[0]
    heapq.heappush(hq, (-val000, 0, 0, 0))
    VIS.add(code(0,0,0))

    ans = None
    for _ in range(K):
        negv, i, j, k = heapq.heappop(hq)
        ans = -negv
        # expand neighbors
        ni = i+1
        if ni < N:
            c = code(ni,j,k)
            if c not in VIS:
                VIS.add(c)
                v = A[ni]*B[j] + B[j]*C[k] + C[k]*A[ni]
                heapq.heappush(hq, (-v, ni, j, k))
        nj = j+1
        if nj < N:
            c = code(i,nj,k)
            if c not in VIS:
                VIS.add(c)
                v = A[i]*B[nj] + B[nj]*C[k] + C[k]*A[i]
                heapq.heappush(hq, (-v, i, nj, k))
        nk = k+1
        if nk < N:
            c = code(i,j,nk)
            if c not in VIS:
                VIS.add(c)
                v = A[i]*B[j] + B[j]*C[nk] + C[nk]*A[i]
                heapq.heappush(hq, (-v, i, j, nk))

    print(ans)

if __name__ == "__main__":
    main()