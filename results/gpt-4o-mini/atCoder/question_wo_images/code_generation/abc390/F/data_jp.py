def sum_of_operations(N, A):
    # f_dict will store the minimum operations needed for each (L, R) pair
    f_dict = {}
    total_operations = 0

    for L in range(N):
        unique_numbers = set()
        for R in range(L, N):
            unique_numbers.add(A[R])
            f_dict[(L, R)] = len(unique_numbers)
            total_operations += f_dict[(L, R)]

    return total_operations


# Input reading
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Get the result and print it
result = sum_of_operations(N, A)
print(result)