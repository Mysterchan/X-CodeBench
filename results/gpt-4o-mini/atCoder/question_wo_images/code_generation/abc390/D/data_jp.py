def count_possible_xors(N, A):
    from functools import reduce
    
    # Generate all unique combinations using bitwise OR
    reachable = set()
    for i in range(N):
        reachable.add(A[i])  # Start with individual bags
        # Iterate through tuples of combinations
        for j in range(i + 1, N):
            combined_value = A[i] | A[j]
            reachable.add(combined_value)

    # Compute the cumulative XOR of reachable bag counts
    all_possible_xors = set()
    for i in range(2 ** N):
        current_xor = 0
        for j in range(N):
            if i & (1 << j):
                current_xor ^= A[j]
        all_possible_xors.add(current_xor)

    return len(all_possible_xors)

# Read input
N = int(input())
A = list(map(int, input().split()))

# Output result
print(count_possible_xors(N, A))