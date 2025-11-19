import java.io.*;
import java.util.*;

public class Main {
    static final int N = 200005;
    static long[] a = new long[N];
    static long[] pre1 = new long[N];
    static long[] pre2 = new long[N];
    static long[] pre = new long[N];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            a[i] = Long.parseLong(st.nextToken());
            pre[i] = pre[i - 1] + a[i];
            if (i % 2 == 1) {
                pre1[i] = pre1[i - 1] + a[i];
                pre2[i] = pre2[i - 1];
            } else {
                pre2[i] = pre2[i - 1] + a[i];
                pre1[i] = pre1[i - 1];
            }
        }

        while (q-- > 0) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());

            long sum = pre[r] - pre[l - 1];
            long sum1 = pre1[r] - pre1[l - 1];
            long sum2 = pre2[r] - pre2[l - 1];

            if ((r - l + 1) % 2 == 1) {
                sum1 += a[l];
                l++;
            }

            long ans = Math.min(sum1, sum2) + (sum - Math.min(sum1, sum2) * 2) / 3;
            System.out.println(ans);
        }
    }
}