X = int(input())

number = 0
i=1
while i <= X:
  if X%i == 0 and X // i <=9:
    number += 1

answer= 2025-number*X

print(answer)