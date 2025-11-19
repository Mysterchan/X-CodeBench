import sys
import math
input = sys.stdin.readline
MOD = 998244353

t = int(input())
for _ in range(t):
    n, m, d = map(int, input().split())
    grid = [input().rstrip('\n') for __ in range(n)]

    # 各 row のホールドの位置（列インデックス）を取得
    holds = []
    for i in range(n):
        row_holds = [j for j, c in enumerate(grid[i]) if c == 'X']
        if not row_holds:
            # どこかの行にホールドがなければルートは0
            holds = None
            break
        holds.append(row_holds)
    if holds is None:
        print(0)
        continue

    # dp[i][mask] := i行目(0-based, 上から)で選んだホールドの組み合わせmaskに対するルート数
    # maskは0~3まで（2ビット）で、0b01は左のホールド、0b10は右のホールド、0b11は両方選択
    # ただし、各行のホールド数は最大2つまで選べるので、maskは0以外の1~3の範囲
    # しかし、行によってホールド数は異なるので、maskの意味は行ごとに異なる
    # そこで、各行のホールドを最大2つまで選べる組み合わせを列挙し、それをmaskとして扱う

    # まず各行のホールド数は任意だが、選べるのは1個か2個まで
    # そのため、各行のホールドの組み合わせを列挙する
    # 1個選択 or 2個選択の組み合わせを列挙し、それを状態として扱う

    # holds[i] は i行目のホールドの列番号リスト
    # 各行の状態は holds[i] の中から1個または2個選ぶ組み合わせ
    # これを states[i] に格納し、indexで管理する

    states = []
    for row in holds:
        row_states = []
        length = len(row)
        # 1個選択
        for i1 in range(length):
            row_states.append((row[i1],))
        # 2個選択
        if length >= 2:
            for i1 in range(length):
                for i2 in range(i1+1, length):
                    row_states.append((row[i1], row[i2]))
        states.append(row_states)

    # dp[i][k]: i行目の状態k(状態kはstates[i][k])のルート数
    # 初期化
    dp = [dict() for _ in range(n)]
    # 最下行(n-1)の状態はすべて1通りのルートの始まり
    for k in range(len(states[n-1])):
        dp[n-1][k] = 1

    # i行目からi-1行目へ遷移
    # 条件:
    # - 各次のホールドは前のホールドよりも低くない（行番号は上から0なのでi-1 < iなのでi-1行は上の行）
    #   → i-1 < i なので i-1行のホールドは上の行、i行のホールドは下の行
    #   → 「次のホールドは前のホールドより低くない」は「i-1行のホールドの行番号 <= i行のホールドの行番号」
    #   → これは常に i-1 < i なので i-1行のホールドは上の行、i行のホールドは下の行なので条件は満たされない？
    #   問題文の「各次のホールドは前のホールドより低くない」は「行番号が小さい方が上のレベル」なので
    #   ルートは下から上に登るので、i行目からi-1行目に遷移する際、i-1 < iなので i-1行目のホールドは上の行
    #   「次のホールドは前のホールドより低くない」→ i-1 <= i なので i-1行目のホールドはi行目のホールドより上なので条件は満たす
    #   つまり、i-1行目のホールドの行番号 <= i行目のホールドの行番号は常に成立するのでこの条件は無視してよい

    # - 各レベルで1個か2個のホールドを使う（statesで管理済み）
    # - 移動可能かどうかは、i行目のホールドからi-1行目のホールドへの距離がd以下であること
    #   i行目のホールドは下の行、i-1行目のホールドは上の行
    #   距離は sqrt((i1 - i2)^2 + (j1 - j2)^2)
    #   i1, i2 は行番号、j1, j2 は列番号
    #   i1 = i, i2 = i-1
    #   つまり距離 = sqrt(1^2 + (j1 - j2)^2) <= d
    #   → (j1 - j2)^2 <= d^2 - 1

    max_dist_sq = d*d - 1
    if max_dist_sq < 0:
        # d=0のときは移動できない（距離は最低1）
        # つまりルートは存在しない
        print(0)
        continue

    # i行目の状態kからi-1行目の状態lへ遷移可能か判定
    # i行目のホールド位置: states[i][k]
    # i-1行目のホールド位置: states[i-1][l]
    # すべての組み合わせで距離判定し、すべてのペアが距離<=dなら遷移可能
    # しかし、問題文の「現在のホールドから次のホールドに移動できるのは、対応するセグメントの中心間の距離がdを超えない場合」
    # これは「各次のホールド」なので、i行目の各ホールドからi-1行目の各ホールドへの移動が可能である必要はない
    # ルートはホールドの列挙なので、i行目のホールドからi-1行目のホールドへの遷移は
    # 「i行目のホールドのいずれかからi-1行目のホールドのいずれかへ移動可能」であればよいのか？
    # いいえ、ルートはホールドの連続なので、i行目のホールドのそれぞれからi-1行目のホールドのそれぞれへ移動可能でなければならない
    # しかし、イーゴルは2つの手で2つまでホールドを持つので、i行目の2つのホールドからi-1行目の2つのホールドへ
    # それぞれ対応するホールド間の距離がd以下でなければならない
    # つまり、i行目のホールドのそれぞれからi-1行目のホールドのそれぞれへ移動可能である必要がある
    # つまり、i行目のホールドの各ホールドからi-1行目のホールドの各ホールドへの距離がd以下でなければならない

    # まとめると、i行目の状態kのホールド集合とi-1行目の状態lのホールド集合の全組み合わせの距離がd以下であること

    # dpを計算
    for i in range(n-1, 0, -1):
        dp_prev = dict()
        st_cur = states[i]
        st_up = states[i-1]
        for k, pos_cur in enumerate(st_cur):
            ways = dp[i].get(k, 0)
            if ways == 0:
                continue
            for l, pos_up in enumerate(st_up):
                # 全組み合わせの距離判定
                ok = True
                for c_j in pos_cur:
                    for u_j in pos_up:
                        dist_sq = 1 + (c_j - u_j) * (c_j - u_j)
                        if dist_sq > d*d:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    dp_prev[l] = (dp_prev.get(l, 0) + ways) % MOD
        dp[i-1] = dp_prev

    # 最上行(0行目)のdpの合計が答え
    ans = 0
    for v in dp[0].values():
        ans = (ans + v) % MOD
    print(ans)