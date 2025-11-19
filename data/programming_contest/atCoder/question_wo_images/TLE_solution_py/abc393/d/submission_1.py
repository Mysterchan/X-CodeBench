N = int(input())
S = input()

count1 = S.count("1")
count0 = N - count1

ans = 0
for i in range(N):
  if S[i] == "0":
    left_ans = S[:i].count("1")
    right_ans = count1 - left_ans
    ans += min(left_ans, right_ans)
print(ans)