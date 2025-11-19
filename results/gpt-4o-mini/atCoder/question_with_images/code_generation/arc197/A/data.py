def max_black_cells(T, cases):
    results = []
    for H, W, S in cases:
        # Count the number of D's and R's in S
        count_D = S.count('D')
        count_R = S.count('R')
        
        # The number of '?' can be used to fill in the remaining D's and R's
        remaining_D = (H - 1) - count_D
        remaining_R = (W - 1) - count_R
        
        # The total number of '?' available
        count_question = S.count('?')
        
        # We can use '?' to fill in the remaining D's and R's
        if remaining_D < 0 or remaining_R < 0:
            results.append(0)  # Invalid case, should not happen due to constraints
            continue
        
        # Fill the remaining D's and R's with '?'
        if remaining_D + remaining_R <= count_question:
            # We can fill all remaining D's and R's
            total_cells = H + W - 1  # All cells in the path
        else:
            # We can only fill some of them
            total_cells = (H - 1) + (W - 1) + count_question
        
        results.append(total_cells)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []

for i in range(1, 2 * T, 2):
    H, W = map(int, data[i].split())
    S = data[i + 1]
    cases.append((H, W, S))

# Get results
results = max_black_cells(T, cases)

# Print results
for result in results:
    print(result)