import sys

input = sys.stdin.read
data = input().splitlines()

N, Q = map(int, data[0].split())

# To maintain the current nest of each pigeon
nests = list(range(N + 1))

# To track the current index for Type 3 queries
output = []

# Execute each operation
for i in range(1, Q + 1):
    op = list(map(int, data[i].split()))
    if op[0] == 1:  # Type 1: Move pigeon a to nest b
        a, b = op[1], op[2]
        nests[a] = b
    elif op[0] == 2:  # Type 2: Swap nests a and b
        a, b = op[1], op[2]
        for j in range(1, N + 1):
            if nests[j] == a:
                nests[j] = b
            elif nests[j] == b:
                nests[j] = a
    elif op[0] == 3:  # Type 3: Report the nest of pigeon a
        a = op[1]
        output.append(nests[a])

# Output all results for Type 3 queries
sys.stdout.write('\n'.join(map(str, output)) + '\n')