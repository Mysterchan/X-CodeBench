import sys
input = sys.stdin.read

data = input().split()
index = 0

T = int(data[index])
index += 1

results = []

for _ in range(T):
    N = int(data[index])
    index += 1

    A = list(map(int, data[index:index + N]))
    index += N

    total = sum(A)
    average = total / N

    count = sum(1 for a in A if a > average)
    results.append(str(count))

print("\n".join(results))