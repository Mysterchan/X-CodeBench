N, M = map(int, input().split())
A = set(map(int, input().split()))

result = [i for i in range(1, N + 1) if i not in A]

print(len(result))
if result:
    print(*result)
else:
    print()