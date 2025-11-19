N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

L1 = []
L2 = []
L3 = []
s = 0

for i in range(N):
    if A[i] == 1:
        s += C[i]
    if A[i] == 1 and B[i] == 0:
        L1.append(C[i])
    elif A[i] == 0 and B[i] == 1:
        L2.append(C[i])
    elif A[i] == 1 and B[i] == 1:
        L3.append(C[i])

L3.sort(reverse=True)
L2.sort()

def compute_cost(a):
    L = L1[:]
    R = L2[:]
    for i in range(a):
        L.append(L3[i])
        R.append(L3[i])
    R.sort()
    L.sort(reverse=True)
    
    p = s
    cost = 0
    for x in L:
        p -= x
        cost += p
    for x in R:
        p += x
        cost += p
    return cost

l = 0
r = len(L3)

while r - l > 2:
    m1 = l + (r - l) // 3
    m2 = r - (r - l) // 3
    
    c1 = compute_cost(m1)
    c2 = compute_cost(m2)
    
    if c1 <= c2:
        r = m2
    else:
        l = m1

result = float('inf')
for a in range(l, r + 1):
    result = min(result, compute_cost(a))

print(result)