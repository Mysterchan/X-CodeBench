a = input()
if a==1: print(1)
else:
  b = 1
  for i in range(3*(10**18)):
    b *= int(i+1)
    if a== b:
      print(i+1)
      break