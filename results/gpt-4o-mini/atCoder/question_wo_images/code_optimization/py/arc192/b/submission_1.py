N = int(input())
A = list(map(int, input().split()))

cnt0 = sum(1 for a in A if a % 2 == 0)
cnt1 = N - cnt0

if cnt1 > cnt0:
    print("Fennec")
else:
    print("Snuke")