def min_inserts_to_good_sequence(test_cases):
    results = []
    
    for A in test_cases:
        frequency = {}
        
        # Count the frequency of each number in A
        for number in A:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1
                
        inserts_needed = 0
        
        # Calculate the total inserts needed
        for count in frequency.values():
            if count > 1:
                inserts_needed += count - 1  # We need (count - 1) inserts to pair each
        
        results.append(inserts_needed)
    
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
T = int(data[0])
test_cases = []

index = 1
for _ in range(T):
    N = int(data[index])
    A = list(map(int, data[index + 1].split()))
    test_cases.append(A)
    index += 2

results = min_inserts_to_good_sequence(test_cases)

for result in results:
    print(result)