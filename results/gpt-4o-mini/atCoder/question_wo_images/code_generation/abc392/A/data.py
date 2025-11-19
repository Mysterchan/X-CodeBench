def can_form_product(A):
    # Sort the array to easily check permutations
    A.sort()
    # Check if the product of the two smaller numbers equals the largest number
    return A[0] * A[1] == A[2]

# Read input
A = list(map(int, input().strip().split()))

# Check and print the result
if can_form_product(A):
    print("Yes")
else:
    print("No")