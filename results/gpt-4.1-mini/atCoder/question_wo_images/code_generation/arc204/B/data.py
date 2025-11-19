def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # We want to sort P into ascending order with minimum swaps.
    # Each swap can be between any two positions i, j (i != j).
    # If |i-j| is multiple of N, Alice gets 1 point for that swap.
    #
    # Among all minimal swap sequences, maximize the sum of points.
    #
    # Key observations:
    # - The minimal number of swaps to sort a permutation is:
    #   total_swaps = (length) - (number_of_cycles)
    # - We want to maximize the number of swaps where |i-j| % N == 0.
    #
    # Positions are 1-based indexed in problem, but we use 0-based internally.
    #
    # The array length is NK.
    #
    # Let's analyze the structure:
    #
    # Positions can be grouped by their index mod N:
    # For each r in [0, N-1], positions r, r+N, r+2N, ..., r+(K-1)*N form a group.
    #
    # Swapping two elements in the same group (same mod N) yields a point.
    #
    # So, the array is divided into N groups of size K.
    #
    # The permutation P maps positions to values.
    # The sorted array is [1, 2, ..., NK].
    #
    # We want to decompose the permutation into cycles.
    #
    # Each cycle can be decomposed into swaps to fix it.
    # The minimal number of swaps to fix a cycle of length L is L-1.
    #
    # To maximize points, we want to perform as many swaps as possible between positions
    # whose indices differ by a multiple of N (i.e., within the same group).
    #
    # If a cycle is contained entirely within one group (all positions have the same i mod N),
    # then all swaps to fix that cycle can be done inside that group, so all swaps yield points.
    #
    # If a cycle contains positions from multiple groups, then some swaps must be between different groups,
    # which do not yield points.
    #
    # So the problem reduces to:
    # - Find the cycles of the permutation.
    # - For each cycle, check how many distinct groups (mod N classes) it contains.
    # - If cycle is contained in one group, all swaps in that cycle yield points.
    # - If cycle spans multiple groups, no swaps in that cycle yield points (because to fix the cycle,
    #   at least one swap must be between different groups).
    #
    # Why no points for multi-group cycles?
    # Because to fix a cycle spanning multiple groups, you must swap elements between different groups,
    # which do not yield points.
    #
    # So the answer is the sum over all cycles of length L:
    #   if cycle in one group: points += L-1
    #   else: points += 0
    #
    # The minimal number of swaps is total length - number of cycles.
    #
    # The maximum points under minimal swaps is sum of (L-1) for cycles contained in one group.
    #
    # Let's implement this.

    visited = [False] * (N * K)
    points = 0

    for start in range(N * K):
        if not visited[start]:
            cycle = []
            cur = start
            while not visited[cur]:
                visited[cur] = True
                cycle.append(cur)
                cur = P[cur] - 1  # P[cur] is 1-based value, map to 0-based index

            # Check groups in cycle
            groups = set(pos % N for pos in cycle)
            if len(groups) == 1:
                # All swaps in this cycle yield points
                points += len(cycle) - 1

    print(points)


if __name__ == "__main__":
    main()