def can_make_equal_sum(N, A, B):
    # Calculate the number of -1s in A and B
    count_A_neg1 = A.count(-1)
    count_B_neg1 = B.count(-1)

    # Calculate the current sums of A and B ignoring -1s
    sum_A = sum(x for x in A if x != -1)
    sum_B = sum(x for x in B if x != -1)

    # Calculate the number of non-negative integers we can set
    total_neg1 = count_A_neg1 + count_B_neg1

    # The target sum for each pair A_i + B_i
    # We need to find a target sum that can be achieved
    # The target sum must be the same for all pairs
    # Let's denote the target sum as S
    # S = (sum_A + sum_B + x) / N where x is the total we can add from -1s

    # We need to check if we can find such an S
    # S must be an integer, hence (sum_A + sum_B + x) must be divisible by N
    # x can be at most total_neg1 * (max_possible_value)
    # But since we can set any non-negative integer, we can just check the feasibility

    # The minimum sum we can achieve with the current values
    min_sum = sum_A + sum_B

    # The maximum sum we can achieve by replacing all -1s with 0
    max_sum = min_sum + total_neg1 * 0  # since we can replace with any non-negative integer

    # We need to check if there exists an S such that:
    # min_sum <= S * N <= max_sum
    # This means:
    # min_sum / N <= S <= max_sum / N
    # S must also be an integer, hence we need to check the bounds

    # Check if we can find a valid S
    for S in range(min_sum // N, (max_sum // N) + 1):
        if (S * N - min_sum) <= total_neg1:
            return "Yes"
    
    return "No"

# Read input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Get the result
result = can_make_equal_sum(N, A, B)

# Print the result
print(result)