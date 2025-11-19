def minimize_cost(N, U, D, L, R):
    # Insert inf at both ends for boundary conditions
    U = [float('inf')] + U + [float('inf')]
    D = [float('inf')] + D + [float('inf')]
    L = [float('inf')] + L + [float('inf')]
    R = [float('inf')] + R + [float('inf')]

    # Find the minimum cost
    ans = float('inf')

    # Precompute the smallest and second smallest costs in U, D, L, R
    def get_two_min_indices(arr):
        min1_index = min2_index = -1
        min1 = min2 = float('inf')
        
        for i in range(1, len(arr) - 1):
            if arr[i] < min1:
                min2 = min1
                min2_index = min1_index
                min1 = arr[i]
                min1_index = i
            elif arr[i] < min2:
                min2 = arr[i]
                min2_index = i

        return min1, min1_index, min2, min2_index

    minU, idxU1, minU2, idxU2 = get_two_min_indices(U)
    minD, idxD1, minD2, idxD2 = get_two_min_indices(D)
    minL, idxL1, minL2, idxL2 = get_two_min_indices(L)
    minR, idxR1, minR2, idxR2 = get_two_min_indices(R)

    # Calculating the answer using the minimums directly
    ans = min(
        minU + minU2 + minD + minD2 + minL + minL2 + minR + minR2
    )

    # Consider the case where we can choose two elements from the same edge (U, D, L, R)
    if idxU1 < idxD1 and idxR1 < idxL1:
        ans = min(ans, minU + minD + minL + minR)

    if idxU2 < idxD2 and idxR2 < idxL2:
        ans = min(ans, minU2 + minD2 + minL2 + minR2)

    return ans

import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        N = int(data[index])
        index += 1
        U = list(map(int, data[index:index + N - 2]))
        index += N - 2
        D = list(map(int, data[index:index + N - 2]))
        index += N - 2
        L = list(map(int, data[index:index + N - 2]))
        index += N - 2
        R = list(map(int, data[index:index + N - 2]))
        index += N - 2
        
        # Calculate result for this test case
        result = minimize_cost(N, U, D, L, R)
        results.append(result)

    # Print all results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()