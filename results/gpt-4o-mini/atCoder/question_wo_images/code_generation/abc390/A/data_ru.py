def can_sort_with_one_swap(arr):
    sorted_arr = sorted(arr)
    mismatches = sum(1 for i in range(5) if arr[i] != sorted_arr[i])
    
    # We can correct the array with exactly one swap if there are exactly 2 mismatched positions
    return mismatches == 2

# Read input
A = list(map(int, input().split()))
# Check if we can sort with one swap and print the result
print("Yes" if can_sort_with_one_swap(A) else "No")