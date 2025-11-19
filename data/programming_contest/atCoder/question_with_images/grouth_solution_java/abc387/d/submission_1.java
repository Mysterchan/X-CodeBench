import java.io.*;
import java.util.*;

public class Main {
    final int N = 1005;
    char[][] g = new char[N][N];
    int n, m;
    int[] dx = {-1, 1, 0, 0}, dy = {0, 0, -1, 1};
    void go() {
        n = nextInt();
        m = nextInt();
        int sx = -1, sy = -1, ex = -1, ey = -1;
        for (int i = 0; i < n; i++) {
            char[] s = next().toCharArray();
            for (int j = 0; j < m; j++) {
                g[i][j] = s[j];
                if (g[i][j] == 'S') {
                    sx = i;
                    sy = j;
                }
                if (g[i][j] == 'G') {
                    ex = i;
                    ey = j;
                }
            }
        }

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{sx, sy, 0, 0});
        boolean[][][] st = new boolean[n][m][3];
        while (!q.isEmpty()) {
            int[] t = q.peek(); q.poll();
            int x = t[0], y = t[1], d = t[2], s = t[3];
            if (s == 0) {
                for (int i = 0; i < 4; i++) {
                    int xx = x + dx[i], yy = y + dy[i];
                    if (xx < 0 || xx >= n || yy < 0 || yy >= m) continue;
                    if (g[xx][yy] == '#') continue;

                    int tmp = -1;
                    if (i < 2) tmp = 1;
                    else tmp = 2;
                    if (st[xx][yy][tmp]) continue;

                    if (xx == ex && yy == ey) {
                        sl(d + 1);
                        return;
                    }

                    q.add(new int[]{xx, yy, d + 1, tmp});
                    st[xx][yy][tmp] = true;
                }
            } else if (s == 1) {
                for (int i = 2; i < 4; i++) {
                    int xx = x + dx[i], yy = y + dy[i];
                    if (xx < 0 || xx >= n || yy < 0 || yy >= m) continue;
                    if (g[xx][yy] == '#') continue;

                    int tmp = 2;
                    if (st[xx][yy][tmp]) continue;

                    if (xx == ex && yy == ey) {
                        sl(d + 1);
                        return;
                    }

                    q.add(new int[]{xx, yy, d + 1, tmp});
                    st[xx][yy][tmp] = true;
                }
            } else if (s == 2) {
                for (int i = 0; i < 2; i++) {
                    int xx = x + dx[i], yy = y + dy[i];
                    if (xx < 0 || xx >= n || yy < 0 || yy >= m) continue;
                    if (g[xx][yy] == '#') continue;

                    int tmp = 1;
                    if (st[xx][yy][tmp]) continue;

                    if (xx == ex && yy == ey) {
                        sl(d + 1);
                        return;
                    }

                    q.add(new int[]{xx, yy, d + 1, tmp});
                    st[xx][yy][tmp] = true;
                }
            }
        }
        sl(-1);
    }

    boolean MULTI_CASE = false;
    boolean ALWAYS_FLUSH = false;

    InputStream inStream;
    byte[] inBuff = new byte[1024];
    int inBuffCursor = 0, inBuffLen = 0;
    boolean isVisibleChar(int c) {
        return 33 <= c && c <= 126;
    }
    boolean hasNextByte() {
        if (inBuffCursor < inBuffLen) return true;
        inBuffCursor = 0;
        try {
            inBuffLen = inStream.read(inBuff);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return inBuffLen > 0;
    }
    boolean hasNext() {
        while (hasNextByte() && !isVisibleChar(inBuff[inBuffCursor])) inBuffCursor++;
        return hasNextByte();
    }
    int nextByte() {
        return hasNextByte() ? inBuff[inBuffCursor++] : -1;
    }
    String next() {
        if (!hasNext()) throw new RuntimeException("no next.");
        StringBuilder sb = new StringBuilder();
        int b = nextByte();
        while (isVisibleChar(b)) {
            sb.appendCodePoint(b);
            b = nextByte();
        }
        return sb.toString();
    }
    long nextLong() {
        if (!hasNext()) throw new RuntimeException("no next.");
        long result = 0;
        boolean negative = false;
        int b = nextByte();
        if (b < '0') {
            if (b == '-') negative = true;
            else if (b != '+') throw new RuntimeException("long number must start with +/-.");
            b = nextByte();
        }
        while (isVisibleChar(b)) {
            if (b < '0' || b > '9') throw new RuntimeException("wrong digit in long:" + (char) b);

            result = result * 10 + (b - '0');
            b = nextByte();
        }
        return negative ? -result : result;
    }
    int nextInt() {
        long x = nextLong();
        if (x < Integer.MIN_VALUE || x > Integer.MAX_VALUE)
            throw new RuntimeException("int overflow:" + x);
        return (int) x;
    }
    double nextDouble() {
        return Double.parseDouble(next());
    }

    PrintWriter printOut = new PrintWriter(System.out);
    void so(Object obj, boolean newLine) {
        if (newLine) printOut.println(obj);
        else printOut.print(obj);
        if (ALWAYS_FLUSH) printOut.flush();
    }
    void so(Object obj) {
        so(obj, false);
    }
    void sl(Object obj) {
        so(obj, true);
    }
    void sl() {
        sl("");
    }

    void mainGo() {
        try {
            inStream = new FileInputStream("src/main.in");
            ALWAYS_FLUSH = true;
        } catch (Exception e) {
            inStream = System.in;
        }
        while (hasNext()) {
            if (MULTI_CASE) {
                int T = nextInt();
                if (T == 0) break;
                for (int i = 0; i < T; ++i) {
                    go();
                }
            } else {
                go();
            }
        }
        printOut.flush();
    }
    public static void main(String[] args) {
        new Main().mainGo();
    }
}