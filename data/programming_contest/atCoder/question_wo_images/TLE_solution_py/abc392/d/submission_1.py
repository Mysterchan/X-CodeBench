import sys
import os

sys.setrecursionlimit(10**7)

input = lambda: sys.stdin.readline().rstrip()

filename = r'ABC_392\インプット\_input_D.txt'
if os.path.exists(filename):
    sys.stdin = open(filename, 'r')

try:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')
except ModuleNotFoundError:
    pass

def MAPIN():
    return map(int,input().split())
def LIN():
    return list(map(int,input().split()))
def ININ():
    return int(input())

N = ININ()

KAs = [LIN() for _ in range(N)]

Amax = 0
As = []
for i in range(N):
    deme = []
    K = KAs[i][0]
    for j in range(K):
        deme.append(KAs[i][j+1])
        Amax = max(Amax,KAs[i][j+1])
    deme.sort()
    As.append(deme)

Ds = [[0]*Amax for _ in range(N)]
for i in range(N):
    A = As[i]
    for v in A:
        Ds[i][v-1] += 1

res = 0
for i in range(N):
    Ki = KAs[i][0]
    for j in range(i+1,N):
        Kj = KAs[j][0]
        res_k = 0
        for k in range(Amax):
            res_k += Ds[i][k]*Ds[j][k]
        res = max(res,res_k/(Ki*Kj))
print(res)