N, M = map(int,input().split())
A = [map(int, input().split())]

print(N, M)
print(A)
A.sort()
beside_A = []

while len(A) > 0:
    for i in range(1, N+1):
        if len(A) == 0:
            beside_A.append(i)
        elif i != A[0]:
            beside_A.append(i)
        elif i == A[0]:
            A.pop(0)

        if i > N: break

print(len(beside_A))
for num in beside_A:
    print(num, end=" ")