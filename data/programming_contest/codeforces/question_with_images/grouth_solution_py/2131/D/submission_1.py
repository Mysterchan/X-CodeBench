I=input
for _ in[0]*int(I()):
 r=[0]+[0]*int(I());g=[[]for _ in r];c=i=0
 for _ in r[2:]:u,v=map(int,I().split());g[u]+=v,;g[v]+=u,
 for l in g:
  if len(l)==1:c+=1;r[i]+=1;r[l[0]]+=1
  i+=1
 print(c-max(r))
