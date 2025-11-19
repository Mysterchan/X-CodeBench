N, M = map(int, input().split())
if M > 0:
    A = set(map(int, input().split()))
else:
    A = set()

missing = []
for i in range(1, N + 1):
    if i not in A:
        missing.append(i)

print(len(missing))
if missing:
    print(' '.join(map(str, missing)))