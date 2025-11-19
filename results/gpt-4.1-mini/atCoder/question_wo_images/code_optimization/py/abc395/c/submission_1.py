N = int(input())
A = list(map(int, input().split()))

last_pos = {}
ans = -1

for i, val in enumerate(A):
    if val in last_pos:
        length = i - last_pos[val] + 1
        if ans == -1 or length < ans:
            ans = length
    last_pos[val] = i

print(ans)