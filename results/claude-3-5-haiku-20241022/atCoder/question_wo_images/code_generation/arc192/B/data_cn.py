n = int(input())
a = list(map(int, input().split()))

total_moves = sum(a)

if total_moves % 2 == 1:
    print("Fennec")
else:
    print("Snuke")