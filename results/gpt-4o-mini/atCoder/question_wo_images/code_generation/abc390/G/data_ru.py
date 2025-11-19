def sum_f_permutations(N):
    MOD = 998244353

    # Calculate the factorial of N with modular arithmetic
    fact = 1
    for i in range(2, N + 1):
        fact = (fact * i) % MOD

    # Precompute powers of 10 and their contributions
    power_of_10 = 1
    contribution = 0
    for i in range(1, N + 1):
        contribution = (contribution + power_of_10) % MOD
        power_of_10 = (power_of_10 * 10) % MOD

    # The total sum f(P) is fact * contribution
    result = (fact * contribution) % MOD
    return result

# Read input
N = int(input().strip())
# Print the result
print(sum_f_permutations(N))