import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

itung = 1  # count the original sequence (L=R)
for i in range(n - 1):
    if a[i] != a[i + 1]:
        itung += 1

print(itung)