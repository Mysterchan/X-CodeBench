import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    U = list(map(int, input().split()))
    D = list(map(int, input().split()))
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))

    # 根據題意，將棋盤全部塗黑的最小成本是：
    # 對於每一行 i (1 <= i <= N-2)，選擇 L_i 和 R_i 配對，成本為 L_i + R_i
    # 對於每一列 j (1 <= j <= N-2)，選擇 U_j 和 D_j 配對，成本為 U_j + D_j
    # 這樣的配對能覆蓋整個棋盤，且不重複使用良好單元格。
    # 因此答案為 sum(L)+sum(R)+sum(U)+sum(D)

    ans = sum(U) + sum(D) + sum(L) + sum(R)
    print(ans)