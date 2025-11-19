A1,A2,A3 = map(int,input().split())
if A1 * A2 == A3 or A2 * A3 == A1 or A2 * A3 == A1:
  print("Yes")
else:
  print("No")