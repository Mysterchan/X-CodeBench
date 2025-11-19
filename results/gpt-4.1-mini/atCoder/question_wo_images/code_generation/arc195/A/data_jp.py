import sys
import bisect

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 各値の出現位置リストを作成
    pos = {}
    for i, a in enumerate(A):
        pos.setdefault(a, []).append(i)

    # Bの各要素がAに存在しなければ即No
    for b in B:
        if b not in pos:
            print("No")
            return

    # 1回目のマッチング（前から）
    prev = -1
    left_pos = []
    for b in B:
        idx_list = pos[b]
        # prevより大きい位置を探す
        i = bisect.bisect_right(idx_list, prev)
        if i == len(idx_list):
            print("No")
            return
        p = idx_list[i]
        left_pos.append(p)
        prev = p

    # 2回目のマッチング（後ろから）
    prev = N
    right_pos = [0]*M
    for i in range(M-1, -1, -1):
        b = B[i]
        idx_list = pos[b]
        # prevより小さい位置を探す
        j = bisect.bisect_left(idx_list, prev) - 1
        if j < 0:
            print("No")
            return
        p = idx_list[j]
        right_pos[i] = p
        prev = p

    # left_pos と right_pos の比較で2つ以上あるか判定
    # 2つ以上あるとは、異なる位置の部分列が2つ以上あること
    # 1つ目の部分列は left_pos
    # 2つ目の部分列は right_pos
    # もし left_pos != right_pos なら Yes
    # もし同じなら、部分列は1つだけなので No

    if left_pos != right_pos:
        print("Yes")
    else:
        # さらに、同じ部分列でも、同じ位置の選択が複数あるかを考える必要はない
        # なぜなら、部分列の位置は一意に決まるため
        print("No")

if __name__ == "__main__":
    main()