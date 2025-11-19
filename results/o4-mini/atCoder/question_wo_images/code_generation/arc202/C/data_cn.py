import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353
MAX = 2 * 10**5

# 预处理最小质因数
spf = [0] * (MAX + 1)
def sieve_spf():
    spf[1] = 1
    for i in range(2, MAX + 1):
        spf[i] = 0
    for i in range(2, int(MAX**0.5) + 1):
        if spf[i] == 0:
            for j in range(i*i, MAX+1, i):
                if spf[j] == 0:
                    spf[j] = i
    for i in range(2, MAX+1):
        if spf[i] == 0:
            spf[i] = i

def factorization(x):
    factors = {}
    while x > 1:
        p = spf[x]
        factors[p] = factors.get(p, 0) + 1
        x //= p
    return factors

def modinv(a, m=MOD):
    # Fermat逆元，MOD为质数
    return pow(a, m-2, m)

def main():
    sieve_spf()
    N = int(input())
    A = list(map(int, input().split()))

    # R_n = (10^n - 1) / 9
    # R_n的质因数分解 = (10^n - 1)/9
    # 9 = 3^2，固定分母，分母不影响LCM，因为所有R_n都除以9，LCM时分母不变，LCM(R_n) = (LCM(10^n -1))/9
    # 计算LCM(R_{A_1},...,R_{A_k}) = LCM((10^{A_i}-1)/9) = (LCM(10^{A_i}-1))/9
    # 由于9固定，最后结果乘以inv(9) mod即可

    # 关键是计算LCM(10^{A_i} - 1)
    # 10^{n} - 1 = ∏_{d|n} Φ_d(10)
    # Φ_d(10)是d阶循环多项式在10处的值，是整数且互质
    # LCM(10^{A_i} - 1) = ∏_{d} Φ_d(10)^{max exponent over all A_i}
    # max exponent = max count of d dividing any A_i

    # 先对所有A_i求因子分解，统计每个d的最大出现次数
    # 但这里d是除数，不是质因数
    # 需要对每个A_i的所有约数d，更新max exponent

    # 由于N和A_i最大2e5，枚举所有约数会超时
    # 优化：
    # 对每个A_i，枚举其所有约数d，更新max_exp[d]
    # 约数枚举复杂度约为O(N * sqrt(A_i))，可行

    max_exp = [0]*(MAX+1)

    # 预处理每个数的质因数分解，方便约数枚举
    # 约数枚举函数
    def get_divisors(x):
        divs = [1]
        f = []
        while x > 1:
            p = spf[x]
            cnt = 0
            while x % p == 0:
                x //= p
                cnt += 1
            f.append((p, cnt))
        def dfs(i):
            if i == len(f):
                return [1]
            res = []
            sub = dfs(i+1)
            p, c = f[i]
            for e in range(c+1):
                for val in sub:
                    res.append(val * (p**e))
            return res
        return dfs(0)

    for a in A:
        divs = get_divisors(a)
        for d in divs:
            if max_exp[d] < 1:
                max_exp[d] = 1

    # 由于每个A_i只出现一次，max exponent为1即可
    # 但题目中没有重复A_i的限制，若有重复，max exponent应为出现次数
    # 题目中是序列，逐步计算LCM，需动态更新max_exp

    # 改为动态更新max_exp，记录每个d的出现次数
    # 但题目要求逐步输出LCM(R_{A_1},...,R_{A_k})

    # 方案：
    # 对每个A_i，枚举其约数d，max_exp[d] = max(max_exp[d], count of d in A_1..A_k)
    # 由于每个d的指数为出现次数，且每个A_i出现一次，指数为0或1
    # 但如果A_i重复，指数会增加

    # 题目中A_i为正整数序列，可能重复
    # 所以max_exp[d]为d在前k个A_i中出现的最大次数

    # 由于每个A_i出现一次，max_exp[d]为d出现的次数

    # 但题目中LCM是最小公倍数，不是乘积，指数为最大出现次数
    # 对于每个d，max_exp[d] = max(max_exp[d], count of d in factorization of 10^{A_i}-1)
    # 10^{A_i}-1 = ∏_{d|A_i} Φ_d(10)
    # Φ_d(10)的指数为1，因为10^{A_i}-1中Φ_d(10)出现一次

    # 所以max_exp[d] = 1 if d divides any A_i in first k, else 0

    # 因此，max_exp[d] = 1 if d divides any A_i in first k, else 0

    # 维护一个布尔数组，记录d是否出现过

    # 计算LCM(10^{A_i}-1) = ∏_{d} Φ_d(10)^{max_exp[d]}，max_exp[d] ∈ {0,1}

    # 关键是如何计算Φ_d(10) mod MOD

    # 计算Φ_d(10)：
    # Φ_n(x) = ∏_{d|n} (x^d -1)^{μ(n/d)}
    # μ为莫比乌斯函数

    # 预处理莫比乌斯函数mu

    mu = [1]*(MAX+1)
    is_prime = [True]*(MAX+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, MAX+1):
        if is_prime[i]:
            for j in range(i*2, MAX+1, i):
                is_prime[j] = False

    mu = [1]*(MAX+1)
    for i in range(2, MAX+1):
        if spf[i//spf[i]] == spf[i]:
            mu[i] = 0
        else:
            mu[i] = -mu[i//spf[i]]

    # 计算Φ_n(10) mod MOD
    # Φ_n(10) = ∏_{d|n} (10^d -1)^{μ(n/d)}

    # 预先计算pow10[d] = 10^d mod MOD
    pow10 = [1]*(MAX+1)
    for i in range(1, MAX+1):
        pow10[i] = (pow10[i-1]*10) % MOD

    # 计算10^d -1 mod MOD
    def val_10d_1(d):
        return (pow10[d] - 1) % MOD

    # 预处理所有Φ_n(10)
    # 由于N最大2e5，预处理所有Φ_n(10)可行

    phi = [1]*(MAX+1)
    for n in range(1, MAX+1):
        res = 1
        # 枚举n的约数d
        # 枚举约数
        # 约数枚举优化：枚举d从1到sqrt(n)
        # 但这里n最大2e5，直接枚举约数可行
        d_list = []
        i = 1
        while i*i <= n:
            if n % i == 0:
                d_list.append(i)
                if i*i != n:
                    d_list.append(n//i)
            i += 1
        res = 1
        for d in d_list:
            e = mu[n//d]
            if e == 0:
                continue
            base = val_10d_1(d)
            if e == 1:
                res = (res * base) % MOD
            else:
                inv = modinv(base)
                res = (res * inv) % MOD
        phi[n] = res

    # 现在维护max_exp[d] = 0/1，表示d是否出现过
    # 对于每个A_i，枚举其约数d，max_exp[d] = 1

    # 维护当前LCM值
    # LCM = ∏_{d} phi[d]^max_exp[d] mod MOD

    # 初始LCM = 1
    # 每次加入A_i，枚举约数d
    # 如果max_exp[d] == 0:
    #   max_exp[d] = 1
    #   LCM = LCM * phi[d] mod MOD

    # 最后LCM(R_{A_1},...,R_{A_k}) = LCM(10^{A_i}-1)/9 mod MOD
    # 9的逆元inv9 = modinv(9)
    # 输出 LCM * inv9 % MOD

    inv9 = modinv(9)

    max_exp = [0]*(MAX+1)
    LCM = 1

    for a in A:
        divs = get_divisors(a)
        for d in divs:
            if max_exp[d] == 0:
                max_exp[d] = 1
                LCM = (LCM * phi[d]) % MOD
        ans = (LCM * inv9) % MOD
        print(ans)

if __name__ == "__main__":
    main()