def calculate_area_sum(N, Y):
    MOD = 998244353
    total_area = 0

    # Precompute the number of subsets for each possible range
    for i in range(N):
        for j in range(i + 1, N):
            min_y = min(Y[i], Y[j])
            max_y = max(Y[i], Y[j])
            width = j - i + 1
            height = max_y - min_y
            area = width * height
            total_area = (total_area + area) % MOD

    # Each pair contributes to 2^(N-2) subsets
    total_area = (total_area * pow(2, N - 2, MOD)) % MOD

    return total_area

# Read input
N = int(input())
Y = list(map(int, input().split()))

# Calculate and print the result
print(calculate_area_sum(N, Y))