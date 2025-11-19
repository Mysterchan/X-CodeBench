import sys

input = sys.stdin.read
data = input().splitlines()

N, Q = map(int, data[0].split())
nests = list(range(1, N + 1))

output = []

for i in range(1, Q + 1):
    operation = list(map(int, data[i].split()))
    if operation[0] == 1:
        a, b = operation[1] - 1, operation[2] - 1
        nests[a] = b + 1
    elif operation[0] == 2:
        a, b = operation[1] - 1, operation[2] - 1
        nests[a], nests[b] = nests[b], nests[a]
    elif operation[0] == 3:
        a = operation[1] - 1
        output.append(nests[a])

print("\n".join(map(str, output)))