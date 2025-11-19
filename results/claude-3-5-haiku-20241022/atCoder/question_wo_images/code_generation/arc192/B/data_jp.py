n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total % 2 == 1:
    print("Fennec")
else:
    print("Snuke")