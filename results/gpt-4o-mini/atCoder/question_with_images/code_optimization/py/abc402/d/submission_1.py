N, M = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(M)]

def cross(A, B):
    return (A[0] < B[0] < A[1] < B[1]) or (B[0] < A[0] < B[1] < A[1])

intersect_count = 0

for i in range(M):
    for j in range(i + 1, M):
        if cross(lines[i], lines[j]):
            intersect_count += 1

print(intersect_count)