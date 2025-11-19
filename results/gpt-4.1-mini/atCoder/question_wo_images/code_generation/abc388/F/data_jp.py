import sys
import bisect

def main():
    input = sys.stdin.readline
    N, M, A, B = map(int, input().split())
    bad_intervals = [tuple(map(int, input().split())) for _ in range(M)]

    # マス1からスタートし、A～Bの範囲でジャンプしながらNに到達可能か判定する。
    # 悪いマスは区間で与えられ、これらの区間は互いに重ならず昇順に並んでいる。

    # 悪いマスの区間を使って「良いマスの区間」を作る。
    # 1 < L_i ≤ R_i < N なので、1とNは悪いマス区間に含まれない。
    # 1はスタート地点であり、Nに到達できるかを判定。

    # 良い区間は、1からNまでの区間から悪い区間を除いた区間のリスト。
    good_intervals = []
    prev_end = 1
    for L, R in bad_intervals:
        if prev_end < L:
            good_intervals.append((prev_end, L - 1))
        prev_end = R + 1
    if prev_end <= N:
        good_intervals.append((prev_end, N))

    # 1は必ず良い区間に含まれているはずなので、1からスタート。
    # ただし、1は良い区間に含まれていない場合はNo。
    # 1が良い区間に含まれているか確認
    # 1は必ず良い区間のどこかに含まれているはずだが念のためチェック
    # もし含まれていなければNo
    def contains_one():
        for s, e in good_intervals:
            if s <= 1 <= e:
                return True
        return False

    if not contains_one():
        print("No")
        return

    # BFS的に区間を進めていくイメージで解く。
    # ただしNは最大10^12なので、1マスずつは無理。
    # そこで、良い区間を使って区間DP的に進める。

    # 現在到達可能な区間を管理する。
    # 初期は1のみ到達可能なので、1を含む良い区間の一部からスタート。

    # 1を含む良い区間を探し、その区間の開始点をcur_left、終了点をcur_rightとする。
    # そこからジャンプ幅A～Bで次の区間に移動可能か判定。

    # 重要: ジャンプはA～Bの範囲で、x+iに移動。
    # 現在の到達可能区間を[cur_left, cur_right]とすると、
    # 次に到達可能な区間は [cur_left + A, cur_right + B] と考えられるが、
    # その区間のうち良い区間と重なる部分のみが実際に到達可能。

    # これを繰り返し、Nに到達可能か判定。

    # good_intervalsは昇順に並んでいるので、二分探索で重なる区間を探す。

    # 初期到達区間は1を含む良い区間の一部
    # 1を含む良い区間を探す
    idx = 0
    for i, (s, e) in enumerate(good_intervals):
        if s <= 1 <= e:
            idx = i
            break
    cur_left, cur_right = 1, 1  # 現在の到達区間は1のみ

    # ただし、1が含まれる良い区間の範囲は[s, e]なので、
    # 実際にはcur_left=1, cur_right=1でスタートし、
    # そこからジャンプで広げていく。

    # 到達可能区間を管理するために、区間のリストを使う。
    # 最初は [(1,1)] からスタート。

    from collections import deque

    reachable = deque()
    reachable.append((1,1))

    # good_intervalsの区間の開始点のリストを作成（二分探索用）
    starts = [s for s, e in good_intervals]

    visited_intervals = set()  # 到達可能区間として処理済みの区間を管理（start,end）

    while reachable:
        l, r = reachable.popleft()
        if (l, r) in visited_intervals:
            continue
        visited_intervals.add((l, r))

        # この区間からジャンプ幅A～Bで移動可能な区間は [l+A, r+B]
        nl = l + A
        nr = r + B
        if nl > N:
            continue
        if nr > N:
            nr = N

        # [nl, nr] と重なる良い区間を探し、そこから新たな到達区間を作る
        # good_intervalsは昇順に並んでいるので、nlを含むかそれ以降の区間を探す
        # nlより前の区間は無視してよい

        # nlを含むか、nlより大きい区間の開始点を二分探索で探す
        pos = bisect.bisect_left(starts, nl)

        # pos-1の区間もnlを含む可能性があるので、pos-1から順に調べる
        candidates = []
        if pos > 0:
            candidates.append(pos - 1)
        # pos以降の区間もnl～nrと重なる可能性があるので、posから順に調べる
        for i in range(pos, len(good_intervals)):
            candidates.append(i)

        # 重複を避けるためsetにする
        candidates = sorted(set(candidates))

        for i in candidates:
            gs, ge = good_intervals[i]
            # [gs, ge] と [nl, nr] の重なりを求める
            left = max(gs, nl)
            right = min(ge, nr)
            if left <= right:
                # 新たな到達区間として追加
                # もしright >= Nなら到達可能
                if right >= N:
                    print("Yes")
                    return
                # すでにvisitedならスキップされるので気にしなくてよい
                reachable.append((left, right))

    print("No")

if __name__ == "__main__":
    main()