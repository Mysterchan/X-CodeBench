def generate_2D_accumulate(array):
    ac=[[0 for j in range(len(array[0])+1)] for i in range(len(array)+1)]
    for i in range(len(array)):
        for j in range(len(array[i])):
            ac[i+1][j+1]=ac[i][j+1]+ac[i+1][j]-ac[i][j]+array[i][j]
    return ac
def calculate_2D_accumulate(array,a,b,c,d):
    return array[c][d]-array[a][d]-array[c][b]+array[a][b]
N,Q=map(int,input().split())
S=[input() for i in range(N)]
r=[[0 for j in range(N-1)] for i in range(N-1)]
for i in range(N-1):
    for j in range(N-1):
        if S[i][j]=="." and S[i][j+1]=="." and S[i+1][j]=="." and S[i+1][j+1]==".":
            r[i][j]=1
ruiseki=generate_2D_accumulate(r)
for _ in range(Q):
    U,D,L,R=map(int,input().split())
    print(calculate_2D_accumulate(ruiseki,U-1,L-1,D-1,R-1))