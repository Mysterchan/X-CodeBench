import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        long[] a = new long[n];
        long[] b = new long[n];
        long[] c = new long[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) a[i] = Long.parseLong(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) b[i] = Long.parseLong(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) c[i] = Long.parseLong(st.nextToken());

        Arrays.sort(a);
        Arrays.sort(b);
        Arrays.sort(c);

        PriorityQueue<long[]> pq = new PriorityQueue<>((x, y) -> Long.compare(y[3], x[3]));
        HashSet<Long> vis = new HashSet<>();

        long cost = a[n-1] * b[n-1] + b[n-1] * c[n-1] + c[n-1] * a[n-1];
        pq.add(new long[]{n-1, n-1, n-1, cost});
        vis.add(encode(n-1, n-1, n-1, n));

        long result = 0;
        for (int count = 0; count < k; count++) {
            long[] curr = pq.poll();
            int i = (int)curr[0];
            int j = (int)curr[1];
            int p = (int)curr[2];
            result = curr[3];

            if (i > 0) {
                long key = encode(i-1, j, p, n);
                if (vis.add(key)) {
                    long newCost = a[i-1] * b[j] + b[j] * c[p] + c[p] * a[i-1];
                    pq.add(new long[]{i-1, j, p, newCost});
                }
            }
            if (j > 0) {
                long key = encode(i, j-1, p, n);
                if (vis.add(key)) {
                    long newCost = a[i] * b[j-1] + b[j-1] * c[p] + c[p] * a[i];
                    pq.add(new long[]{i, j-1, p, newCost});
                }
            }
            if (p > 0) {
                long key = encode(i, j, p-1, n);
                if (vis.add(key)) {
                    long newCost = a[i] * b[j] + b[j] * c[p-1] + c[p-1] * a[i];
                    pq.add(new long[]{i, j, p-1, newCost});
                }
            }
        }

        System.out.println(result);
    }

    private static long encode(int i, int j, int p, int n) {
        return ((long)i * n + j) * n + p;
    }
}