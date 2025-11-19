def count_fine_triplets(N, S):
    S = sorted(S)
    count = 0
    S_set = set(S)

    for i in range(N):
        A = S[i]
        for j in range(i + 1, N):
            B = S[j]
            C = 2 * B - A
            if C > B and C in S_set:
                count += 1

    return count

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
S = list(map(int, data[1:N + 1]))

# Get the result and print it
result = count_fine_triplets(N, S)
print(result)