def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    NK = N * K

    # 目標是將 P 排序成 (1, 2, ..., NK)
    # 操作是交換 P[i], P[j]，若 |i-j| 是 N 的倍數，得 1 分
    # 要在最少操作數下排序，且最大化得分

    # 分析：
    # 位置分成 N 個模 N 的類別：位置 i 屬於 i % N 的類別
    # 交換得分的條件是 |i-j| % N == 0，表示只能在同一類別內交換得分
    # 不同類別間交換不會得分

    # 因此，整體排列可視為 N 個獨立的子序列，每個子序列長度 K：
    # 子序列 c (0 <= c < N) 包含位置 i 使 i % N == c 的元素
    # 目標排序後，子序列 c 應該是元素 c+1, c+1+N, c+1+2N, ..., c+1+(K-1)*N

    # 對每個子序列，我們要將其元素排序成目標子序列
    # 在子序列內交換可得分，跨子序列交換不會得分

    # 最少操作數排序一個子序列的排列，等於該子序列排列的 cycle decomposition 中
    # 所有 cycle 長度減 1 的和 (即子序列長度 - cycle 數)
    # 但我們要最大化得分，得分來自於在同一子序列內的交換

    # 由於跨子序列交換不會得分，且最少操作數是固定的，
    # 我們應該盡量在子序列內完成交換，避免跨子序列交換。

    # 事實上，整體排列的 cycle 會跨越多個子序列，
    # 跨子序列交換不會得分，但可以減少操作數。
    # 但題目要求最少操作數下最大化得分，
    # 因此我們不能犧牲操作數來換取得分。

    # 結論：
    # 最少操作數是整體排列的 cycle decomposition 的 (NK - cycle數)
    # 最大得分是在這些操作中，能在同一子序列內交換的次數最大化。

    # 透過分析，最大得分等於所有子序列內 cycle decomposition 的 (子序列長度 - cycle數) 之和
    # 因為每個子序列內的 cycle 數決定了該子序列內最少交換數，
    # 這些交換都能得分。

    # 實作：
    # 1. 將排列 P 分成 N 個子序列，每個子序列長度 K
    # 2. 對每個子序列計算 cycle 數
    # 3. 得分 = sum(子序列長度 - cycle數) = N*K - sum(子序列cycle數)

    # 計算 cycle 數的方法：
    # 對子序列建立映射：位置 -> 目標位置
    # 目標子序列是排序後的子序列 (1-based: c+1, c+1+N, ...)
    # 但因為元素是 1..NK，且子序列 c 的目標元素是 c+1 + N * idx
    # 我們可以用元素值來判斷目標位置

    # 具體：
    # 子序列 c 的元素索引是 0..K-1
    # 子序列 c 的目標元素是 c+1 + N * idx (idx=0..K-1)
    # 對子序列內元素建立映射：當前元素 -> 目標位置索引

    # 但更簡單的是：
    # 對子序列 c，建立一個長度 K 的排列 arr_sub
    # arr_sub[i] = (P[pos] - (c+1)) // N
    # 這是元素在子序列中的目標位置
    # 目標排列是 [0,1,2,...,K-1]
    # arr_sub 是當前排列，求 cycle 數

    # cycle 數 = K - 最少交換數

    # 最後得分 = sum(最少交換數) = sum(K - cycle數) = N*K - sum(cycle數)

    # 計算 cycle 數的函數
    def count_cycles(arr):
        visited = [False]*len(arr)
        cycles = 0
        for i in range(len(arr)):
            if not visited[i]:
                cycles += 1
                cur = i
                while not visited[cur]:
                    visited[cur] = True
                    cur = arr[cur]
        return cycles

    total_cycles = 0
    for c in range(N):
        arr_sub = []
        for i in range(K):
            pos = c + N*i
            val = P[pos]
            # 計算 val 在子序列中的目標位置
            # val = c+1 + N * idx
            idx = (val - (c+1)) // N
            arr_sub.append(idx)
        total_cycles += count_cycles(arr_sub)

    # 得分 = N*K - total_cycles
    print(N*K - total_cycles)


if __name__ == "__main__":
    main()