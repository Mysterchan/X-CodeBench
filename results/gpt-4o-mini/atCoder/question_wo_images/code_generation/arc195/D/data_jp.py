def min_operations_to_empty(T, cases):
    results = []
    for case in cases:
        N, A = case
        count = {}
        
        # Count the frequency of each number in A
        for num in A:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # The number of operations needed is the number of unique elements
        # plus the maximum frequency of any single element
        max_freq = max(count.values())
        unique_count = len(count)
        
        # The minimum operations needed
        min_operations = unique_count + (max_freq - 1)
        results.append(min_operations)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []
index = 1
for _ in range(T):
    N = int(data[index])
    A = list(map(int, data[index + 1].split()))
    cases.append((N, A))
    index += 2

# Get results
results = min_operations_to_empty(T, cases)

# Output results
sys.stdout.write('\n'.join(map(str, results)) + '\n')