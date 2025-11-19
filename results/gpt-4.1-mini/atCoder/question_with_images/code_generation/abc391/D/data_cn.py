import sys
input = sys.stdin.readline

N, W = map(int, input().split())
blocks = [None]*(N+1)
col_blocks = [[] for _ in range(W+1)]

for i in range(1, N+1):
    x, y = map(int, input().split())
    blocks[i] = (x, y)
    col_blocks[x].append((y, i))

# 對每列方塊按高度排序（由低到高）
for c in range(1, W+1):
    col_blocks[c].sort()

# 計算每列的底部行高度（即該列方塊數量）
col_heights = [len(col_blocks[c]) for c in range(W+1)]

# 底部行高度 = min(每列方塊數量)
# 因為底部行被填滿時會消除，消除後所有方塊往下掉一層，等同於整體往下移動一層
# 消除次數 = min_col_height

min_col_height = min(col_heights)

# 消除次數 = min_col_height
# 消除時間分別是 1,2,...,min_col_height
# 消除後方塊高度減 min_col_height

# 對每個方塊計算消除時間（消失時間）
# 方塊在消除前的高度 = y
# 消除次數 = min_col_height
# 方塊消失時間 = y - (消除次數) + 1
# 但要注意方塊是否在消除範圍內

# 實際消失時間計算：
# 方塊在時間 t 消失，當 t = y - (消除次數) + 1 <= min_col_height
# 但消除次數是 min_col_height，消除時間是 1..min_col_height
# 方塊消失時間 = y - (min_col_height - 1)
# 如果消失時間 <= 0，表示方塊不會被消除（因為消除時間從1開始）

# 但題目中消除是當底部行被填滿時，底部行高度是 min_col_height
# 消除時間是 1..min_col_height
# 方塊消失時間 = y - (min_col_height - 1)
# 如果消失時間 <= 0，表示方塊在時間0就不存在（不可能，因為y>=1）
# 實際上，方塊消失時間 = y - (min_col_height - 1)
# 如果消失時間 > min_col_height，表示方塊不會被消除

# 綜合：
# 方塊消失時間 = y - (min_col_height - 1)
# 若消失時間 <= 0，消失時間 = 1（最早消失）
# 若消失時間 > min_col_height，表示不會消失

# 但根據題意，消除時間是 1..min_col_height
# 方塊消失時間必須在此範圍內才會消失

# 另外，方塊會往下移動，移動距離 = min(T, y-1)
# 方塊高度在時間 T+0.5 是 max(y - T, 1)
# 方塊消失時間是消除行的時間，消除行是底部行高度

# 重新整理思路：

# 1. 底部行高度 = min_col_height
# 2. 消除時間為 1..min_col_height
# 3. 第 k 次消除會移除高度為 k 的行
# 4. 方塊初始高度 y
# 5. 方塊在時間 t 往下移動 t 格，但不會低於 1
# 6. 方塊消失時間是 y - (min_col_height - 1)
#    - 如果 y <= min_col_height，方塊會在時間 y 消失
#    - 否則不會消失

# 因此方塊消失時間 = y if y <= min_col_height else None

# 查詢時：
# 時間 T_j + 0.5
# 方塊是否存在：
# - 若消失時間存在且 <= T_j，方塊已消失，輸出 No
# - 否則輸出 Yes

Q = int(input())
# 預先計算每個方塊消失時間
disappear_time = [None]*(N+1)
for i in range(1, N+1):
    x, y = blocks[i]
    if y <= min_col_height:
        disappear_time[i] = y
    else:
        disappear_time[i] = None

for _ in range(Q):
    T, A = map(int, input().split())
    dt = disappear_time[A]
    if dt is not None and dt <= T:
        print("No")
    else:
        print("Yes")