def max_min_vitamins(N, X, foods):
    # Storage for maximum units of each vitamin per calorie limit
    dp = [[[0] * (X + 1) for _ in range(4)] for _ in range(3)]

    # Process the food items
    for v, a, c in foods:
        for i in range(2, -1, -1):  # Iterate backward over vitamins
            for j in range(X, c - 1, -1):  # Iterate backward over calories
                dp[i][j] = dp[i][j]  # Don't take this food
                if v == i + 1:
                    dp[i][j] = max(dp[i][j], dp[i][j - c] + a)

    # Search for maximum minimum vitamin intake
    left, right = 0, min(sum(dp[i][X] for i in range(3)), 200000)
    
    while left < right:
        mid = (left + right + 1) // 2  # Check if we can achieve mid units of each vitamin
        
        # Check if we can satisfy the condition of at least 'mid' units for each vitamin
        calorie_limit = [[0] * (X + 1) for _ in range(3)]
        for i in range(3):
            for j in range(X + 1):
                calorie_limit[i][j] = dp[i][j]

        # We can only eat if we have enough vitamins >= mid
        can_eat = True
        for j in range(mid, 200001):  # Check vitamins at least 'mid'
            for i in range(3):
                for cals in range(X + 1):
                    if calorie_limit[i][cals] >= mid:
                        # Reduce the calories spent for this specific vitamin intake
                        new_cals = cals
                        while new_cals >= 0 and calorie_limit[i][new_cals] >= mid:
                            new_cals -= 1
            # Check for maximum calories left to feed other vitamins
            if new_cals >= 0:
                can_eat = False
                break

        if can_eat:
            left = mid  # We can satisfy at least 'mid' vitamins
        else:
            right = mid - 1  # Cannot satisfy so go lower

    return left

# Reading input values
import sys
input = sys.stdin.read
data = input().strip().splitlines()
first_line = data[0].split()
N = int(first_line[0])
X = int(first_line[1])
foods = [tuple(map(int, line.split())) for line in data[1:]]

# Compute and print the result
result = max_min_vitamins(N, X, foods)
print(result)