from math import gcd
from functools import reduce
from operator import mul

MOD = 998244353

def lcm(a, b):
    return a * b // gcd(a, b)

def get_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

def get_lcms(a, b):
    lcms = set()
    for p in get_divisors(a):
        for q in get_divisors(b):
            if p * q == a:
                lcms.add(lcm(p, q))
    return lcms

def main():
    n = int(input())
    a = list(map(int, input().split()))

    lcms = [get_lcms(a[0], a[i]) for i in range(1, n - 1)]

    scores = [1]
    for lcms_i in lcms:
        new_scores = []
        for score in scores:
            for lcm in lcms_i:
                new_scores.append(score * lcm)
        scores = new_scores

    ans = 0
    for score in scores:
        ans += reduce(mul, [score] + list(map(lambda x: x // gcd(score, x), a)), 1)
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()