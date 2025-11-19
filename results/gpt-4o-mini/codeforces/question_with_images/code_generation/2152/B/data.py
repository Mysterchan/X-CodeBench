def krug_survival_time(test_cases):
    results = []
    for n, r_K, c_K, r_D, c_D in test_cases:
        krug_distance = abs(r_K - r_D) + abs(c_K - c_D)

        if krug_distance == 1:  # If Doran is 1 step from the Krug
            results.append(1)
        elif krug_distance <= 2:  # Just 2 steps apart, Doran can catch in 2 moves.
            results.append(2)
        else:
            # Check if they are separated in a way that Doran cannot catch Krug
            vertical_distance = abs(r_K - r_D)
            horizontal_distance = abs(c_K - c_D)
            min_distance = min(vertical_distance, horizontal_distance)

            if n - krug_distance + 1 <= min_distance:
                results.append(-1)  # Krug can survive indefinitely
            else:
                results.append(max(vertical_distance, horizontal_distance) if krug_distance > 2 else 3)

    return results

# Reading input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = krug_survival_time(test_cases)

# Printing output
for result in results:
    print(result)