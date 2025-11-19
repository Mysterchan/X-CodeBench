def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    results = []

    for _ in range(T):
        N = int(input())

        A, B, C, D, E = [], [], [], [], []
        for _ in range(N):
            ai, bi, ci, di, ei = map(int, input().split())
            A.append(ai)
            B.append(bi)
            C.append(ci)
            D.append(di)
            E.append(ei)

        div1 = [min(A[i], B[i], C[i]) for i in range(N)]
        div2 = [min(B[i], C[i], D[i]) for i in range(N)]
        div3 = [min(C[i], D[i], E[i]) for i in range(N)]

        ans = []
        s1 = s2 = s3 = 0
        for i in range(N):
            s1 += div1[i]
            s2 += div2[i]
            s3 += div3[i]
            ans.append(str(min(s1, s2, s3)))

        results.append(' '.join(ans))

    print('\n'.join(results))

if __name__ == '__main__':
    main()