def can_sort_by_single_swap(A):
    # Count the number of out-of-order pairs
    out_of_order_count = 0
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            out_of_order_count += 1
            
    # We can sort the array with exactly one swap if there's exactly one out-of-order pair
    return out_of_order_count == 1

# Read input
A = list(map(int, input().strip().split()))

# Check if it's possible to sort by a single swap
if can_sort_by_single_swap(A):
    print("Yes")
else:
    print("No")