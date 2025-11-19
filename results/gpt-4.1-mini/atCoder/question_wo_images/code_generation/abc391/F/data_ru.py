import sys
import heapq

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Sort arrays descending to get largest sums first
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # We want to find the K-th largest value of:
    # A[i]*B[j] + B[j]*C[k] + C[k]*A[i]
    # = (A[i] + C[k]) * B[j] + C[k]*A[i]
    # But this is complicated to separate fully.
    #
    # Instead, consider the expression as:
    # A[i]*B[j] + B[j]*C[k] + C[k]*A[i]
    # = B[j]*(A[i] + C[k]) + C[k]*A[i]
    #
    # For fixed i,k, define:
    # X = A[i] + C[k]
    # Y = A[i]*C[k]
    #
    # Then value = B[j]*X + Y
    #
    # For each pair (i,k), the values over j are:
    # B[j]*X + Y, j=1..N
    #
    # We want the top K values over all triples (i,j,k).
    #
    # Approach:
    # 1) Generate top K pairs (i,k) by A[i]+C[k] and A[i]*C[k].
    #    Since N can be large, we cannot generate all N^2 pairs.
    #    But we can generate top K pairs of (A[i]+C[k], A[i]*C[k]) using a heap.
    #
    # 2) For each such pair, generate top K values over B[j]:
    #    values = B[j]*X + Y, j=1..N
    #    Since B is sorted descending, values are descending in j.
    #
    # 3) Merge all these sequences to get top K values overall.
    #
    # Implementation details:
    # - Generate top K pairs (i,k) by (A[i]+C[k], A[i]*C[k]) using a max heap.
    # - For each pair, we have a sequence over j: B[j]*X + Y, j=0..N-1 descending.
    # - Use a heap to merge these sequences to get top K values overall.
    #
    # Complexity:
    # - Generating top K pairs (i,k) using a heap: O(K log K)
    # - Merging K sequences each with up to N elements is too large.
    #   But we only need top K values overall.
    #   So we only push next element when we pop one, total O(K log K).
    #
    # This approach is feasible for K up to 5*10^5.

    # Step 1: Generate top K pairs (i,k) by (A[i]+C[k], A[i]*C[k])
    # Use a max heap for pairs (sum, product, i, k)
    visited = set()
    heap_pairs = []
    # Start from (0,0)
    i, k = 0, 0
    initial_sum = A[i] + C[k]
    initial_prod = A[i] * C[k]
    heapq.heappush(heap_pairs, (-(initial_sum), -(initial_prod), i, k))
    visited.add((i, k))

    top_pairs = []
    for _ in range(min(K, N*N)):
        if not heap_pairs:
            break
        s_neg, p_neg, i, k = heapq.heappop(heap_pairs)
        s = -s_neg
        p = -p_neg
        top_pairs.append((s, p))
        # Push next pairs (i+1,k) and (i,k+1) if not visited
        if i + 1 < N and (i+1, k) not in visited:
            ns = A[i+1] + C[k]
            np = A[i+1] * C[k]
            heapq.heappush(heap_pairs, (-ns, -np, i+1, k))
            visited.add((i+1, k))
        if k + 1 < N and (i, k+1) not in visited:
            ns = A[i] + C[k+1]
            np = A[i] * C[k+1]
            heapq.heappush(heap_pairs, (-ns, -np, i, k+1))
            visited.add((i, k+1))

    # Step 2 and 3: For each pair (X=s, Y=p), generate sequence over B:
    # values_j = B[j]*X + Y, j=0..N-1 descending since B sorted descending and X>=0
    # We merge these sequences to get top K values overall.

    # We will use a heap to merge sequences:
    # Each element in heap: (value, pair_index, j)
    # Start with j=0 for each pair

    heap_values = []
    for idx, (X, Y) in enumerate(top_pairs):
        val = B[0]*X + Y
        heapq.heappush(heap_values, ( -val, idx, 0))

    answer = None
    for _ in range(K):
        val_neg, idx, j = heapq.heappop(heap_values)
        answer = -val_neg
        # Push next element in sequence idx if exists
        if j + 1 < N:
            X, Y = top_pairs[idx]
            val_next = B[j+1]*X + Y
            heapq.heappush(heap_values, (-val_next, idx, j+1))

    print(answer)

if __name__ == "__main__":
    main()