import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, X, Y = map(int, input().split())
S = input().rstrip()
T = input().rstrip()

# 操作A,Bは長さX+Yの区間内で
# 0...0 (X個) + 1...1 (Y個) を
# 1...1 (Y個) + 0...0 (X個) に入れ替える操作（またはその逆）
# つまり、長さX+Yの区間内で「0の塊と1の塊」を入れ替える操作

# 重要なことは、操作はX+Yの区間内で0と1の塊を入れ替えることができるということ。
# これを繰り返すことで、Sの中の0と1の塊の並びを入れ替えられる。

# したがって、SとTの0と1の塊の長さの並びが同じであればYes、
# そうでなければNo。

# ただし、塊の長さはXとYの単位で入れ替えられるので、
# 0の塊の長さはXの倍数、1の塊の長さはYの倍数でなければならない。

# まず、SとTの0と1の塊の長さをX,Yで割った個数の列に変換し、
# それが一致するかを判定する。

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

S_rle = run_length_encode(S)
T_rle = run_length_encode(T)

# 0と1の塊の数が違えばNo
if len(S_rle) != len(T_rle):
    print("No")
    exit()

# 各塊の文字が一致しなければNo
for (sc, sl), (tc, tl) in zip(S_rle, T_rle):
    if sc != tc:
        print("No")
        exit()

# 各塊の長さがXまたはYの倍数でなければNo
# さらに、Sの塊の長さとTの塊の長さは同じでなければならない
# なぜなら操作は塊の入れ替えのみで、塊の長さは変わらないから

for (c, sl), (_, tl) in zip(S_rle, T_rle):
    if sl != tl:
        print("No")
        exit()
    if c == '0':
        if sl % X != 0:
            print("No")
            exit()
    else:
        if sl % Y != 0:
            print("No")
            exit()

print("Yes")