import java.io.*;
import java.util.*;

public class Main {
    static class Fenwick {
        int[] bit;
        int n;

        Fenwick(int n) {
            this.n = n;
            bit = new int[n + 2];
        }

        void update(int i, int v) {
            while (i <= n) {
                bit[i] += v;
                i += i & (-i);
            }
        }

        int query(int i) {
            int s = 0;
            while (i > 0) {
                s += bit[i];
                i -= i & (-i);
            }
            return s;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] chords = new int[M][2];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (a > b) {
                int tmp = a;
                a = b;
                b = tmp;
            }
            chords[i][0] = a;
            chords[i][1] = b;
        }

        // Sort chords by their left endpoint
        Arrays.sort(chords, Comparator.comparingInt(o -> o[0]));

        Fenwick fenw = new Fenwick(N);
        long intersections = 0;

        // For each chord in order of left endpoint,
        // count how many chords with right endpoint less than current chord's right endpoint have appeared
        for (int i = 0; i < M; i++) {
            int r = chords[i][1];
            // Number of chords with right endpoint < r
            int less = fenw.query(r - 1);
            // Number of chords processed so far = i
            // Intersections contributed by current chord = i - less
            intersections += i - less;
            fenw.update(r, 1);
        }

        out.println(intersections);
        out.close();
    }
}