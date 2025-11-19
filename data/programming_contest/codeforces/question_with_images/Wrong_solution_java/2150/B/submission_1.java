import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    static Scanner input = new Scanner(System.in);
    static final long MOD = 998244353;
    static final int N = 2 * 100000 + 1;
    static final long[] fac = new long[N];
    public static void main(String[] args) throws IOException {
        int t = input.nextInt();
        fac[0] = 1;
        for(int i = 1; i < N; ++i) {
            fac[i] = ((long)i*fac[i-1]) % MOD;
        }
        while(t --> 0) {
            int n = input.nextInt();
            int[] a = new int[n];
            for(int i = 0; i < n; ++i) a[i] = input.nextInt();
            int half = n/2+n%2;
            boolean can = true;
            for(int i = half; i < n; ++i) {
                if(a[i] > 0) {
                    can = false;
                    break;
                }
            }
            long sum = 0;
            for(int i = 0; i < half; ++i) {
                sum += (long)a[i];
            }
            if(sum != (long)n) can = false;
            if(!can) {
                System.out.println(0);
                continue;
            }
            long answer = 1;
            int used = 0;
            if(n%2 == 1) {
                if(a[half-1] > 1) {
                    System.out.println(0);
                    continue;
                }
                used = a[half-1] == 1 ? 1 : 0;
                --half;
            }
            for(int i = half-1; i > -1; --i) {
                int active = n-2*i - used;
                int inrow = a[i];
                if(inrow > active) {
                    answer = 0;
                    break;
                }
                answer = (answer * calc(inrow, active)) % MOD;
                used += inrow;
            }
            if(used != n) answer = 0;
            System.out.println(answer);
        }
    }
    static long calc(int s, int n) {
        if(s == n) {
            return 1;
        }
        return (fac[n] * inverse(fac[n-s] * fac[s]))%MOD;
    }
   static long inverse(long a) {
        return power(a, MOD-2, (int)MOD);
    }
    static long power(long a, long b, int MOD) {
        long result = 1;
        while(b > 0) {
            if(b%2 == 1) result = (result*a)%MOD;
            a = (a*a)%MOD;
            b /= 2;
        }
        return result;
    }
    static class Scanner {
        BufferedReader reader;
        StringTokenizer string;
        public Scanner(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
        }
        public String next() throws IOException {
            while(string == null || ! string.hasMoreElements()) {
                string = new StringTokenizer(reader.readLine());
            }
            return string.nextToken();
        }
        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }
    }
}
