import sys
input = sys.stdin.readline
MOD = 998244353

# A瓷磚4種旋轉對應的(右端點, 下端點)連接情況：
# 右端點: 0或1 (是否有線段端點在右邊中點)
# 下端點: 0或1 (是否有線段端點在下邊中點)
# A瓷磚四種旋轉的(右,下)端點組合：
# 旋轉0: 右=1, 下=0 (連接右-下)
# 旋轉1: 右=0, 下=1 (連接下-左)
# 旋轉2: 右=0, 下=0 (連接左-上)
# 旋轉3: 右=1, 下=1 (連接上-右)
# 但題意中A瓷磚連接的是相鄰邊中點，四種旋轉分別是：
# 右下, 下左, 左上, 上右
# 右端點是否有線段端點 = 1當且僅當旋轉是0或3
# 下端點是否有線段端點 = 1當且僅當旋轉是1或3
# 因此A瓷磚的(右,下)端點組合為：
# 0:(1,0), 1:(0,1), 2:(0,0), 3:(1,1)
A_patterns = [(1,0),(0,1),(0,0),(1,1)]

# B瓷磚2種旋轉對應的(右端點, 下端點)連接情況：
# B瓷磚連接相對邊中點，兩種旋轉：
# 旋轉0: 連接上下 => 右端點=0, 下端點=1
# 旋轉1: 連接左右 => 右端點=1, 下端點=0
B_patterns = [(0,1),(1,0)]

# 對每個瓷磚類型，列出所有可能的(右端點, 下端點)組合及其旋轉數量
# A有4種旋轉，B有2種旋轉
# 但同一(右,下)組合可能有多個旋轉對應，計數旋轉數量
from collections import Counter
A_count = Counter(A_patterns)  # { (right,down): count }
B_count = Counter(B_patterns)

def solve_case(H, W, S):
    # 對每個格子，我們有該瓷磚類型的所有可能(右端點, 下端點)組合及其旋轉數量
    # 我們要找出所有(右端點陣列, 下端點陣列)的組合，使得：
    # 對每行i，對每列j：
    # 右端點[i][j] == 左端點[i][(j+1)%W]
    # 下端點[i][j] == 上端點[(i+1)%H][j]
    #
    # 由於是環面，左右和上下邊界是環繞的。
    #
    # 觀察條件：
    # 右端點[i][j] = 左端點[i][(j+1)%W]
    # 下端點[i][j] = 上端點[(i+1)%H][j]
    #
    # 但左端點[i][j] = 右端點[i][(j-1)%W]
    # 上端點[i][j] = 下端點[(i-1)%H][j]
    #
    # 因此：
    # 右端點[i][j] = 右端點[i][j] (自洽)
    # 下端點[i][j] = 下端點[i][j] (自洽)
    #
    # 這表示右端點在每行是環狀一致的，且下端點在每列是環狀一致的。
    #
    # 換句話說：
    # 對每行i，右端點[i][j]在j方向必須一致（因為右端點[i][j] = 左端點[i][(j+1)%W] = 右端點[i][j]）
    # 對每列j，下端點[i][j]在i方向必須一致。
    #
    # 因此：
    # 每行的右端點必須全相同（0或1）
    # 每列的下端點必須全相同（0或1）
    #
    # 現在問題簡化為：
    # 對每個格子(i,j)，瓷磚的(右端點, 下端點)必須等於 (row_right[i], col_down[j])
    # 且瓷磚類型S[i][j]的旋轉中必須有一個(右端點, 下端點)等於(row_right[i], col_down[j])
    #
    # 我們要計算所有(row_right陣列, col_down陣列)的組合，使得所有格子都能找到對應旋轉，
    # 並計算旋轉數量乘積。
    #
    # row_right有2^H種可能（每行0或1）
    # col_down有2^W種可能（每列0或1）
    #
    # 但H,W最大可達10^6，暴力不行。
    #
    # 觀察：
    # 對每行i，row_right[i]只能是0或1
    # 對每列j，col_down[j]只能是0或1
    #
    # 對每格子(i,j)，瓷磚類型為A或B
    # 我們有該瓷磚類型的(右端點, 下端點)可能值集合
    #
    # 對該格子，(row_right[i], col_down[j])必須在該瓷磚的可能值集合中
    #
    # 因此：
    # 對每格子(i,j)，(row_right[i], col_down[j]) ∈ allowed_set(S[i][j])
    #
    # 這是對(row_right[i], col_down[j])的限制。
    #
    # 這種限制是對row_right[i]和col_down[j]的二元約束。
    #
    # 我們可以將問題看成：
    # 對row_right和col_down的二元變數，找出所有滿足條件的組合數。
    #
    # 由於row_right[i]和col_down[j]都是0或1，且每格子限制(row_right[i], col_down[j]) ∈ allowed_set，
    # 這是典型的二分圖二元變數約束問題。
    #
    # 進一步分析：
    # 對每格子(i,j)，allowed_set是該瓷磚類型的(右,下)端點集合：
    # A瓷磚allowed_set = {(1,0),(0,1),(0,0),(1,1)} = 全部4種
    # B瓷磚allowed_set = {(0,1),(1,0)}
    #
    # 因此：
    # A瓷磚不限制(row_right[i], col_down[j])，因為四種組合都可
    # B瓷磚限制(row_right[i], col_down[j]) ∈ {(0,1),(1,0)}，即row_right[i] != col_down[j]
    #
    # 總結：
    # 對A瓷磚格子無限制
    # 對B瓷磚格子(row_right[i], col_down[j])必須不同
    #
    # 問題簡化為：
    # 找row_right和col_down的0/1陣列，使得對所有B瓷磚格子(i,j)，row_right[i] != col_down[j]
    #
    # 這是對(row_right, col_down)的二分圖邊的異或約束。
    #
    # 這種約束可用圖論分析：
    # 對B瓷磚格子(i,j)建立邊(i,j)要求row_right[i] != col_down[j]
    #
    # row_right是左邊集合，col_down是右邊集合
    #
    # 我們要計算有多少(row_right, col_down)的0/1賦值，使得所有B瓷磚邊的兩端值不同。
    #
    # 這是二分圖的二色性約束：
    # 對B瓷磚邊，兩端必須不同顏色
    #
    # 因此，row_right和col_down的賦值是該二分圖的二色塗色方案。
    #
    # 但row_right和col_down是0/1值，且邊要求兩端不同。
    #
    # 這個二分圖必須是二分的（沒有奇環），否則無解。
    #
    # 計算方案數：
    # 對每個連通分量：
    # - 如果該分量中有頂點，則有2種二色塗色方式（顏色0或1可反轉）
    # - 但row_right和col_down的值決定了瓷磚旋轉數量
    #
    # 另外，A瓷磚格子不限制，對旋轉數量影響是4種旋轉都可用
    #
    # 現在計算旋轉數量：
    # 對每格子(i,j)：
    # - row_right[i], col_down[j]確定(右端點, 下端點)
    # - 該瓷磚類型S[i][j]中有多少旋轉對應該(右,下)組合？
    #
    # 對A瓷磚：
    # A_patterns = [(1,0),(0,1),(0,0),(1,1)]
    # 每種(右,下)組合對應1種旋轉，總4種旋轉
    # 因此每個(右,下)組合對應1種旋轉
    #
    # 對B瓷磚：
    # B_patterns = [(0,1),(1,0)]
    # 每種(右,下)組合對應1種旋轉
    #
    # 因此每格子旋轉數量 = 1（因為(右,下)組合唯一對應1種旋轉）
    #
    # 但題目說A瓷磚有4種旋轉，B瓷磚有2種旋轉，旋轉數量是4^a * 2^b
    # 但在符合條件的放置中，旋轉被(右,下)端點唯一確定
    #
    # 因此旋轉數量 = 1（因為旋轉被(右,下)端點唯一確定）
    #
    # 但題目要求計算所有滿足條件的放置方式數量
    #
    # 由於row_right和col_down的賦值決定了每格子旋轉唯一
    #
    # 因此方案數 = 符合row_right和col_down條件的賦值數量
    #
    # 另外，對A瓷磚格子，(右,下)組合有4種旋轉，但只有1種旋轉對應該(右,下)組合
    # 因此旋轉數量是1
    #
    # 總結：
    # 方案數 = 符合row_right和col_down條件的賦值數量
    #
    # 計算符合條件的賦值數量：
    # 對B瓷磚建立二分圖邊，要求兩端顏色不同
    # 若圖非二分，方案數為0
    # 否則，對每個連通分量有2種二色塗色方式
    # 對不含B瓷磚的行或列，row_right或col_down可自由0或1
    #
    # 但題目中所有格子都在圖中，因為B瓷磚邊只連接行和列
    #
    # 需要考慮孤立的行或列（沒有B瓷磚連接）
    #
    # 對孤立行，row_right[i]可自由0或1 => 2種
    # 對孤立列，col_down[j]可自由0或1 => 2種
    #
    # 對連通分量，2種二色塗色方式
    #
    # 因此：
    # 方案數 = 2^(孤立行數 + 孤立列數 + 連通分量數)
    #
    # 其中連通分量是B瓷磚邊構成的二分圖的連通分量數
    #
    # 實作：
    # - 建立二分圖，左邊為行，右邊為列
    # - 邊為B瓷磚格子(i,j)
    # - 用並查集或DFS找連通分量
    # - 判斷是否二分
    # - 計算孤立行和孤立列數
    #
    # 注意：
    # 行和列的節點編號分開，行0..H-1，列0..W-1
    # 並查集或圖遍歷時要區分左右集合
    
    # 建立圖
    # 左邊節點: 0..H-1 (行)
    # 右邊節點: 0..W-1 (列)
    # 邊: B瓷磚(i,j)
    
    # 用鄰接表存圖，左右節點分開
    # 但為方便，將列節點編號偏移H，整體節點數為H+W
    # 節點0..H-1為行，節點H..H+W-1為列
    
    n = H + W
    adj = [[] for _ in range(n)]
    row_has_edge = [False]*H
    col_has_edge = [False]*W
    
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'B':
                u = i
                v = H + j
                adj[u].append(v)
                adj[v].append(u)
                row_has_edge[i] = True
                col_has_edge[j] = True
    
    color = [-1]*n
    def dfs(u, c):
        color[u] = c
        for w in adj[u]:
            if color[w] == -1:
                if not dfs(w, c^1):
                    return False
            else:
                if color[w] == color[u]:
                    return False
        return True
    
    visited = [False]*n
    components = 0
    for i in range(n):
        if (i < H and row_has_edge[i]) or (i >= H and col_has_edge[i - H]):
            if color[i] == -1:
                if not dfs(i, 0):
                    return 0
                components += 1
    
    # 計算孤立行和孤立列數
    isolated_rows = sum(1 for i in range(H) if not row_has_edge[i])
    isolated_cols = sum(1 for j in range(W) if not col_has_edge[j])
    
    # 方案數 = 2^(components + isolated_rows + isolated_cols)
    # 因為：
    # - 每個連通分量有2種二色塗色方式
    # - 每個孤立行自由0/1 => 2種
    # - 每個孤立列自由0/1 => 2種
    
    ans = pow(2, components + isolated_rows + isolated_cols, MOD)
    return ans

T = int(input())
for _ in range(T):
    H,W = map(int,input().split())
    S = [input().strip() for __ in range(H)]
    print(solve_case(H,W,S))