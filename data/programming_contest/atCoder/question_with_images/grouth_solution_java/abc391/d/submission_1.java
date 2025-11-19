import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), W = Integer.parseInt(st.nextToken());
        int[] X = new int[N], Y = new int[N], p = new int[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            X[i] = Integer.parseInt(st.nextToken());
            Y[i] = Integer.parseInt(st.nextToken());
        }
        Integer[] ord = new Integer[N];
        for (int i = 0; i < N; i++) ord[i] = i;
        Arrays.sort(ord, Comparator.comparingInt(i -> Y[i]));
        int[] colCnt = new int[W + 1];
        for (int idx : ord) p[idx] = ++colCnt[X[idx]];
        long[] lineUp = new long[N + 2], deleted = new long[N + 2];
        Arrays.fill(deleted, -1);
        long del = 0;
        for (int idx : ord) {
            int pp = p[idx];
            long t = (long) Y[idx] - pp + del;
            lineUp[pp]++;
            if (lineUp[pp] == W) {
                deleted[pp] = t + 1;
                del++;
            }
        }
        long[] die = new long[N];
        for (int i = 0; i < N; i++) die[i] = deleted[p[i]];
        int Q = Integer.parseInt(br.readLine());
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            long T = Long.parseLong(st.nextToken());
            int A = Integer.parseInt(st.nextToken()) - 1;
            if (die[A] == -1 || die[A] > T) System.out.println("Yes");
            else System.out.println("No");
        }
    }
}