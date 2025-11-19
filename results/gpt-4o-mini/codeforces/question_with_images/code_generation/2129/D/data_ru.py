def count_permutations(t, test_cases):
    MOD = 998244353
    results = []

    for case in test_cases:
        n, s = case
        if s.count(-1) == n:
            # If all s[i] are -1, the result is n! (n factorial)
            factorial = 1
            for i in range(1, n + 1):
                factorial = factorial * i % MOD
            results.append(factorial)
            continue

        count_fixed_positions = sum(1 for x in s if x != -1)
        if count_fixed_positions >= 2 and (s.count(0) > 1):
            results.append(0)
            continue

        valid_permutation_count = 1
        for idx in range(n):
            if s[idx] != -1:
                # s[idx] should show how many previous black cells were close to this cell
                left = max(0, idx - s[idx])
                right = min(n - 1, idx + s[idx])
                # Check how many fixed positions are in the range
                fixed_inside = sum(1 for i in range(left, right + 1) if s[i] != -1)
                
                if fixed_inside > 1:
                    valid_permutation_count = 0
                    break

        free_count = s.count(-1)
        # Each free position can take one of the remaining available numbers
        for i in range(1, free_count + 1):
            valid_permutation_count = valid_permutation_count * i % MOD

        results.append(valid_permutation_count)

    return results


# Reading input
input_data = input().splitlines()
t = int(input_data[0])
test_cases = []
index = 1
for _ in range(t):
    n = int(input_data[index])
    s = list(map(int, input_data[index + 1].split()))
    test_cases.append((n, s))
    index += 2

# Getting results
results = count_permutations(t, test_cases)

# Printing results
for result in results:
    print(result)