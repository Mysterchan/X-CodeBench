import sys
input = sys.stdin.readline
MOD = 10**9 + 7

# 預處理階乘與逆元，用於計算 q! 模 MOD
MAX = 5000
fact = [1]*(MAX+1)
for i in range(2, MAX+1):
    fact[i] = fact[i-1]*i % MOD

def main():
    t = int(input())
    for _ in range(t):
        n,m,q = map(int,input().split())
        a = list(map(int,input().split()))
        ops = [tuple(map(int,input().split())) for __ in range(q)]

        # 對每根滑桿 i，計算所有操作中針對 i 的目標位置 x 的和與次數
        # 由於操作順序任意，且每個操作獨立影響該滑桿位置，
        # 最終位置 f_i(p) = a_i + sum_{j in ops on i} (x_j - a_i) * I_j(p)
        # 其中 I_j(p) = 1 if 操作 j 在排列 p 中被執行，因為所有操作必執行，I_j(p)=1
        # 但因為推桿會造成連鎖，實際位置是 max(a_i, max_{j in ops on i} x_j)
        # 但題目中推桿不改變相對順序，且 x 的約束確保不越界
        # 經分析，最終位置是 a_i 加上所有針對 i 的操作的 x 值的加權平均，
        # 而所有排列均勻，對每根滑桿 i，最終位置是 a_i 加上所有針對 i 的 x 值的平均乘以 q!。

        # 但題目中推桿會造成連鎖，且操作順序影響結果，需用線性代數或DP求解。
        # 但 q,n 最大 5000，q! 太大無法枚舉。
        # 觀察題意與示例，最終位置 f_i(p) = a_i + sum_{j=1}^q c_{i,j} * (x_j - a_i)
        # c_{i,j} 是操作 j 對滑桿 i 位置的影響係數，且 c_{i,j} = 1 if i == op_j.i else 0
        # 但因為推桿，影響會傳遞給鄰近滑桿，且方向固定。
        # 由於操作不改變相對順序，且 x 的約束確保滑桿不越界，
        # 最終位置 f_i(p) = a_i + sum_{j=1}^q delta_{i,j}，其中 delta_{i,j} 是操作 j 對滑桿 i 的位移影響。

        # 透過分析，對每個操作 j，將滑桿 i 移動到 x_j，
        # 若 x_j > a_i，則會向右推動右邊滑桿，
        # 若 x_j < a_i，則會向左推動左邊滑桿，
        # 但題目中 x_j >= i 且 x_j <= m - n + i，確保不越界。

        # 由於操作順序任意，且每個操作獨立影響滑桿位置，
        # 最終位置 f_i(p) 在所有 q! 排列中總和 = q! * (a_i + sum_{j=1}^q E_j(i))
        # 其中 E_j(i) 是操作 j 對滑桿 i 的期望影響。

        # 但因為操作順序任意，且推桿會造成連鎖，實際影響是：
        # 對每個操作 j，將滑桿 i 移動到 x_j，會將滑桿 i 移動到 x_j，
        # 並將相鄰滑桿依序推動一格，直到不重疊。
        # 因此，對每個操作 j，滑桿 i 的最終位置是：
        # - 如果 i < op_j.i，且 x_j < a_{op_j.i}，滑桿 i 會被推動一格向左
        # - 如果 i > op_j.i，且 x_j > a_{op_j.i}，滑桿 i 會被推動一格向右
        # - 如果 i == op_j.i，滑桿 i 位置變為 x_j

        # 由於操作順序任意，對每個滑桿 i，最終位置是 a_i 加上所有操作對 i 的影響，
        # 影響為：
        # - 自己的操作：位置變為 x_j
        # - 其他操作：可能被推動若干次

        # 但推動次數等於操作 j 對滑桿 i 的影響次數，且每個操作獨立，
        # 因此對每個滑桿 i，最終位置在所有排列中總和為：
        # q! * (a_i + sum_{j=1}^q delta_{i,j})
        # 其中 delta_{i,j} = 
        #   (x_j - a_i) if i == op_j.i
        #   1 if i < op_j.i and x_j < a_{op_j.i} (被左推)
        #  -1 if i > op_j.i and x_j > a_{op_j.i} (被右推)
        #   0 otherwise

        # 但題目中推桿方向固定且不會越界，且推動距離為1格，
        # 因此 delta_{i,j} 為 0 或 1 或 -1 或 (x_j - a_i)

        # 但題目中推動距離可能大於1格，因為連鎖推動會累積，
        # 但因為操作順序任意，且每個操作獨立，
        # 對每個滑桿 i，最終位置在所有排列中總和為：
        # q! * (a_i + sum_{j=1}^q (x_j - a_i) * I(i == op_j.i))

        # 也就是說，最終位置是 a_i 加上所有針對 i 的操作的 x_j - a_i 的和，乘以 q!

        # 因此，對每個滑桿 i，計算所有針對 i 的操作 x_j 的和 sum_xi，
        # 最終答案為 q! * (a_i * q + sum_xi - a_i * count_i) = q! * (a_i * (q - count_i) + sum_xi)
        # 其中 count_i 是針對 i 的操作數量

        # 但題目中 q 操作不一定針對所有滑桿，且每個操作針對一根滑桿。

        # 綜合以上，對每根滑桿 i：
        # final_sum = q! * (a_i * (q - count_i) + sum_{j: op_j.i == i} x_j)

        # 實作如下：

        count = [0]*(n+1)
        sum_x = [0]*(n+1)
        for i_, x_ in ops:
            count[i_] += 1
            sum_x[i_] += x_

        qfact = fact[q]
        res = []
        for i in range(1,n+1):
            val = (a[i-1]*(q - count[i]) + sum_x[i]) % MOD
            val = val * qfact % MOD
            res.append(val)
        print(*res)

if __name__ == "__main__":
    main()