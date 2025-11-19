def can_sort_with_one_swap(A):
    # Check if already sorted
    if A == sorted(A):
        return "No"

    # Count how many pairs are out of order
    out_of_order_count = 0
    for i in range(4):
        if A[i] > A[i + 1]:
            out_of_order_count += 1
            
    # It can be sorted by exactly one swap if there is exactly one pair out of order
    return "Yes" if out_of_order_count == 1 else "No"

# Read input
A = list(map(int, input().strip().split()))
# Output result
print(can_sort_with_one_swap(A))