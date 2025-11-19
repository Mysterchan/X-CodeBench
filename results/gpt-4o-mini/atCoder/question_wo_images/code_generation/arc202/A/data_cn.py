def min_insertions_to_good_sequence(test_cases):
    results = []
    for case in test_cases:
        N, A = case
        freq = {}
        
        for num in A:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # The number of unique pairs of values we can form
        pairs = 0
        for count in freq.values():
            pairs += count // 2  # Each pair can create one new element
        
        # The number of unique elements needs (pairs + 1) merges to become 1
        unique_elements_needed = len(freq) - pairs
        insertions = max(0, unique_elements_needed)

        results.append(insertions)

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
    test_cases.append((N, A))
    index += 2

results = min_insertions_to_good_sequence(test_cases)

# Print results
for result in results:
    print(result)