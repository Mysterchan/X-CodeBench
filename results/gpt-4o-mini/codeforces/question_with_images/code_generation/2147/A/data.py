def min_steps_to_target(t, test_cases):
    results = []
    
    for x, y in test_cases:
        total_length = x + y
        steps = 1
        length_needed = 1
        
        while total_length > 0:
            total_length -= length_needed
            steps += 1
            length_needed += 1
            
        steps -= 1  # The last increment is unnecessary because it goes out of bounds
        
        if steps < 1 or (steps % 2 == 1 and x < y) or (x + 1 < y):
            results.append(-1)
        else:
            results.append(steps)
    
    return results

# Read input and output results
t = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(t)]
results = min_steps_to_target(t, test_cases)

for result in results:
    print(result)