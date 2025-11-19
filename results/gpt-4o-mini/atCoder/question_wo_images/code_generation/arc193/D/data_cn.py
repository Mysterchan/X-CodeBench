import sys

input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
results = []
index = 1

for _ in range(T):
    N = int(data[index])
    A = data[index + 1]
    B = data[index + 2]
    index += 3

    # Find the positions of the pieces in A and the required positions in B
    positions_A = [i for i in range(N) if A[i] == '1']
    positions_B = [i for i in range(N) if B[i] == '1']

    # Check if it's possible to satisfy the condition
    if len(positions_A) < len(positions_B):
        results.append(-1)
        continue

    # Calculate the minimum moves required
    moves = 0
    j = 0
    for pos_A in positions_A:
        if j < len(positions_B) and pos_A >= positions_B[j]:
            moves += pos_A - positions_B[j]
            j += 1
        if j >= len(positions_B):
            break

    if j < len(positions_B):
        results.append(-1)
    else:
        results.append(moves)

print('\n'.join(map(str, results)))