def min_insertions_to_good_sequence(test_cases):
    results = []
    
    for A in test_cases:
        # Count frequencies of each number in A
        frequency = {}
        for number in A:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1
        
        # Count how many additions we need
        insertions_needed = 0
        last_count = 0
        
        # We can work with sorted numbers to count the additional needed "fills"
        for x in sorted(frequency):
            count = frequency[x]
            if count > last_count:
                insertions_needed += count - last_count
            last_count = count
        
        results.append(insertions_needed)
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []

index = 1
for _ in range(T):
    N = int(data[index])  # We can ignore N because we read the whole line for A
    A = list(map(int, data[index + 1].split()))
    test_cases.append(A)
    index += 2

results = min_insertions_to_good_sequence(test_cases)
for result in results:
    print(result)