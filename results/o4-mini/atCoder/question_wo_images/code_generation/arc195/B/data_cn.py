def can_make_equal_sums(N, A, B):
    total_A = sum(x for x in A if x != -1)
    total_B = sum(x for x in B if x != -1)
    count_A_neg = A.count(-1)
    count_B_neg = B.count(-1)

    # Calculate the total number of -1s
    total_neg = count_A_neg + count_B_neg

    # Calculate the target sum for each pair
    target_sum = (total_A + total_B + total_neg) // N

    # If the total sum is not divisible by N, it's impossible
    if (total_A + total_B + total_neg) % N != 0:
        return "No"

    # Check if we can achieve the target sum
    needed_A = 0
    needed_B = 0

    for a in A:
        if a == -1:
            needed_A += target_sum
        else:
            needed_A += a

    for b in B:
        if b == -1:
            needed_B += target_sum
        else:
            needed_B += b

    # Check if we can satisfy the needed sums with the available -1s
    if needed_A <= total_A + count_A_neg * target_sum and needed_B <= total_B + count_B_neg * target_sum:
        return "Yes"
    else:
        return "No"

# Read input
N = int(input().strip())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

# Get the result and print it
result = can_make_equal_sums(N, A, B)
print(result)