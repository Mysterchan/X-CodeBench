import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader fr = new FastReader();
        int T = fr.nextInt();
        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            int N = fr.nextInt();
            int M = fr.nextInt();
            int[] A = new int[N];
            int[] B = new int[N];

            for (int i = 0; i < N; i++) A[i] = fr.nextInt();
            for (int i = 0; i < N; i++) B[i] = fr.nextInt();

            Arrays.sort(A);
            Arrays.sort(B);

            int left = 0, right = M - 1, ans = M - 1;

            while (left <= right) {
                int mid = (left + right) / 2;
                if (isPossible(A, B, M, mid)) {
                    ans = mid;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            sb.append(ans).append("\n");
        }

        System.out.print(sb);
    }

    static boolean isPossible(int[] A, int[] B, int M, int maxMod) {
        TreeMap<Integer, Integer> multiset = new TreeMap<>();
        for (int val : A) {
            multiset.put(val, multiset.getOrDefault(val, 0) + 1);
        }

        for (int i = B.length - 1; i >= 0; i--) {
            int b = B[i];
            int limit1 = maxMod - b;
            int limit2 = M - b;

            Integer x = multiset.floorKey(limit1);
            if (x == null) {
                x = multiset.ceilingKey(limit2);
                if (x == null) return false;
            }

            if (multiset.get(x) == 1) {
                multiset.remove(x);
            } else {
                multiset.put(x, multiset.get(x) - 1);
            }
        }

        return true;
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try { st = new StringTokenizer(br.readLine()); }
                catch (IOException e) { e.printStackTrace(); }
            }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }
    }
}