import java.io.*;
import java.util.*;

public class Main {
    static class FenwickTree {
        long[] tree;
        int n;

        FenwickTree(int n) {
            this.n = n;
            tree = new long[n + 1];
        }

        void update(int i, long delta) {
            while (i <= n) {
                tree[i] += delta;
                i += i & (-i);
            }
        }

        long query(int i) {
            long sum = 0;
            while (i > 0) {
                sum += tree[i];
                i -= i & (-i);
            }
            return sum;
        }

        long query(int l, int r) {
            return query(r) - query(l - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] p = new int[n];
        for (int i = 0; i < n; i++) {
            p[i] = Integer.parseInt(st.nextToken());
        }

        // Fenwick tree to count how many elements have been processed at positions
        FenwickTree fenwCount = new FenwickTree(n);
        // Fenwick tree to sum positions of processed elements
        FenwickTree fenwSum = new FenwickTree(n);

        long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = p[i];
            // Number of elements already processed with value > x
            long countGreater = fenwCount.query(x + 1, n);
            // Sum of positions of elements greater than x
            long sumPosGreater = fenwSum.query(x + 1, n);

            // Cost contribution for current element:
            // For each inversion (x,y) with x > y, cost += position of smaller element (which is y)
            // Here, smaller element is x, but we accumulate cost by sum of positions of greater elements minus count * current position
            ans += sumPosGreater - countGreater * (i + 1);

            fenwCount.update(x, 1);
            fenwSum.update(x, i + 1);
        }

        out.println(ans);
        out.close();
    }
}