import java.io.*;
import java.util.*;

public class Main {
    static FastReader in = new FastReader();
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int n = in.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = in.nextInt();

        // dp[i][j] = map from sequence (as list of indices) to sum
        Map<List<Integer>, Long>[] dp = new HashMap[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = new HashMap<>();
        
        dp[0].put(new ArrayList<>(), 0L);

        for (int i = 0; i < n; i++) {
            for (Map.Entry<List<Integer>, Long> entry : dp[i].entrySet()) {
                List<Integer> seq = entry.getKey();
                long sum = entry.getValue();
                
                // Append
                List<Integer> newSeq = new ArrayList<>(seq);
                newSeq.add(i);
                long newSum = sum + arr[i];
                dp[i + 1].merge(newSeq, newSum, Math::max);
                
                // Delete (if possible)
                if (!seq.isEmpty()) {
                    List<Integer> delSeq = new ArrayList<>(seq);
                    delSeq.remove(delSeq.size() - 1);
                    dp[i + 1].merge(delSeq, sum, Math::max);
                }
            }
        }

        long ans = Long.MIN_VALUE;
        for (long val : dp[n].values()) {
            ans = Math.max(ans, val);
        }
        out.println(ans);
        out.flush();
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