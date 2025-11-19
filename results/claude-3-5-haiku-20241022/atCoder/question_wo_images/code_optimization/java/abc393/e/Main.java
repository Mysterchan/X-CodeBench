import java.io.*;
import java.util.*;

public class Main {
    static class MyScanner {
        static BufferedReader r;
        static StringTokenizer st;
        public MyScanner() {
            r = new BufferedReader(new InputStreamReader(System.in));
        }
        public String next() {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    st = new StringTokenizer(r.readLine());
                }
                return st.nextToken();
            } catch (Exception e) {
                return null;
            }
        }
        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
    
    public static void main(String[] args) throws IOException {
        MyScanner sc = new MyScanner();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = sc.nextInt();
        int K = sc.nextInt();
        
        int[] a = new int[N + 1];
        int maxA = 0;
        
        for (int i = 1; i <= N; i++) {
            a[i] = sc.nextInt();
            maxA = Math.max(maxA, a[i]);
        }
        
        // Count how many elements are divisible by each divisor
        int[] cnt = new int[maxA + 1];
        for (int i = 1; i <= N; i++) {
            int num = a[i];
            int sqrt = (int) Math.sqrt(num);
            for (int d = 1; d <= sqrt; d++) {
                if (num % d == 0) {
                    cnt[d]++;
                    if (d != num / d) {
                        cnt[num / d]++;
                    }
                }
            }
        }
        
        // For each element, find the maximum GCD
        for (int i = 1; i <= N; i++) {
            int num = a[i];
            int sqrt = (int) Math.sqrt(num);
            int ans = 1;
            
            // Collect all divisors
            List<Integer> divisors = new ArrayList<>();
            for (int d = 1; d <= sqrt; d++) {
                if (num % d == 0) {
                    divisors.add(d);
                    if (d != num / d) {
                        divisors.add(num / d);
                    }
                }
            }
            
            // Check divisors in descending order
            divisors.sort(Collections.reverseOrder());
            for (int d : divisors) {
                if (cnt[d] >= K) {
                    ans = d;
                    break;
                }
            }
            
            bw.write(ans + "\n");
        }
        
        bw.flush();
    }
}