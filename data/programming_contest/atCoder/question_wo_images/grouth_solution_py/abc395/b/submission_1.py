N = int(input())
list1 = [[0] * N  for _ in range(N)]
for i in range(1,N+1):
  j =  N + 1 - i
  if i <= j:
    for x in range(i,j + 1):
      for y in range(i,j + 1):
         if i % 2 != 0:
           list1[x-1][y-1] = '#'
         else:
            list1[x-1][y-1] = '.'
for value in list1:
  print(''.join(value))