N = int(input())
dic1 = {}
list1 = []
for i in range(N):
  S = input()
  dic1[S] = len(S)
sort_dic = sorted(dic1.items(),key = lambda x:x[1])
print(sort_dic)
for value in sort_dic:
  list1.append(value[0])
print(''.join(list1))