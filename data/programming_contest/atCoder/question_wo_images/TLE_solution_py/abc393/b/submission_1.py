S = list(input())
ans = 0
j = 0
for i in range(len(S)):
  j = 0
  if S[i] == "B":
    while i-j > -1 and i+j < len(S):
      if S[i-j] == "A" and S[i+j] == "C":
        ans += 1
        j += 1
print(ans)