def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # 根據題意，操作是將一個袋子的石頭全部移到另一袋子，
    # 最終每個袋子要麼是0，要麼是若干袋子石頭的和。
    # 因為石頭是整數且不可拆分，最終的狀態是將N個袋子分成若干組，
    # 每組的石頭數量是該組袋子石頭數的和，其他袋子為0。
    #
    # XOR值 = 所有非零袋子石頭數的XOR。
    #
    # 這等價於從A中選擇一組非空子集，使得該子集的和的XOR值。
    #
    # 但因為可以任意合併袋子，最終的XOR值是所有非空子集和的XOR值集合。
    #
    # 事實上，這問題等價於：
    # 對所有非空子集S，計算 sum_{i in S} A_i 的XOR值，求不同XOR值的數量。
    #
    # 但N最大12，2^N=4096，暴力枚舉所有子集和XOR值是可行的。
    #
    # 但題目說可能值數量有限，且N最大12，暴力枚舉即可。

    possible = set()
    from itertools import combinations

    # 枚舉所有非空子集
    for mask in range(1, 1 << N):
        s = 0
        for i in range(N):
            if mask & (1 << i):
                s ^= A[i]
        possible.add(s)

    print(len(possible))


if __name__ == "__main__":
    main()