N, M = map(int, input().split())
A = set(map(int, input().split()))

missing_numbers = [i for i in range(1, N + 1) if i not in A]

print(len(missing_numbers))
if missing_numbers:
    print(" ".join(map(str, missing_numbers)))