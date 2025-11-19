def count_distinct_xor_values(N, A):
    # Calculate the overall XOR of all A_i
    overall_xor = 0
    for num in A:
        overall_xor ^= num

    # Set to hold possible XOR values
    possible_xors = set()

    # We can produce values by taking combinations of the initial bags
    # The number of distinct values is 2 * (max_A xor overall_xor) + 1
    # This is all values ranging from 0 to overall_xor inclusive
    # as shifting bits in any combination will yield every combination from using 0 to maximum

    # To find all unique combinations of values that can manifest
    # Only unique values from the maximum elements need to be analyzed

    # To store encountered basis
    basis = []

    for num in A:
        # Reducing the number with the existing basis
        for b in basis:
            num = min(num, num ^ b)
        if num > 0:
            basis.append(num)
            # Generating all combinations
            new_combinations = []
            for x in possible_xors:
                new_combination = x ^ num
                new_combinations.append(new_combination)
            possible_xors.update(new_combinations)
        possible_xors.add(0)  # Always can produce 0

    return len(possible_xors)

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:N+1]))

# Output the result
print(count_distinct_xor_values(N, A))