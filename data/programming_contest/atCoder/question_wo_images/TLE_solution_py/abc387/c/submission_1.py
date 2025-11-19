L,R = map(int,input().split())
count = 0

def hebi(x):
  a = list(map(int,str(x)))
  if a[0] > max(a[1:]):
    return True
  else:
    return False

for i in range(L,R+1):
  if hebi(i):
    count += 1

print(count)