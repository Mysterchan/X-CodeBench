import sys
input = sys.stdin.readline

MOD = 10**9 + 7

t = int(input())
for _ in range(t):
    a,b,k = map(int,input().split())
    # 根據題意和示例分析：
    # 要保證任意 n x m 矩陣中必有 a x b 子矩陣所有元素相等，
    # 且哈希特可用 k 種顏色最優策略避免，
    # 則 n 和 m 必須足夠大，使得無法避免出現該子矩陣。
    #
    # 題目示例和解釋暗示：
    # n = a + (a-1)*(k-1)
    # m = b + (b-1)*(k-1)
    #
    # 這是因為哈希特可以用 k 種顏色交錯排列，避免出現 a 行連續同色和 b 列連續同色，
    # 但當 n 和 m 超過此界限時，必定存在 a x b 的同色子矩陣。
    #
    # 取字典序最小，即先固定 n，再求最小 m。
    # 因此輸出 (n,m) = (a+(a-1)*(k-1), b+(b-1)*(k-1))，並對 MOD 取模。

    n = (a + (a-1)*(k-1)) % MOD
    m = (b + (b-1)*(k-1)) % MOD
    print(n,m)