N = int(input())
A = list(map(int, input().split()))

total = sum(A)

if total % 2 == 1:
    print("Fennec")
else:
    print("Snuke")