import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 若序列中沒有0，直接輸出 Yes
if all(x == 1 for x in A):
    print("Yes")
    exit()

# 將序列視為環狀，找出所有連續的0區間
# 先找到第一個0的位置，若無0則已處理
try:
    start = A.index(0)
except ValueError:
    print("Yes")
    exit()

visited = [False]*N
# 找出所有0的區間（環狀）
zero_segments = []
i = start
while True:
    if A[i] == 0 and not visited[i]:
        # 找一段連續0區間
        seg_start = i
        length = 0
        while A[i] == 0 and not visited[i]:
            visited[i] = True
            length += 1
            i = (i+1)%N
        zero_segments.append(length)
    else:
        i = (i+1)%N
    if i == start:
        break

# 若沒有0區間，表示全1，輸出Yes
if not zero_segments:
    print("Yes")
    exit()

# 根據題意，操作是以ARC或CRA三字串為基礎，
# 每次操作可將A_i和A_{i+1}設為1，
# 意味著每次操作可覆蓋連續兩個位置的0。

# 因為字串長度為N，且字串是環狀，
# 我們要判斷是否存在一個字串S，使得所有0都能被覆蓋。

# 觀察操作：
# - 操作以ARC或CRA三字串為基礎，且ARC和CRA是反向的，
# - 兩種操作都會將A_i和A_{i+1}設為1，
# - 因此每次操作可覆蓋兩個相鄰位置。

# 因為字串S是由大寫字母組成，且只要存在一個好的字串即可，
# 我們可以自由選擇S的字母。

# 重要的是，對於每個0區間，我們需要用操作覆蓋所有0。
# 每次操作覆蓋兩個相鄰位置，
# 因此每個0區間長度為L，需要至少ceil(L/2)次操作。

# 但題目沒有限制操作次數，只要存在字串S使得所有0都能被覆蓋。

# 但操作的條件是S_i= A, S_{i+1}= R, S_{i+2}= C 或反向，
# 因此字串S中必須有ARC或CRA的三字串出現，
# 且這三字串的起點i對應的A_i和A_{i+1}可被設為1。

# 因為字串S是環狀，且長度N≥3，
# 我們可以嘗試構造字串S，使得ARC或CRA的三字串出現在所有需要覆蓋的區間。

# 由於ARC和CRA的三字串長度為3，且操作覆蓋兩個相鄰位置，
# 我們可以將字串S設計成重複的ARC或CRA模式，
# 使得每個位置都至少被一個操作覆蓋。

# 例如，字串S = "ARCARCARC..."長度N，
# 對於任意i，S_i,S_{i+1},S_{i+2}是ARC的循環，
# 因此每個位置i都會被某個操作覆蓋。

# 因此，只要序列A中沒有連續的0長度超過N（不可能），
# 且N≥3，理論上都可以用這種字串覆蓋所有0。

# 唯一不行的情況是所有A都是0，因為操作每次只能覆蓋兩個位置，
# 但字串S長度為N，且操作需要ARC或CRA三字串，
# 若全是0，無法透過有限操作全部變1。

# 因此，只要A中不全是0，輸出Yes，否則No。

if all(x == 0 for x in A):
    print("No")
else:
    print("Yes")