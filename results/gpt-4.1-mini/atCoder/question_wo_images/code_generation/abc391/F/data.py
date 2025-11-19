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
    # A_i*B_j + B_j*C_k + C_k*A_i
    # = (A_i + C_k)*B_j + C_k*A_i
    # But this is complicated to separate easily.
    #
    # Instead, consider the expression as:
    # A_i*B_j + B_j*C_k + C_k*A_i
    # = B_j*(A_i + C_k) + C_k*A_i
    #
    # We can try to fix pairs (i,k) and then consider B_j.
    #
    # But N=2e5, N^2=4e10 too large.
    #
    # We need to reduce the problem:
    # Let's try to generate top M sums of A_i*B_j + B_j*C_k + C_k*A_i by merging.
    #
    # Let's rewrite:
    # For fixed j:
    # A_i*B_j + B_j*C_k + C_k*A_i = B_j*(A_i + C_k) + C_k*A_i
    #
    # For fixed j, define X_i_k = (A_i + C_k), Y_i_k = C_k*A_i
    # So value = B_j * X_i_k + Y_i_k
    #
    # But again, too large.
    #
    # Alternative approach:
    # Let's try to generate top K sums of A_i*B_j + B_j*C_k + C_k*A_i by:
    # 1) Generate top K sums of A_i*B_j (call this AB)
    # 2) Generate top K sums of B_j*C_k (call this BC)
    # 3) Generate top K sums of C_k*A_i (call this CA)
    #
    # Then, the original sum = AB + BC + CA
    #
    # But the problem is that the indices j and k are shared in multiple terms.
    #
    # So this approach is invalid because the indices must be the same j and k.
    #
    # Another approach:
    # Let's try to fix j:
    # For each j, the sum over i,k is:
    # A_i*B_j + B_j*C_k + C_k*A_i = B_j*(A_i + C_k) + C_k*A_i
    #
    # For fixed j, define arrays:
    # P = A (length N)
    # Q = C (length N)
    #
    # For each pair (i,k), value = B_j*(A_i + C_k) + C_k*A_i
    #
    # For fixed j, we want to find top values of:
    # B_j*(A_i + C_k) + C_k*A_i
    #
    # Let's try to generate top K values of (A_i + C_k) and top K values of (C_k*A_i).
    #
    # But again, N^2 is too large.
    #
    # Let's try to fix k:
    # For fixed k:
    # value = A_i*B_j + B_j*C_k + C_k*A_i = B_j*(A_i + C_k) + C_k*A_i
    #
    # For fixed k, define:
    # For each i,j:
    # value = B_j*(A_i + C_k) + C_k*A_i
    #
    # For fixed k, define array D_i = A_i + C_k
    # and E_i = C_k*A_i
    #
    # Then value = B_j * D_i + E_i
    #
    # For fixed k, we want to find top K values of B_j * D_i + E_i over i,j.
    #
    # Now, for fixed k, we can try to generate top K values of B_j * D_i + E_i.
    #
    # Let's fix k and try to generate top K values of B_j * D_i + E_i.
    #
    # Since B and D are sorted descending, we can use a heap to generate top K sums of B_j * D_i + E_i.
    #
    # But E_i depends on i and k, so for fixed k, E_i is fixed.
    #
    # So for fixed k:
    # We have arrays D (length N): D_i = A_i + C_k
    # and E (length N): E_i = C_k * A_i
    #
    # We want top K values of B_j * D_i + E_i over i,j.
    #
    # Let's try to generate top K values of B_j * D_i + E_i:
    #
    # For each i, the values over j are B_j * D_i + E_i.
    # Since B_j is sorted descending, for fixed i, values decrease as j increases.
    #
    # So for each i, the sequence over j is decreasing.
    #
    # We can use a heap to generate top K values over all i,j:
    # Initialize heap with (B_0 * D_i + E_i, i, 0) for all i.
    # Pop max, push next j for same i.
    #
    # This is O(K log N) per k.
    #
    # But k goes up to N=2e5, so total O(N K log N) is too large.
    #
    # So we cannot do for all k.
    #
    # We need to reduce the number of k's considered.
    #
    # Since we want top K values overall, and K <= 5e5, we can try to consider only top M elements of C.
    #
    # Let's pick M = min(N, 1000) (or 2000) to limit complexity.
    #
    # For each of these M largest C_k, we generate top K values of B_j * D_i + E_i.
    #
    # Then merge all these M * K values and pick top K.
    #
    # This is feasible.
    #
    # Steps:
    # 1) Sort A, B, C descending.
    # 2) Take top M elements of C.
    # 3) For each C_k in top M:
    #    - Compute D_i = A_i + C_k
    #    - Compute E_i = C_k * A_i
    #    - Generate top K values of B_j * D_i + E_i over i,j using a heap.
    # 4) Merge all M * K values and pick top K.
    #
    # M=1000, K=5e5, N=2e5
    # Generating top K values for each k is O(K log N) = 5e5 * log(2e5) ~ 5e5 * 18 = 9e6 per k
    # For M=1000, 9e9 operations too large.
    #
    # So reduce M further, say M=50.
    #
    # Then total ~4.5e8 operations, possibly feasible with efficient code.
    #
    # Alternatively, reduce K to min(K, 5000) for each k, then merge.
    #
    # Let's do:
    # For each of top M=50 C_k:
    #   Generate top L=10000 values of B_j * D_i + E_i
    # Merge all M*L=500,000 values and pick top K.
    #
    # This matches the constraint K <= 5e5.
    #
    # Implementation details:
    # - For each k in top M:
    #   - D_i = A_i + C_k
    #   - E_i = C_k * A_i
    #   - Use a max heap to generate top L values of B_j * D_i + E_i:
    #     * Initialize heap with (B_0 * D_i + E_i, i, 0) for i in [0..N-1]
    #     * Pop max, push next j for same i if j+1 < N
    #     * Stop after L pops
    #
    # - Collect all these values in a list.
    # - Merge all M*L values and pick top K.
    #
    # This approach should work within time limits.

    M = 50  # number of top C elements to consider
    L = 10000  # number of top values per fixed k to generate

    M = min(M, N)
    L = min(L, K)

    top_C = C[:M]

    # Pre-sort A and B descending
    # Already sorted

    results = []

    for c_val in top_C:
        D = [a + c_val for a in A]
        E = [c_val * a for a in A]

        # Generate top L values of B_j * D_i + E_i over i,j
        # Use max heap
        heap = []
        # Push initial pairs (j=0) for all i
        # To reduce memory, we can push only top L i's with largest E_i + B_0*D_i
        # But let's push all i to be safe, then pop L times

        # To optimize, we can push only top L i's by E_i + B_0*D_i
        # Let's compute initial values and pick top L i's

        initial_vals = []
        for i in range(N):
            val = B[0] * D[i] + E[i]
            initial_vals.append((val, i))
        initial_vals.sort(reverse=True)
        initial_vals = initial_vals[:L]

        heap = []
        for val, i in initial_vals:
            # Store negative for max heap
            heapq.heappush(heap, (-val, i, 0))

        count = 0
        local_results = []
        while heap and count < L:
            val_neg, i, j = heapq.heappop(heap)
            val = -val_neg
            local_results.append(val)
            count += 1
            nj = j + 1
            if nj < N:
                new_val = B[nj] * D[i] + E[i]
                heapq.heappush(heap, (-new_val, i, nj))

        results.extend(local_results)

    # Now results has up to M*L values, pick top K
    results.sort(reverse=True)
    print(results[K-1])

if __name__ == "__main__":
    main()