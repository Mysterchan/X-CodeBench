import java.io.*;
import java.util.*;

public class Main {
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
        private int read() throws IOException {
            if (ptr >= len) { len = in.read(buffer); ptr = 0; if (len <= 0) return -1; }
            return buffer[ptr++];
        }
        int nextInt() throws IOException {
            int c; do { c = read(); } while (c <= ' ');
            boolean neg = c == '-'; if (neg) c = read();
            int x = 0; while (c > ' ') { x = x * 10 + (c - '0'); c = read(); }
            return neg ? -x : x;
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        int N = fs.nextInt();
        int L = fs.nextInt();

        int[] pos = new int[N + 1];
        pos[1] = 0;
        for (int i = 2; i <= N; i++) {
            pos[i] = (pos[i-1] + fs.nextInt()) % L;
        }

        int count = 0;

        for (int a = 1; a <= N - 2; a++) {
            for (int b = a + 1; b <= N - 1; b++) {
                for (int c = b + 1; c <= N; c++) {

                    int d1 = (pos[b] - pos[a] + L) % L;
                    int d2 = (pos[c] - pos[b] + L) % L;
                    int d3 = (pos[a] - pos[c] + L) % L;

                    d1 = Math.min(d1, L - d1);
                    d2 = Math.min(d2, L - d2);
                    d3 = Math.min(d3, L - d3);

                    if (d1 == d2 && d2 == d3 && d1 > 0) {
                        count++;
                    }
                }
            }
        }

        System.out.println(count);
    }
}