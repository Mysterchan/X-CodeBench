import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# 梯形定義：四點組合中，有且只有一對對邊平行（平行四邊形、矩形也算梯形）
# 梯形的特徵是存在一對平行邊，且另一對邊不平行（平行四邊形的兩對邊都平行也算梯形）

# 思路：
# 1. 對所有點對(i,j)計算向量的斜率（用約分後的(dx,dy)表示方向）
# 2. 對每個斜率，收集所有點對
# 3. 對每個斜率組合的點對，嘗試配對成梯形的兩條平行邊
# 梯形的兩條平行邊必須是兩組點對，且四點互不重複
# 4. 計算所有平行邊組合數量，扣除平行四邊形（兩對邊都平行）重複計數

# 由於無三點共線，且點不重複，斜率唯一性可保證

# 儲存斜率對應的邊列表
# 斜率用(dx,dy)表示，且dx>=0，dy>=0或dx<0時同時反號，確保唯一表示
def normalize(dx, dy):
    if dx == 0:
        return (0,1)
    if dy == 0:
        return (1,0)
    g = gcd(dx, dy)
    dx //= g
    dy //= g
    if dx < 0:
        dx = -dx
        dy = -dy
    return (dx, dy)

from collections import defaultdict

slope_edges = defaultdict(list)
for i in range(N):
    x1, y1 = points[i]
    for j in range(i+1, N):
        x2, y2 = points[j]
        dx = x2 - x1
        dy = y2 - y1
        s = normalize(dx, dy)
        slope_edges[s].append((i,j))

# 梯形計數：
# 對每個斜率s，edges為所有平行邊
# 從edges中選兩條邊，且四點不重複，組成梯形的平行邊對
# 梯形的另一對邊不平行，若另一對邊也平行，則是平行四邊形，仍算梯形
# 但平行四邊形會在另一斜率中重複計數，需扣除重複

# 計算所有平行邊對數量：
# 對每個斜率，計算edges中兩兩組合，排除有重點的組合

# 計算平行四邊形數量：
# 平行四邊形由兩組平行邊組成，兩組斜率互相垂直或不垂直皆可
# 但平行四邊形的四條邊中有兩對平行邊
# 平行四邊形的四點由兩組平行邊組成，且兩組平行邊的斜率不同
# 所以平行四邊形數量 = 對所有斜率對(s1,s2)，計算兩組邊中四點互不重複且兩組邊平行的組合數

# 實作：
# 1. 計算所有斜率的平行邊對數量 sum_parallel_pairs
# 2. 計算所有平行四邊形數量 sum_parallelograms
# 3. 梯形數 = sum_parallel_pairs - sum_parallelograms

# 優化：
# N=2000，邊數約2000*1999/2=約2,000,000，斜率數量較多
# 直接兩兩比較邊會超時
# 使用點編號集合判斷重複，改用bitset或集合判斷
# 但Python效率有限，需用hash技巧

# 實作細節：
# 對每個斜率，edges列表長度M
# 計算不重複點的邊對數量：
# 總組合數 M*(M-1)//2 - 有重點組合數
# 有重點組合數計算：
# 對每個點，計算該點出現的邊數 c
# 有重點組合數 = sum c*(M-c)
# 但此計算會重複計數，需用組合計算

# 更簡單方法：
# 對每個斜率，edges中點出現次數
# 總組合數 = M*(M-1)//2
# 重複點組合數 = sum over 點 p: C(count_p,2)
# 因為兩條邊若共用點，則這兩條邊不能同時作為梯形的兩條平行邊
# 所以不重複點的邊對數 = 總組合數 - 重複點組合數

# 平行四邊形計算：
# 平行四邊形由兩組平行邊組成，且兩組邊的中點和向量和相同
# 但題目無三點共線，平行四邊形必須是兩組平行邊且兩組邊的中點和向量和相同
# 透過向量和和中點判斷平行四邊形

# 實作平行四邊形計數：
# 對所有邊，計算中點和向量和 (x1+x2, y1+y2, dx, dy)
# 將相同中點和向量和的邊組合起來
# 平行四邊形數量 = sum over key C(count,2)

# 最後梯形數 = sum_parallel_pairs - sum_parallelograms

# 實作如下：

# 計算平行邊對數
total_parallel_pairs = 0
for s, edges in slope_edges.items():
    M = len(edges)
    if M < 2:
        continue
    # 計算每個點出現次數
    count = [0]*N
    for (a,b) in edges:
        count[a] += 1
        count[b] += 1
    total_pairs = M*(M-1)//2
    overlap_pairs = 0
    for c in count:
        if c >= 2:
            overlap_pairs += c*(c-1)//2
    total_parallel_pairs += total_pairs - overlap_pairs

# 計算平行四邊形數量
# key = (x1+x2, y1+y2, dx, dy)
parallelogram_map = defaultdict(int)
for s, edges in slope_edges.items():
    dx, dy = s
    for (a,b) in edges:
        x1, y1 = points[a]
        x2, y2 = points[b]
        mx = x1 + x2
        my = y1 + y2
        # 方向向量固定為(dx, dy)
        parallelogram_map[(mx, my, dx, dy)] += 1

total_parallelograms = 0
for v in parallelogram_map.values():
    if v >= 2:
        total_parallelograms += v*(v-1)//2

# 梯形數 = 平行邊對數 - 平行四邊形數
print(total_parallel_pairs - total_parallelograms)