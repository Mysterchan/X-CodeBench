def count_good_triplets(N, S):
    S_set = set(S)
    count = 0
    
    for b in S:
        for d in range(1, 1000001):
            a = b - d
            c = b + d
            if a in S_set and c in S_set:
                count += 1
                
    return count

import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
S = list(map(int, data[1:N+1]))

result = count_good_triplets(N, S)
print(result)