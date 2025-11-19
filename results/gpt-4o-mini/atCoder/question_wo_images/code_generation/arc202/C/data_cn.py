def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x // gcd(x, y)) * y

MOD = 998244353

n = int(input().strip())
a = list(map(int, input().strip().split()))

current_lcm = 1
results = []

for num in a:
    R_n = int('1' * num)
    current_lcm = lcm(current_lcm, R_n) % MOD
    results.append(current_lcm)

print("\n".join(map(str, results)))