import java.io.*;
import java.util.*;

public class Main {
    static class G {
        long g, u, v;
        G(long g, long u, long v) {
            this.g = g;
            this.u = u;
            this.v = v;
        }
    }

    static G egcd(long a, long b) {
        if (b == 0) return new G(a, 1, 0);
        G t = egcd(b, a % b);
        return new G(t.g, t.v, t.u - (a / b) * t.v);
    }

    static long gcd(long a, long b) {
        return b == 0 ? Math.abs(a) : gcd(b, a % b);
    }

    static long cd(long a, long b) {
        return a >= 0 ? (a + b - 1) / b : a / b;
    }

    static long hits(long i, long j) {
        if (i == 1 || j == 1) {
            long L = Math.max(i, j);
            return 2 * L - (L % 2 == 0 ? 2 : 1);
        }
        return (i - 1) + (j - 1) + (i + j) / 2 + Math.abs(i - j) / 2;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long n = Long.parseLong(st.nextToken());
            long x = Long.parseLong(st.nextToken());
            long y = Long.parseLong(st.nextToken());
            long vx = Long.parseLong(st.nextToken());
            long vy = Long.parseLong(st.nextToken());

            long m = vx * y - vy * x;
            if (m % n != 0) {
                out.println(-1);
                continue;
            }

            long k0 = m / n;
            long g0 = gcd(vx, vy);
            if (k0 % g0 != 0) {
                out.println(-1);
                continue;
            }

            long a1 = vx / g0, b1 = vy / g0, k1 = k0 / g0;
            G res = egcd(a1, b1);
            long j0 = res.u * k1;
            long i0 = -res.v * k1;
            long t1 = cd(1 - i0, a1);
            long t2 = cd(1 - j0, b1);
            long t = Math.max(t1, t2);

            long i = i0 + a1 * t;
            long j = j0 + b1 * t;

            if (i < 1 || j < 1) {
                out.println(-1);
            } else {
                out.println(hits(i, j));
            }
        }
        out.flush();
    }
}
