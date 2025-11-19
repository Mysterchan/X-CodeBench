def krug_survival_time(test_cases):
    results = []
    for n, r_K, c_K, r_D, c_D in test_cases:
        dx = abs(r_K - r_D)
        dy = abs(c_K - c_D)
        
        if dx <= 1 and dy <= 1:
            results.append(1)
        elif n == 1:  # If n is 1, then next move will capture Krug
            results.append(2)
        else:
            if dx > dy:
                results.append((dx + 1) // 2)
            else:
                results.append((dy + 1) // 2)
                
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = [tuple(map(int, line.split())) for line in data[1:t + 1]]
results = krug_survival_time(test_cases)

# Output the results
for res in results:
    print(res)