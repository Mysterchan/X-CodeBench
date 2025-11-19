for s in[*open(0)][1:]:n,a,b=map(int,s.split());print('YNEOS'[n+b&1or n+a&1and a>b::2])
