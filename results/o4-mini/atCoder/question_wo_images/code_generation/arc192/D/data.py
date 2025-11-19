def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * (b // gcd(a, b))

def f(x):
    from math import gcd
    p, q = x
    return p * q

def find_good_sequences(N, A):
    MOD = 998244353
    from collections import defaultdict
    from math import gcd
    from functools import reduce

    # Step 1: Calculate the LCM of all A_i
    lcm_A = reduce(lcm, A)

    # Step 2: Create a list of possible values for S_i
    possible_values = []
    for a in A:
        for k in range(1, lcm_A // a + 1):
            possible_values.append(a * k)

    # Step 3: Count the number of good sequences
    total_sum = 0
    count = 0

    # We will use a recursive function to generate sequences
    def generate_sequence(current_sequence, index):
        nonlocal total_sum, count
        if index == N:
            if reduce(gcd, current_sequence) == 1:
                score = reduce(lambda x, y: x * y % MOD, current_sequence, 1)
                total_sum = (total_sum + score) % MOD
                count += 1
            return
        
        for value in possible_values:
            if index == 0 or f((current_sequence[index - 1], value)) == A[index - 1]:
                current_sequence[index] = value
                generate_sequence(current_sequence, index + 1)

    # Start generating sequences
    current_sequence = [0] * N
    generate_sequence(current_sequence, 0)

    return total_sum

# Read input
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Get the result
result = find_good_sequences(N, A)

# Print the result
print(result)