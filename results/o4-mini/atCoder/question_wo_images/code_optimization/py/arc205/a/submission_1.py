import sys
import threading

def main():
    import sys

    input = sys.stdin.readline
    n, q = map(int, input().split())
    grid = [input().rstrip() for _ in range(n)]

    # Build s_score: (n-1) x (n-1), 1 if 2x2 block of white dots
    m = n - 1
    s_score = [[0]*m for _ in range(m)]
    for i in range(m):
        row_i = grid[i]
        row_i1 = grid[i+1]
        for j in range(m):
            if row_i[j]=='.' and row_i[j+1]=='.' and row_i1[j]=='.' and row_i1[j+1]=='.':
                s_score[i][j] = 1

    # Build 2D prefix sum over s_score
    ps = [[0]*(m+1) for _ in range(m+1)]
    for i in range(m):
        acc = 0
        for j in range(m):
            acc += s_score[i][j]
            ps[i+1][j+1] = ps[i][j+1] + acc

    out = []
    for _ in range(q):
        u, d, l, r = map(int, input().split())
        # Convert to 0-based indices in s_score
        # rows u-1 ... d-2, cols l-1 ... r-2
        tl_r = u-1
        br_r = d-2
        tl_c = l-1
        br_c = r-2
        if tl_r>br_r or tl_c>br_c:
            out.append('0')
        else:
            # sum over [tl_r..br_r] x [tl_c..br_c]
            # using ps: ps[x2+1][y2+1] - ps[x1][y2+1] - ps[x2+1][y1] + ps[x1][y1]
            res = ps[br_r+1][br_c+1] - ps[tl_r][br_c+1] - ps[br_r+1][tl_c] + ps[tl_r][tl_c]
            out.append(str(res))

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    threading.Thread(target=main).start()