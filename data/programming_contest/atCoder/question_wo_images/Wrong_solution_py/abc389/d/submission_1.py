R = int(input())

def sircle(x):
  return int((R**2 - x**2) ** (1/2))

ans = 0
i = 0.5
j = R + 0.5

while j != 0.5:
  ans += sircle(i)-1
  i += 1
  j -= 1

print(4*ans -3 + 4*R)