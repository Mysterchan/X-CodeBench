import java.io.*;
import java.util.*;

public class Main extends PrintWriter {
    Main() { super(System.out); }
    static class Scanner {
        Scanner(InputStream in) { this.in = in; } InputStream in;
        byte[] bb = new byte[1 << 15]; int i, n;
        byte getc() {
            if (i == n) {
                i = n = 0;
                try { n = in.read(bb); } catch (IOException e) {}
            }
            return i < n ? bb[i++] : 0;
        }
        int nextInt() {
            byte c = 0; while (c <= ' ') c = getc();
            int a = 0; while (c > ' ') { a = a * 10 + c - '0'; c = getc(); }
            return a;
        }
    }
    Scanner sc = new Scanner(System.in);

    // Check vertical split: all rows have same width and can be split vertically in the middle
    boolean verticalSplit(int[] ll, int[] rr, int n) {
        int l = ll[0], r = rr[0];
        int width = r - l;
        if ((width & 1) == 1) return false; // width must be even
        int mid = (l + r) >> 1;
        for (int i = 1; i < n; i++) {
            if (rr[i] - ll[i] != width) return false;
            // Check if the split line is strictly inside the polyomino
            if (ll[i] >= mid || rr[i] <= mid) return false;
        }
        return true;
    }

    // Check horizontal split: polyomino can be split horizontally into two congruent connected parts
    boolean horizontalSplit(int[] ll, int[] rr, int n) {
        // The polyomino is convex, so the horizontal split must be at some row k where top k rows
        // and bottom n-k rows are congruent shapes.
        // We check if for some k, the top k rows and bottom k rows are congruent by comparing intervals.
        // Since the polyomino is convex, the intervals are continuous and connected.
        if ((n & 1) == 1) return false; // n must be even for horizontal split
        int half = n >> 1;
        for (int i = 0; i < half; i++) {
            if (rr[i] - ll[i] != rr[i + half] - ll[i + half]) return false;
            int shift = ll[i + half] - ll[i];
            if (shift != 0) return false; // must be exactly same columns
        }
        return true;
    }

    // Check slanted split: try all possible offsets o where 2*o <= n
    // The idea is to check if the polyomino can be split into two congruent connected parts by shifting rows by o
    boolean slantedSplit(int[] ll, int[] rr, int n) {
        for (int o = 1; o * 2 <= n; o++) {
            // Check if the shape from row 0..o-1 matches row o..2o-1 shifted horizontally
            int shift = rr[o - 1] - rr[0];
            boolean valid = true;
            for (int i = 0; i < o; i++) {
                int topL = ll[i], topR = rr[i];
                int botL = ll[i + o], botR = rr[i + o];
                if (botR - botL != topR - topL) {
                    valid = false;
                    break;
                }
                if (botL - topL != shift) {
                    valid = false;
                    break;
                }
            }
            if (!valid) continue;

            // Check connectivity and monotonicity conditions
            // The problem guarantees convexity, so we only need to check if the shape is connected after split
            // and the shifted parts do not overlap incorrectly.
            // We verify that the intervals in the bottom part are shifted by the same amount and no gaps appear.
            for (int i = o + 1; i < n; i++) {
                int topWidth = rr[i - o] - ll[i - o];
                int botWidth = rr[i] - ll[i];
                if (topWidth != botWidth) {
                    valid = false;
                    break;
                }
                int topShift = ll[i] - ll[i - o];
                if (topShift != shift) {
                    valid = false;
                    break;
                }
            }
            if (valid) return true;
        }
        return false;
    }

    void main() {
        int t = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            int n = sc.nextInt();
            int[] ll = new int[n];
            int[] rr = new int[n];
            long area = 0;
            for (int i = 0; i < n; i++) {
                ll[i] = sc.nextInt();
                rr[i] = sc.nextInt() + 1; // exclusive right bound
                area += rr[i] - ll[i];
            }
            // area guaranteed even by problem statement

            if (verticalSplit(ll, rr, n)) {
                sb.append("YES\n");
                continue;
            }
            if (horizontalSplit(ll, rr, n)) {
                sb.append("YES\n");
                continue;
            }
            if (slantedSplit(ll, rr, n)) {
                sb.append("YES\n");
                continue;
            }
            // Try slanted split on mirrored polyomino (negate coordinates)
            for (int i = 0; i < n; i++) {
                int tmp = ll[i];
                ll[i] = -rr[i];
                rr[i] = -tmp;
            }
            if (slantedSplit(ll, rr, n)) {
                sb.append("YES\n");
                continue;
            }
            sb.append("NO\n");
        }
        print(sb);
        flush();
    }

    public static void main(String[] args) {
        new Main().main();
    }
}