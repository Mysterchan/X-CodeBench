S=lambda:input()
I=lambda:int(input())
L=lambda:list(map(int,input().split()))
LS=lambda:list(map(str,input().split()))

n=I()
s=S()

count_one = s.count("1")
halfcount_one = count_one//2

cost_one = []
for i in range(n):
    if s[i] == "1":
        cost_one.append(i - len(cost_one))
ans = 0
for i in cost_one:
    ans += abs(i - halfcount_one)
print(ans)