N, M = map(int, input().split())
A = set(map(int, input().split()))

missing = [i for i in range(1, N+1) if i not in A]

print(len(missing))
if missing:
    print(*missing)