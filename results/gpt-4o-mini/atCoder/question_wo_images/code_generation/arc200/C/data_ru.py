def minimize_discontent(T, test_cases):
    results = []
    
    for case in test_cases:
        N, intervals = case
        people = sorted(range(N), key=lambda i: (intervals[i][0], intervals[i][1]))
        
        P = [0] * N
        available_seats = list(range(1, N + 1))
        
        for person in people:
            P[person] = available_seats.pop(0)
        
        results.append(" ".join(map(str, P)))
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []
index = 1

for _ in range(T):
    N = int(data[index])
    intervals = []
    for i in range(N):
        L, R = map(int, data[index + 1 + i].split())
        intervals.append((L, R))
    test_cases.append((N, intervals))
    index += N + 1

results = minimize_discontent(T, test_cases)
for result in results:
    print(result)