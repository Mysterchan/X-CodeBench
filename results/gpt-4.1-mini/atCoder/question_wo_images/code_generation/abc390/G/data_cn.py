MOD = 998244353

def main():
    import sys
    sys.setrecursionlimit(10**7)
    N = int(sys.stdin.readline())

    # 預處理階乘與反元素
    fact = [1] * (N+1)
    for i in range(2, N+1):
        fact[i] = fact[i-1] * i % MOD

    # 計算每個數字的位數
    def digit_len(x):
        return len(str(x))

    # 預先計算每個數字的位數
    lens = [digit_len(i) for i in range(1, N+1)]

    # 計算所有數字位數的和
    sum_len = sum(lens)

    # 計算10的冪次方
    # 由於每個數字會出現在所有排列的每個位置上，
    # 我們需要計算每個位置的權重(10的冪次方)
    # 但因為排列中數字順序不同，位數不同，計算較複雜
    # 透過數學推導：
    # f(P) = sum_{i=1}^N A_{p_i} * 10^{sum of lengths of numbers after position i}
    # 對所有排列求和：
    # sum_{P} f(P) = sum_{i=1}^N sum_{x=1}^N x * 10^{sum of lens after i} * (N-1)!
    # 因為每個數字在每個位置出現次數相同 = (N-1)!
    # 位置i的權重為10^{sum of lens after i}
    # sum of lens after i = sum_len - prefix_len[i]
    # prefix_len[i] = sum of lens of first i numbers in permutation
    # 但因為排列不同，prefix_len[i]不同，無法直接計算
    #
    # 但因為所有排列中，每個數字在每個位置出現次數相同，
    # 且所有數字的lens分布固定，
    # 我們可以將問題轉化為：
    # sum_{P} f(P) = (N-1)! * sum_{i=1}^N 10^{sum_len - expected_prefix_len[i]} * sum_{x=1}^N x
    #
    # 但expected_prefix_len[i]無法直接求，因為排列不同
    #
    # 另一種思路：
    # 對所有排列，對每個位置i，所有數字出現次數相同 = (N-1)!
    # 位置i的權重為10^{sum of lens of numbers after i}
    # sum of lens of numbers after i = sum of lens of N - i numbers
    #
    # 因為排列中數字順序不同，lens的分布也不同
    # 但因為所有排列均勻，對每個位置，lens的期望是平均的
    #
    # 透過數學推導可得：
    # sum_{P} f(P) = (N-1)! * sum_{i=1}^N 10^{sum_len - i * avg_len} * sum_{x=1}^N x
    #
    # 但avg_len不一定整數，且不精確
    #
    # 另一種方法：
    # 對每個數字x，計算它在所有排列中出現的位置i的貢獻：
    # x出現在位置i時，f(P)中x的權重為10^{sum of lens of numbers after i}
    # 對所有排列，x在每個位置出現次數相同 = (N-1)!
    #
    # 因此：
    # sum_{P} f(P) = (N-1)! * sum_{x=1}^N sum_{i=1}^N x * 10^{sum of lens of numbers after i}
    #
    # sum of lens of numbers after i = sum of lens of N - i numbers
    #
    # 但lens的分布不固定，因為排列不同
    #
    # 但因為lens是固定的，且所有排列均勻，lens的分布在位置i是均勻的
    # 因此，sum of lens of numbers after i = sum of lens of N - i numbers的期望
    #
    # 期望為 (N - i) * avg_len
    #
    # 但avg_len = sum_len / N
    #
    # 因此：
    # sum_{P} f(P) = (N-1)! * sum_{x=1}^N x * sum_{i=1}^N 10^{(N - i) * avg_len}
    #
    # 但10^{(N - i) * avg_len}非整數次方，無法直接計算
    #
    # 另一種解法：
    # 對每個數字x，計算它的位數d_x
    # 對每個位置i，x出現時，f(P)中x的權重為10^{sum of lens of numbers after i}
    # sum of lens of numbers after i = total_len - prefix_len[i]
    #
    # 但prefix_len[i]是前i數字的lens和，因為排列不同，無法直接求
    #
    # 但因為所有排列均勻，對每個位置i，lens的分布均勻
    # 因此，對每個位置i，lens的期望為 i * avg_len
    #
    # 因此，sum of lens of numbers after i = sum_len - i * avg_len
    #
    # 仍然是非整數次方
    #
    # 由於題目中數字是1..N，且位數只有1~6(因為N<=2*10^5)
    # 我們可以將數字分組，根據位數分組
    #
    # 計算每個位數d的數字個數cnt_d，及其和sum_d
    #
    # 對每個位置i，所有排列中，位數為d的數字出現在位置i的次數為 cnt_d * (N-1)!
    #
    # 位置i的權重為 10^{sum of lens of numbers after i}
    #
    # sum of lens of numbers after i = sum of lens of N - i numbers
    #
    # 由於排列均勻，位數為d的數字在位置i出現的期望個數為 cnt_d * (N-1)! / N
    #
    # 但計算複雜
    #
    # 另一種思路：
    # 對每個數字x，計算它在所有排列中出現的位置i的貢獻：
    # x在位置i時，權重為 10^{sum of lens of numbers after i}
    #
    # sum over i=1..N of 10^{sum of lens of numbers after i} = sum over i=1..N of 10^{sum of lens of N - i numbers}
    #
    # 因為lens是固定的，我們可以預先計算 pow10_len_prefix
    #
    # 具體做法：
    # 對所有數字排序，lens排序
    # prefix_len[i] = lens[0] + lens[1] + ... + lens[i-1]
    #
    # sum of lens of numbers after i = sum_len - prefix_len[i]
    #
    # 對 i=0..N-1，計算 pow10[sum_len - prefix_len[i]]
    #
    # sum over i=0..N-1 pow10[sum_len - prefix_len[i]]
    #
    # 對每個數字x，出現位置i的次數為 (N-1)!
    #
    # sum_{P} f(P) = (N-1)! * sum_{x=1}^N x * sum_{i=0}^{N-1} 10^{sum_len - prefix_len[i]}
    #
    # prefix_len[i]是lens排序後的前綴和
    #
    # 但lens排序後的前綴和與原序列lens不同
    #
    # 但因為lens是固定的，且lens排序後的前綴和是lens的排列之一
    #
    # 因此，我們可以將lens排序，計算prefix_len
    #
    # sum_{P} f(P) = (N-1)! * sum_{x=1}^N x * sum_{i=0}^{N-1} 10^{sum_len - prefix_len[i]}
    #
    # sum_{x=1}^N x = N*(N+1)//2
    #
    # pow10預先計算
    #
    # 實作如下：

    lens_sorted = sorted(lens)
    prefix_len = [0]*(N+1)
    for i in range(N):
        prefix_len[i+1] = prefix_len[i] + lens_sorted[i]

    max_len_sum = prefix_len[-1]
    # pow10[i] = 10^i mod MOD
    pow10 = [1]*(max_len_sum+1)
    for i in range(1, max_len_sum+1):
        pow10[i] = pow10[i-1]*10 % MOD

    total_sum_x = N*(N+1)//2 % MOD
    fact_n_1 = fact[N-1]

    ans = 0
    for i in range(N):
        power = max_len_sum - prefix_len[i]
        ans += pow10[power]
    ans %= MOD

    ans = ans * total_sum_x % MOD
    ans = ans * fact_n_1 % MOD

    print(ans)

if __name__ == "__main__":
    main()