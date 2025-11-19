import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Main {
    static long[] extGCD(long a, long b) {
        if (b == 0) {
            return new long[]{a, 1, 0};
        } else {
            long[] r = extGCD(b, a % b);
            long g = r[0], x = r[1], y = r[2];
            return new long[]{g, y, x - (a / b) * y};
        }
    }

    static long modInv(long a, long m) {
        long[] r = extGCD(a, m);
        long inv = r[1] % m;
        if (inv < 0) inv += m;
        return inv;
    }

    static long[] solveLinear(long v, long r, long n) {
        long g = gcd(v, n);
        if ((r % g) != 0) {
            return null;
        }
        long v0 = v / g;
        long n0 = n / g;
        long r0 = (r / g) % n0;
        if (r0 < 0) r0 += n0;
        long inv = modInv(v0, n0);
        long a0 = (inv * r0) % n0;
        return new long[]{a0, n0};
    }

    static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    static long[] crt(long a1, long m1, long a2, long m2) {
        long g = gcd(m1, m2);
        long diff = a2 - a1;
        if (diff % g != 0) {
            return null;
        }
        long m1p = m1 / g, m2p = m2 / g;
        long rhs = (diff / g) % m2p;
        if (rhs < 0) rhs += m2p;
        long inv = modInv(m1p, m2p);
        long t = (inv * rhs) % m2p;
        long M = m1 * m2p;
        long x0 = a1 + m1 * t;
        x0 %= M;
        if (x0 < 0) x0 += M;
        return new long[]{x0, M};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        for (int _case = 0; _case < T; _case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long n = Long.parseLong(st.nextToken());
            long x = Long.parseLong(st.nextToken());
            long y = Long.parseLong(st.nextToken());
            long vx = Long.parseLong(st.nextToken());
            long vy = Long.parseLong(st.nextToken());

            long g0 = gcd(vx, vy);
            vx /= g0;
            vy /= g0;
            long rx = (n - x) % n;  if (rx < 0) rx += n;
            long ry = (n - y) % n;  if (ry < 0) ry += n;

            long[] sol1 = solveLinear(vx, rx, n);
            if (sol1 == null) {
                out.println(-1);
                continue;
            }
            long a1 = sol1[0], m1 = sol1[1];

            long[] sol2 = solveLinear(vy, ry, n);
            if (sol2 == null) {
                out.println(-1);
                continue;
            }
            long a2 = sol2[0], m2 = sol2[1];
            long[] sol = crt(a1, m1, a2, m2);
            if (sol == null) {
                out.println(-1);
                continue;
            }
            long t0 = sol[0];
            long M  = sol[1];
            if (t0 == 0) t0 += M;
            BigInteger Bn = BigInteger.valueOf(n);
            BigInteger Bx = BigInteger.valueOf(x);
            BigInteger By = BigInteger.valueOf(y);
            BigInteger Bvx = BigInteger.valueOf(vx);
            BigInteger Bvy = BigInteger.valueOf(vy);
            BigInteger Bt  = BigInteger.valueOf(t0);

            BigInteger PX = Bx.add(Bvx.multiply(Bt)).divide(Bn);
            BigInteger PY = By.add(Bvy.multiply(Bt)).divide(Bn);

            long p = PX.longValue();
            long q = PY.longValue();
            long s = p + q;

            long ans = (p - 1) + (q - 1) + (s / 2);
            out.println(ans);
        }
        out.flush();
    }
}
