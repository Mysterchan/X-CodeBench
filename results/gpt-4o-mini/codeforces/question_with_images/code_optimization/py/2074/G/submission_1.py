import sys
from itertools import combinations

input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n
    
    # For a polygon with n vertices, we can only use at most
    # n//3 triangles since each triangle takes 3 vertices.

    max_score = 0
    
    # Calculate the maximum score by considering combinations of indices
    for indices in combinations(range(n), 3):
        i, j, k = indices
        max_score = max(max_score, a[i] * a[j] * a[k])

    results.append(max_score)

# Print all results after processing all test cases
sys.stdout.write("\n".join(map(str, results)) + "\n")