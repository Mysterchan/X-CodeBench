import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static PrintWriter out;
    static StringTokenizer st;
    static List<Long> divisors;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);

        int Q = readInt();
        divisors = new ArrayList<>();

        for (int i = 0; i < Q; i++) {
            long a = readLong();
            int b = readInt();
            
            addDivisor(a);
            
            long result = findKth(b);
            out.println(result);
        }

        out.close();
    }

    static void addDivisor(long a) {
        List<Long> newDivisors = new ArrayList<>();
        
        for (long d : divisors) {
            long g = gcd(a, d);
            if (g == d) {
                return;
            }
            if (g == a) {
                a = -1;
                break;
            }
        }
        
        if (a != -1) {
            for (long d : divisors) {
                long lcm = lcm(a, d);
                if (lcm <= 2000000000L) {
                    newDivisors.add(lcm);
                }
            }
            divisors.add(a);
            divisors.addAll(newDivisors);
        }
    }

    static long findKth(int k) {
        long left = 1, right = 200000;
        
        while (left < right) {
            long mid = (left + right) / 2;
            if (countValid(mid) < k) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return left;
    }

    static long countValid(long n) {
        long total = n;
        int size = divisors.size();
        
        for (int mask = 1; mask < (1 << size); mask++) {
            long lcm = 1;
            int bits = 0;
            
            for (int i = 0; i < size; i++) {
                if ((mask & (1 << i)) != 0) {
                    lcm = lcm(lcm, divisors.get(i));
                    if (lcm > n) break;
                    bits++;
                }
            }
            
            if (lcm <= n) {
                if (bits % 2 == 1) {
                    total -= n / lcm;
                } else {
                    total += n / lcm;
                }
            }
        }
        
        return total;
    }

    static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    static long lcm(long a, long b) {
        long g = gcd(a, b);
        if (a / g > 2000000000L / b) return 2000000001L;
        return a / g * b;
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine());
        return st.nextToken();
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }

    static long readLong() throws IOException {
        return Long.parseLong(next());
    }
}