def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 將 A 和 B 中的 -1 記錄下來，方便後續處理
    # 我們的目標是找到一個常數 S，使得對所有 i，有 A_i + B_i = S
    # 且 A_i, B_i >= 0，且可替換 -1 為任意非負整數，且 A 可重新排列

    # 先將 A 和 B 中非 -1 的元素分別記錄
    # 對於已知的 A_i, B_i，A_i + B_i 是固定的（如果兩者都非 -1）
    # 如果兩者都非 -1，則 A_i + B_i 必須等於 S
    # 如果其中一個是 -1，則可以調整該值使得和為 S
    # 如果兩者都是 -1，則可以任意分配使得和為 S

    # 由於 A 可以重新排列，我們可以將 A 排序，B 不動
    # 但因為 A 可以任意重新排列，我們可以將 A 的已知值排序，B 的已知值排序
    # 但更簡單的做法是：
    # 對所有 i，若 A_i != -1 且 B_i != -1，則和必須相同，否則不可能
    # 這些和的值必須一致，否則直接 No

    # 找出所有已知和的值
    known_sums = set()
    for i in range(N):
        if A[i] != -1 and B[i] != -1:
            known_sums.add(A[i] + B[i])
    if len(known_sums) > 1:
        print("No")
        return
    # 如果沒有已知和，則任意 S 都可行，先假設 S = 0
    S_candidates = list(known_sums) if known_sums else [0]

    # 因為 A 可以重新排列，我們可以嘗試所有 S_candidates
    # 但只有一個或沒有，故只需嘗試該 S

    S = S_candidates[0]

    # 現在檢查是否存在一種替換方式，使得所有 A_i, B_i >= 0 且 A_i + B_i = S
    # 且 A 可以重新排列

    # 對於每個 i：
    # - 若 A_i != -1 且 B_i != -1，已檢查過和為 S
    # - 若 A_i == -1 且 B_i != -1，則 A_i = S - B_i，需 A_i >= 0
    # - 若 A_i != -1 且 B_i == -1，則 B_i = S - A_i，需 B_i >= 0
    # - 若 A_i == -1 且 B_i == -1，則可任意分配，只要非負即可，無限制

    # 但因為 A 可以重新排列，我們可以將 A 中已知的值排序，B 中已知的值排序
    # 但更簡單的做法是：
    # 對於所有 i，檢查是否存在非負解

    # 但 A 可以重新排列，意味著我們可以將 A 的已知值任意匹配 B 的已知值
    # 因此，我們可以將 A 中已知值排序，B 中已知值排序
    # 對於 A_i != -1，B_i != -1 的位置已固定，和必須是 S
    # 對於 A_i == -1 或 B_i == -1 的位置，我們可以調整值

    # 但因為 A 可以重新排列，我們可以將 A 的已知值排序，B 的已知值排序
    # 對於 A_i == -1 的位置，我們可以任意賦值
    # 對於 B_i == -1 的位置，我們也可以任意賦值

    # 重要的是，對於所有 i，S - B_i >= 0（若 A_i == -1）
    # 對於所有 i，S - A_i >= 0（若 B_i == -1）

    # 因此，我們嘗試將 A 中已知值排序，B 中已知值排序
    # 對於 A_i == -1 的位置，A_i 可以是任意非負整數
    # 對於 B_i == -1 的位置，B_i 可以是任意非負整數

    # 但因為 A 可以重新排列，我們可以將 A 中已知值排序，B 中已知值排序
    # 並嘗試匹配，使得對所有 i，A_i + B_i = S，且 A_i, B_i >= 0

    # 實際上，我們只需檢查是否存在一個 S，使得：
    # 對所有 i，若 A_i != -1 且 B_i != -1，A_i + B_i = S
    # 對所有 i，若 A_i != -1 且 B_i == -1，則 S - A_i >= 0
    # 對所有 i，若 A_i == -1 且 B_i != -1，則 S - B_i >= 0
    # 對所有 i，若 A_i == -1 且 B_i == -1，無限制

    # 因為 A 可以重新排列，我們可以將 A 中已知值排序，B 中已知值排序
    # 但更簡單的是，因為 A 可以重新排列，我們可以將 A 中已知值排序，B 中已知值排序
    # 並嘗試匹配，使得對所有 i，A_i + B_i = S

    # 但 A 中已知值的數量可能不等於 B 中已知值的數量
    # 因此，我們將 A 中已知值和 B 中已知值分別排序
    # 對於 A 中已知值，B 中未知值，我們可以調整 B_i = S - A_i >= 0
    # 對於 B 中已知值，A 中未知值，我們可以調整 A_i = S - B_i >= 0
    # 對於 A 中未知值，B 中未知值，我們可以任意分配

    # 因此，我們只需檢查：
    # 對所有 A_i != -1，S - A_i >= 0（若 B_i == -1）
    # 對所有 B_i != -1，S - B_i >= 0（若 A_i == -1）

    # 但因為 A 可以重新排列，我們可以將 A 中已知值排序，B 中已知值排序
    # 並嘗試匹配，使得對所有 i，A_i + B_i = S

    # 但更簡單的做法是：
    # 對所有 i，若 A_i != -1 且 B_i != -1，A_i + B_i = S，否則 No
    # 對所有 i，若 A_i != -1 且 B_i == -1，S - A_i >= 0，否則 No
    # 對所有 i，若 A_i == -1 且 B_i != -1，S - B_i >= 0，否則 No
    # 對所有 i，若 A_i == -1 且 B_i == -1，無限制

    # 因為 A 可以重新排列，我們不必考慮 A_i 與 B_i 的原始配對，只需考慮數量和條件

    # 實作如下：

    # 先分別記錄 A 中已知值和未知值數量，B 中已知值和未知值數量
    A_known = [x for x in A if x != -1]
    A_unknown_count = A.count(-1)
    B_known = [x for x in B if x != -1]
    B_unknown_count = B.count(-1)

    # 對於已知和 S，檢查是否存在一種匹配，使得：
    # 對所有 A_known 中的值 a，存在一個 b，使得 a + b = S 且 b >= 0
    # 對所有 B_known 中的值 b，存在一個 a，使得 a + b = S 且 a >= 0

    # 因為 A 可以重新排列，我們可以將 A_known 排序，B_known 排序
    # 嘗試匹配 A_known 和 B_known，使得 a + b = S

    # 但因為 A 和 B 中未知值可以任意賦值，我們可以用未知值來補足差距

    # 具體做法：
    # 對於 A_known 中的每個 a，若 S - a < 0，則不可能
    # 對於 B_known 中的每個 b，若 S - b < 0，則不可能

    # 但因為 A 可以重新排列，我們可以將 A_known 排序，B_known 排序
    # 嘗試匹配，使得對所有 i，a_i + b_i = S

    # 但 A_known 和 B_known 數量可能不等
    # 我們可以將較短的序列補充未知值（視為可任意賦值）

    # 具體步驟：
    # 1. 將 A_known 排序，B_known 排序
    # 2. 若 len(A_known) > len(B_known)，則 B_known 補充 B_unknown_count 個任意值（0）
    #    若 len(B_known) > len(A_known)，則 A_known 補充 A_unknown_count 個任意值（0）
    # 3. 若補充後長度仍不等，則不可能
    # 4. 對於每對 (a, b)，檢查 a + b == S，且 a,b >= 0
    #    若 a 或 b 是補充的未知值，則可調整為 S - 另一方的值，且非負即可
    # 5. 若所有配對都可行，輸出 Yes，否則 No

    # 但因為未知值可任意賦值，我們只需檢查：
    # 對所有已知 a，S - a >= 0
    # 對所有已知 b，S - b >= 0

    # 且未知值數量足夠補足長度差

    # 實作如下：

    # 檢查 S - a >= 0 對所有 a in A_known
    if any(S - a < 0 for a in A_known):
        print("No")
        return
    # 檢查 S - b >= 0 對所有 b in B_known
    if any(S - b < 0 for b in B_known):
        print("No")
        return

    # 補充未知值使兩邊長度相等
    len_A = len(A_known)
    len_B = len(B_known)

    # 未知值數量
    A_unknown = A_unknown_count
    B_unknown = B_unknown_count

    # 補充未知值
    if len_A > len_B:
        diff = len_A - len_B
        if B_unknown < diff:
            print("No")
            return
        B_unknown -= diff
        len_B += diff
    elif len_B > len_A:
        diff = len_B - len_A
        if A_unknown < diff:
            print("No")
            return
        A_unknown -= diff
        len_A += diff

    # 現在 len_A == len_B

    # 剩餘未知值可任意分配，不影響結果

    print("Yes")


if __name__ == "__main__":
    main()