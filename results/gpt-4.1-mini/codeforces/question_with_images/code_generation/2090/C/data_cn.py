import sys
input = sys.stdin.readline

# 解析距離與座標關係：
# 桌子單元格為 (3x+1, 3y+1), (3x+1, 3y+2), (3x+2, 3y+1), (3x+2, 3y+2)
# 走廊為其他格子，客人只能走走廊格子，最後一步移動到相鄰的桌子單元格。
# 起點為 (0,0)，距離定義為最短步數。
# 走廊格子為非桌子格子，且鄰接走廊格子可移動。
# 桌子格子距離可由走廊格子鄰接推算。

# 觀察距離計算：
# 走廊格子為非桌子格子，桌子格子在3x+1或3x+2行列。
# 走廊格子在3x或3x+3行列。
# 起點(0,0)為走廊格子。
# 移動只能在走廊格子中，最後一步移動到相鄰桌子格子。

# 由於桌子格子分布規律，距離可用公式計算：
# 桌子格子 (X,Y) 距離 = X + Y - 1
# 例如 (1,1) 距離 = 1+1-1=1
# 但題目範例中距離是2，表示距離定義是步數，起點(0,0)到(1,1)需2步。
# 因此距離 = X + Y

# 但因為只能走走廊格子，且最後一步移動到桌子格子，距離為走廊格子步數+1。
# 走廊格子距離 = X + Y - 1 (因為走廊格子在3x或3x+3位置)
# 桌子格子距離 = 走廊格子距離 + 1 = X + Y

# 綜合以上，距離 = X + Y

# 桌子格子有四種形態：
# (3x+1, 3y+1), (3x+1, 3y+2), (3x+2, 3y+1), (3x+2, 3y+2)
# 對於固定的 x,y，四個格子距離分別為：
# d1 = 3x+1 + 3y+1 = 3(x+y)+2
# d2 = 3x+1 + 3y+2 = 3(x+y)+3
# d3 = 3x+2 + 3y+1 = 3(x+y)+3
# d4 = 3x+2 + 3y+2 = 3(x+y)+4

# 因此距離分組為 3k+2, 3k+3, 3k+3, 3k+4，k = x+y

# 按距離排序，距離越小優先，距離相同時 x 越小優先，x 相同時 y 越小優先。

# 題目要求：
# t_i=1：選擇最近的空桌子單元格（任一空格子）
# t_i=0：選擇最近的完全未佔用的桌子（四格全空）

# 解法：
# 1. 按距離順序生成桌子單元格序列。
# 2. 對於 t_i=0，選擇最近的未佔用整張桌子（四格全空），佔用四格。
# 3. 對於 t_i=1，選擇最近的空桌子單元格（任一空格子），佔用該格。
# 4. 使用兩個指標分別遍歷 t_i=0 和 t_i=1 的座位分配序列。

# 實作細節：
# - 預先生成足夠多的桌子座位（因為 n 最大 50000，最多需要 50000 桌子）
# - 對於 t_i=0，依序分配整張桌子（四格）
# - 對於 t_i=1，依序分配單格（四格中任一空格）
# - 由於 t_i=1 可選擇任一空格，且距離排序中四格距離不同，故四格視為獨立座位
# - 由於 t_i=0 需整張桌子，故先分配整張桌子，四格都標記佔用
# - t_i=1 分配時跳過已佔用的格子

# 生成座位序列：
# 按距離排序，距離 = 3k + offset (offset in {2,3,4})
# k = x + y
# 對 k 從 0 開始，生成所有 (x,y) 使 x+y=k
# 對每個 (x,y)，生成四個座位，距離分別為 3k+2, 3k+3, 3k+3, 3k+4
# 按距離排序後，依序加入座位列表

# 由於距離排序優先，且 x 越小優先，y 越小優先，生成順序為：
# 對 k 從 0 開始：
#   對 x 從 0 到 k：
#       y = k - x
#       四個座位依距離排序為：
#         (3x+1, 3y+1) 距離 3k+2
#         (3x+1, 3y+2) 距離 3k+3
#         (3x+2, 3y+1) 距離 3k+3
#         (3x+2, 3y+2) 距離 3k+4
# 四個座位中距離相同的兩個座位，x 越小優先，故 (3x+1, 3y+2) 先於 (3x+2, 3y+1)

# 實作時，先生成整張桌子座標，存成列表
# 再生成所有單格座位，存成列表

# 分配策略：
# t_i=0：從整張桌子列表依序分配
# t_i=1：從單格座位列表依序分配，跳過已佔用的格子

# 儲存佔用狀態：
# 使用 set 記錄已佔用的座位

# 輸出每位客人所選座位

MAX_N = 50000

def solve():
    q = int(input())
    # 預先生成足夠多的桌子座位
    # 估計最多需要 n 桌子，n 最大 50000
    # k 最大約為 n，因為每個 k 產生 k+1 桌子
    # 生成桌子直到桌子數 >= MAX_N

    # 生成整張桌子座標列表（四格）
    tables = []  # 每個元素為 [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
    # 生成單格座位列表，元素為 (x,y)
    single_seats = []

    count_tables = 0
    k = 0
    while count_tables < MAX_N:
        for x in range(k+1):
            y = k - x
            # 四格座位
            s1 = (3*x+1, 3*y+1)  # 距離 3k+2
            s2 = (3*x+1, 3*y+2)  # 距離 3k+3
            s3 = (3*x+2, 3*y+1)  # 距離 3k+3
            s4 = (3*x+2, 3*y+2)  # 距離 3k+4
            tables.append([s1,s2,s3,s4])
            # 加入單格座位，依距離排序順序加入
            # 距離排序：s1 < s2 < s3 < s4
            single_seats.append(s1)
            single_seats.append(s2)
            single_seats.append(s3)
            single_seats.append(s4)
            count_tables += 1
            if count_tables >= MAX_N:
                break
        k += 1

    # 兩個指標分別指向 tables 和 single_seats
    table_ptr = 0
    single_ptr = 0
    occupied = set()

    for _ in range(q):
        n = int(input())
        t = list(map(int, input().split()))
        res = [None]*n

        # 重置指標與佔用狀態
        table_ptr = 0
        single_ptr = 0
        occupied.clear()

        for i in range(n):
            if t[i] == 0:
                # 選擇最近的完全未佔用桌子
                while True:
                    if table_ptr >= len(tables):
                        # 理論上不會發生
                        break
                    table = tables[table_ptr]
                    # 檢查四格是否全空
                    if all(pos not in occupied for pos in table):
                        # 佔用四格
                        for pos in table:
                            occupied.add(pos)
                        # 選擇距離最小的格子作為座位（四格中距離最小為第一格）
                        res[i] = table[0]
                        table_ptr += 1
                        break
                    else:
                        table_ptr += 1
            else:
                # 選擇最近的空桌子單元格
                while True:
                    if single_ptr >= len(single_seats):
                        # 理論上不會發生
                        break
                    pos = single_seats[single_ptr]
                    single_ptr += 1
                    if pos not in occupied:
                        occupied.add(pos)
                        res[i] = pos
                        break

        for x,y in res:
            print(x,y)

if __name__ == "__main__":
    solve()