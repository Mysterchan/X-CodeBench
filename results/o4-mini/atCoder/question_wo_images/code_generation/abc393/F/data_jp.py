import sys
import bisect

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    # queries_by_R[i] に、R = i+1 のクエリ (インデックス, X) をためておく
    queries_by_R = [[] for _ in range(N)]
    answers = [0] * Q
    for qi in range(Q):
        R, X = map(int, input().split())
        queries_by_R[R-1].append((qi, X))

    tail = []  # tail[l] = 最小の末尾値を持つ長さ l+1 の増加部分列の末尾値
    for i in range(N):
        ai = A[i]
        # strict increasing のために bisect_left
        pos = bisect.bisect_left(tail, ai)
        if pos == len(tail):
            tail.append(ai)
        else:
            tail[pos] = ai

        # R = i+1 のクエリを処理
        for qi, X in queries_by_R[i]:
            # tail は単調増加なので bisect_right で tail[j] <= X となる最大 j+1 を得る
            answers[qi] = bisect.bisect_right(tail, X)

    print('\n'.join(map(str, answers)))

if __name__ == "__main__":
    main()