import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline
    MOD = 998244353

    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    Q, sh, sw = map(int, input().split())
    sh -= 1; sw -= 1

    # Precompute dp_enter: number of ways' products to enter (i,j) excluding A[i][j]
    dp_enter = [[0] * W for _ in range(H)]
    dp_enter[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            v = 0
            if i > 0:
                # from above: multiply by A[i-1][j]
                v = (v + dp_enter[i-1][j] * A[i-1][j]) % MOD
            if j > 0:
                # from left: multiply by A[i][j-1]
                v = (v + dp_enter[i][j-1] * A[i][j-1]) % MOD
            dp_enter[i][j] = v

    # Precompute dp_exit: number of ways' products from (i,j) to sink excluding A[i][j]
    dp_exit = [[0] * W for _ in range(H)]
    dp_exit[H-1][W-1] = 1
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if i == H-1 and j == W-1:
                continue
            v = 0
            if i+1 < H:
                v = (v + dp_exit[i+1][j] * A[i+1][j]) % MOD
            if j+1 < W:
                v = (v + dp_exit[i][j+1] * A[i][j+1]) % MOD
            dp_exit[i][j] = v

    # Precompute weight[i][j] = dp_enter[i][j] * dp_exit[i][j]
    weight = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            weight[i][j] = dp_enter[i][j] * dp_exit[i][j] % MOD

    # Initial answer: sum over all cells of A[i][j] * weight[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = (ans + A[i][j] * weight[i][j]) % MOD

    x, y = sh, sw
    out = []
    for _ in range(Q):
        d, p = input().split()
        p = int(p)
        # move
        if d == 'L':
            y -= 1
        elif d == 'R':
            y += 1
        elif d == 'U':
            x -= 1
        else:  # 'D'
            x += 1
        # update
        delta = (p - A[x][y]) % MOD
        if delta:
            ans = (ans + delta * weight[x][y]) % MOD
            A[x][y] = p
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    threading.Thread(target=main).start()