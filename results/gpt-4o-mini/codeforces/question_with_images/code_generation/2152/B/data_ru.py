def survival_time(t, test_cases):
    results = []
    
    for n, r_K, c_K, r_D, c_D in test_cases:
        # Determine the distance between K and D
        d_r = abs(r_K - r_D)
        d_c = abs(c_K - c_D)

        # Check the difference in distance and calculate the distance metrics
        if d_r > d_c:
            # K can escape in the vertical direction
            if d_r > n - d_c:
                results.append(-1)
            else:
                results.append((d_r + 1) // 2)
        else:
            # K can escape in the horizontal direction
            if d_c > n - d_r:
                results.append(-1)
            else:
                results.append((d_c + 1) // 2)

    return results


# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = [tuple(map(int, line.split())) for line in data[1:t + 1]]

# Get results
results = survival_time(t, test_cases)

# Print results
for result in results:
    print(result)