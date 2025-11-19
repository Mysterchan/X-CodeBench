import sys
import bisect

input = sys.stdin.read
data = input().splitlines()

Q = int(data[0])
queries = [tuple(map(int, line.split())) for line in data[1:Q + 1]]

removed = set()
results = []

for A, B in queries:
    # Mark multiples of A as removed
    for multiple in range(A, 10**9 + 1, A):
        removed.add(multiple)
    
    # Find the B-th smallest number not in removed
    count = 0
    current = 0
    while count < B:
        current += 1
        if current not in removed:
            count += 1
    
    results.append(current)

# Print all results
sys.stdout.write('\n'.join(map(str, results)) + '\n')