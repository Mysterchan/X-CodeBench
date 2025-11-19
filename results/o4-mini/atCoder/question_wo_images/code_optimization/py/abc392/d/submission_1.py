import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    Ks = [0]*N
    dice = [None]*N
    for i in range(N):
        data = list(map(int, input().split()))
        k = data[0]
        Ks[i] = k
        faces = data[1:]
        faces.sort()
        lst = []
        prev = faces[0]
        cnt = 1
        for x in faces[1:]:
            if x == prev:
                cnt += 1
            else:
                lst.append((prev, cnt))
                prev = x
                cnt = 1
        lst.append((prev, cnt))
        dice[i] = lst

    ans = 0.0
    for i in range(N):
        lst_i = dice[i]
        ki = Ks[i]
        for j in range(i+1, N):
            lst_j = dice[j]
            kj = Ks[j]
            p = q = 0
            dot = 0
            # two‐pointer dot product of counts on equal face values
            while p < len(lst_i) and q < len(lst_j):
                vi, ci = lst_i[p]
                vj, cj = lst_j[q]
                if vi == vj:
                    dot += ci * cj
                    p += 1
                    q += 1
                elif vi < vj:
                    p += 1
                else:
                    q += 1
            prob = dot / (ki * kj)
            if prob > ans:
                ans = prob

    # print with sufficient precision
    print("%.15f" % ans)

if __name__ == "__main__":
    main()