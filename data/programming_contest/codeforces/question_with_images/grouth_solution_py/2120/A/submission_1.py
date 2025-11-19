for s in[*open(0)][1:]:a=*map(int,s.split()),;(a,b,c),(d,e,f)=sorted((a[::2],a[1::2]));print('YNEOS'[{e,f,a+b+c}!={d}!={e+f,a+b,a+c}::2])
