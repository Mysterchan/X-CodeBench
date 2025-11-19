def ril():
    return map(int, input().split())

T = int(input())
output = []

for _ in range(T):
    n, M = ril()
    A = sorted(ril())
    B = sorted(ril())
    
    # Calculate optimal pairs
    max_val = 0
    for i in range(n):
        max_val = max(max_val, (A[i] + B[n - 1 - i]) % M)

    output.append(str(max_val))

print("\n".join(output))