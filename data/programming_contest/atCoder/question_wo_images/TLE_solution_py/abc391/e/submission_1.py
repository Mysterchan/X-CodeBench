import sys
import os

sys.setrecursionlimit(10**7)

input = lambda: sys.stdin.readline().rstrip()

filename = r'ABC_391\インプット\_input_E.txt'
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
A = input()

cost = [1]*(3**N)
def turn(i):
    ct = 0
    for j in range(3):
        if A[3*i+j] == "0":
            ct += 1
    if ct >= 2:
        nx_01 = "0"
    else:
        nx_01 = "1"

    cs_m = 0
    nx_cs = 0
    for j in range(3):
        if A[3*i+j] == nx_01:
            cs_m = max(cs_m,cost[3*i+j])
            nx_cs += cost[3*i+j]
    nx_cs -= cs_m
    return nx_01,nx_cs

for n in reversed(range(N)):
    A_new = ""
    cost_new = [0]*(3**n)
    for i in range(3**n):
        nx_01,nx_cs = turn(i)
        A_new = "".join([A_new,nx_01])
        cost_new[i] = nx_cs
    A = A_new
    cost = cost_new
print(cost[0])