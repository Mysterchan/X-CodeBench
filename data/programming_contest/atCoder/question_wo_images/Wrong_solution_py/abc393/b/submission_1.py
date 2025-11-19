import math
import copy
import string
from collections import Counter
import decimal

def number_input():return int(input())
def number_split():return map(int,input().split())
def number_list():return list(map(int,input().split()))
def number_matrix(N):return [list(map(int,input().split())) for _ in range(N)]
def number_bunkatsu():return [int(digit) for digit in input().strip()]
def strings_input(): return input()
def strings_split(): return input().split()
def strings_list():return list(input().split())
def strings_matrix_list(N): return [list(strings_input()) for _ in range(N)]

def strings_matrix(N):return list([input().split() for _ in range(N)])
def strings_bunkatsu():return list(strings_input())

S=strings_bunkatsu()

ans=0

for i in range(len(S)):
    for j in range(len(S)):
        for k in range(len(S)):
            if j-i==k-j and S[i]=="A" and S[j]=="B" and S[k]=="C":
                ans+=1

print(ans)