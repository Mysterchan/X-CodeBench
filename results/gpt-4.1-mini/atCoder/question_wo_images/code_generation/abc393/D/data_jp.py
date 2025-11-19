def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = input().rstrip()

    ones_pos = [i for i, c in enumerate(S) if c == '1']
    k = len(ones_pos)

    # すべての1を連続させる区間の長さは k
    # 1を連続させる区間の開始位置を決めると、
    # その区間に1を詰めるための操作回数は、
    # 各1の現在位置と目標位置の差の絶対値の和の最小化問題になる。

    # 目標区間の開始位置を x とすると、
    # 目標位置は x, x+1, ..., x+k-1
    # 操作回数は sum(|ones_pos[i] - (x + i)|) となる。

    # この値を最小化する x を求める。
    # x は整数で 0 <= x <= N-k

    # ここで、xを変数として考えると、
    # sum(|ones_pos[i] - (x + i)|) = sum(|(ones_pos[i] - i) - x|)
    # となる。

    # つまり、配列 A = [ones_pos[i] - i for i in range(k)] に対して、
    # sum(|A[i] - x|) を最小化する x を求める問題になる。

    # sum(|A[i] - x|) は x を A の中央値にすると最小になる。

    A = [ones_pos[i] - i for i in range(k)]
    A.sort()
    median = A[k // 2]

    ans = sum(abs(a - median) for a in A)
    print(ans)

if __name__ == "__main__":
    main()