def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # The key insight:
    # After any number of operations, the stones are redistributed by moving all stones from one bag to another.
    # This means the final configuration is a partition of the original stones into some subset of bags,
    # where some bags may be empty.
    #
    # Since we can move stones any number of times, the final configuration corresponds to a partition of the
    # multiset A into groups, where each group sums the stones of the bags merged into one bag.
    #
    # The XOR of the final configuration is the XOR of the sums of these groups.
    #
    # The problem reduces to:
    # Find the number of distinct XOR values of all possible partitions of A into any number of groups,
    # where each group sum is the sum of the elements in that group.
    #
    # This is a known problem and can be solved using a DP approach:
    #
    # Let dp be a set of possible XOR values of sums of some partition of a subset of A.
    # We process elements one by one, and for each element, we can either:
    # - start a new group with this element (XOR with the element)
    # - merge it into an existing group (which changes the sums, but since we only track XOR of sums,
    #   we need a way to represent all possible XORs)
    #
    # However, the problem is simplified by the fact that the operation allows moving all stones from one bag to another,
    # so the final configuration corresponds to grouping the original bags arbitrarily.
    #
    # The number of possible XOR values is equal to the number of distinct XOR sums of all subsets of A,
    # but since groups can be merged arbitrarily, the problem is equivalent to:
    #
    # The set of possible XOR values is the set of XOR sums of all subsets of A.
    #
    # But this is not correct because the XOR of sums of groups is not the XOR of subsets of A directly.
    #
    # Let's analyze the problem carefully:
    #
    # Each final configuration corresponds to a partition of the set {1,...,N} into groups.
    # For each group, sum the A_i in that group.
    # Then XOR all these sums.
    #
    # We want to find the number of distinct values of XOR of sums over all partitions.
    #
    # Key observation:
    # The XOR of sums over a partition can be rewritten as:
    # XOR_{groups} (sum of elements in group)
    #
    # Since sum is addition, and XOR is XOR, this is a complicated function.
    #
    # But the problem is known and can be solved using a DP over subsets:
    #
    # Let dp be a set of possible XOR values of sums of partitions of subsets of A.
    #
    # We can use a DP approach:
    # - Initialize dp = {0}
    # - For each element a in A:
    #   - For each XOR value x in dp:
    #     - Add x ^ a to dp
    #
    # But this counts XOR of subsets, not XOR of sums of partitions.
    #
    # Another approach:
    #
    # The problem is equivalent to:
    # The number of distinct XOR values of sums of partitions of A.
    #
    # We can use a DP over subsets:
    #
    # Let f[S] be the set of possible XOR values of sums of partitions of subset S.
    #
    # Base case:
    # f[empty] = {0}
    #
    # For each non-empty subset S:
    #   For each non-empty subset T of S:
    #     For each x in f[S \ T]:
    #       f[S].add(x ^ sum(T))
    #
    # The answer is |f[full set]|
    #
    # Since N <= 12, we can implement this DP.
    #
    # Complexity:
    # There are 2^N subsets.
    # For each subset, we consider all its non-empty subsets.
    # This is O(3^N) which is feasible for N=12.
    #
    # Implementation details:
    # - Precompute sum of all subsets.
    # - Use a list of sets f of size 2^N.
    # - f[0] = {0}
    # - For each S in 1..2^N-1:
    #   - Initialize f[S] = empty set
    #   - For each non-empty subset T of S:
    #       For each x in f[S \ T]:
    #           f[S].add(x ^ sum(T))
    #
    # Finally, print len(f[(1<<N)-1])
    #
    # To optimize:
    # - Use bitmask iteration for subsets.
    # - Use a dictionary or set for f[S].
    #
    # Let's implement.

    # Precompute sum of all subsets
    total_subsets = 1 << N
    subset_sum = [0] * total_subsets
    for mask in range(total_subsets):
        s = 0
        for i in range(N):
            if mask & (1 << i):
                s += A[i]
        subset_sum[mask] = s

    f = [set() for _ in range(total_subsets)]
    f[0].add(0)

    for S in range(1, total_subsets):
        # Enumerate all non-empty subsets T of S
        T = S
        while T > 0:
            # For each x in f[S \ T], add x ^ sum(T) to f[S]
            remainder = S ^ T
            for x in f[remainder]:
                f[S].add(x ^ subset_sum[T])
            T = (T - 1) & S

    print(len(f[total_subsets - 1]))


if __name__ == "__main__":
    main()