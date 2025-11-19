N = int(input())
S = list(input().strip() for _ in range(N))
S.sort(key=len)

print("".join(S))