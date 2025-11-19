import sys
input = sys.stdin.readline

N, X, Y = map(int, input().split())
S = input().strip()
T = input().strip()

# 觀察操作 A 和 B：
# 操作 A 和 B 都是將長度為 X+Y 的區間內的 0^X 1^Y 與 1^Y 0^X 互換，
# 也就是在該區間內將前 X 個和後 Y 個的 0 和 1 交換位置。
#
# 這種操作本質上是交換一段連續的 0 和 1 的位置，但不會改變整體的 0 和 1 的數量。
#
# 因此，S 和 T 必須有相同的 0 和 1 的數量，否則不可能轉換。
#
# 接著，我們考慮 S 和 T 的結構：
# 將 S 和 T 分解成連續相同字符的區塊（run-length encoding）。
#
# 由於操作只會在長度為 X+Y 的區間內交換 0 和 1 的位置，
# 這意味著在 S 中，0 和 1 的塊可以通過操作在相鄰塊間交換位置，但塊的長度會被拆分或合併。
#
# 但因為操作是交換固定長度的 0^X 和 1^Y，
# 這表示 0 和 1 的塊長度必須能被 X 和 Y 分割成若干段。
#
# 因此，我們對 S 和 T 的 run-length encoding 進行比較：
# - 兩者的塊數必須相同，且塊的字符必須交替相同（0,1,0,1,...）
# - 對於每個塊，長度 mod X (若是 0 塊) 或 mod Y (若是 1 塊) 必須相同，因為操作只能交換整段 X 或 Y 長度的區間。
# - 且每個塊的長度必須能由操作拆分或合併成對方的塊長度。
#
# 但實際上，因為操作是交換固定長度的 0^X 和 1^Y，
# 只要兩者的 run-length encoding 的塊數和塊的字符相同，且每個塊的長度 mod X (0塊) 或 mod Y (1塊) 相同，
# 就可以通過操作達成轉換。
#
# 因為操作可以在塊內部調整 0 和 1 的位置，達成塊長度的調整。
#
# 實作步驟：
# 1. 對 S 和 T 做 run-length encoding，得到 [(char, length), ...]
# 2. 比較兩者塊數和塊的字符是否相同
# 3. 對每個塊，檢查長度 mod X 或 mod Y 是否相同
# 4. 若全部符合，輸出 Yes，否則 No

def run_length_encode(s):
    res = []
    prev = s[0]
    count = 1
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            res.append((prev, count))
            prev = c
            count = 1
    res.append((prev, count))
    return res

rle_s = run_length_encode(S)
rle_t = run_length_encode(T)

if len(rle_s) != len(rle_t):
    print("No")
    sys.exit()

for (c1, l1), (c2, l2) in zip(rle_s, rle_t):
    if c1 != c2:
        print("No")
        sys.exit()
    if c1 == '0':
        if l1 % X != l2 % X:
            print("No")
            sys.exit()
        if l1 < l2:
            # 因為操作只能交換固定長度區間，塊長度不能無限制增加
            # 但實際上，塊長度可以透過多次交換調整，只要餘數相同即可
            # 所以不需判斷大小，只需餘數相同即可
            pass
    else:  # c1 == '1'
        if l1 % Y != l2 % Y:
            print("No")
            sys.exit()

print("Yes")