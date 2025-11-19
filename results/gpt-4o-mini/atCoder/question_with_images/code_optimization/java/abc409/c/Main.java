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

        int[] pos = new int[N];
        pos[0] = 0;
        for (int i = 1; i < N; i++) {
            pos[i] = (pos[i - 1] + fs.nextInt()) % L;
        }

        Map<Integer, Integer> countMap = new HashMap<>();
        for (int i = 0; i < N; i++) {
            countMap.put(pos[i], countMap.getOrDefault(pos[i], 0) + 1);
        }

        long count = 0;
        for (int i = 0; i < N; i++) {
            int a_pos = pos[i];

            for (int j = 1; j <= L / 3; j++) {
                int b_pos = (a_pos + j) % L;
                int c_pos = (a_pos + 2 * j) % L;
                
                int aCount = countMap.getOrDefault(a_pos, 0);
                int bCount = countMap.getOrDefault(b_pos, 0);
                int cCount = countMap.getOrDefault(c_pos, 0);

                if (b_pos == a_pos) {
                    bCount--;
                }
                if (c_pos == a_pos) {
                    cCount--;
                }
                if (b_pos == c_pos) {
                    cCount--;
                }

                if (bCount > 0 && cCount > 0) {
                    count += aCount * bCount * cCount;
                }
            }
        }

        System.out.println(count / 6);
    }
}