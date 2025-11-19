import sys
input = sys.stdin.readline

# Precompute Fibonacci numbers up to n=10 (1-based indexing)
fs = [0, 1, 2]
for i in range(3, 11):
    fs.append(fs[i-1] + fs[i-2])

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    fn = fs[n]
    fn_1 = fs[n-1]

    res = []
    for __ in range(m):
        w, l, h = map(int, input().split())
        dims = sorted([w, l, h], reverse=True)
        # dims[0] >= dims[1] >= dims[2]
        # Check if largest dimension >= f_n and the other two >= f_{n-1}
        if dims[0] >= fn and dims[1] >= fn_1 and dims[2] >= fn_1:
            res.append('1')
        else:
            res.append('0')
    print(''.join(res))