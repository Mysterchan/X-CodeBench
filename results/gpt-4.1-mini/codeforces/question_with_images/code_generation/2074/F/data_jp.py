import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        l1, r1, l2, r2 = map(int, input().split())
        width = r1 - l1
        height = r2 - l2

        # クワッドツリーのノードは、サイズが2^kの正方形領域で表される。
        # 与えられた矩形領域を最小のノード数でカバーするには、
        # それぞれの軸方向に対して、区間長を2のべき乗の区間に分割したときの最小個数を求め、
        # それらの積をとる。

        # 区間長を2のべき乗の区間に分割する最小個数を求める関数
        def min_cover_length(length):
            count = 0
            while length > 0:
                # length以下の最大の2のべき乗を求める
                p = 1 << (length.bit_length() - 1)
                length -= p
                count += 1
            return count

        ans = min_cover_length(width) * min_cover_length(height)
        print(ans)

if __name__ == "__main__":
    solve()