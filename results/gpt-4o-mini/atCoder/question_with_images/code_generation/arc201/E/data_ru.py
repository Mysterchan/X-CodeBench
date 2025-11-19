def sum_of_rectangles(N, Y):
    MOD = 998244353
    total_area = 0

    # Precompute the contribution of each point
    for i in range(N):
        for j in range(i + 1, N):
            # Calculate the area of the rectangle formed by points (i, Y[i]) and (j, Y[j])
            width = j - i + 1
            height = max(Y[i], Y[j]) - min(Y[i], Y[j])
            area = width * height
            total_area = (total_area + area) % MOD

    return total_area

# Input reading
N = int(input().strip())
Y = list(map(int, input().strip().split()))

# Output the result
print(sum_of_rectangles(N, Y))