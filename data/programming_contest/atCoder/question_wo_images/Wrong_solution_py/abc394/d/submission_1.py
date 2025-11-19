s=['_']*4**9;i=0
for c in input():
 if c in'([<':s[i]=c;i+=1
 elif')]>_([<'.index(c)=='([<_'.index(s[i-1]):i-=1
 else:print('No');exit()
print('Yes')