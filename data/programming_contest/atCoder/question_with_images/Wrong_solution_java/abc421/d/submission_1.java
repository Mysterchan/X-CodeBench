import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.IOException;

import javax.print.attribute.HashAttributeSet;

import java.util.*;

public class Main {

    static final int INF = Integer.MAX_VALUE;
    static final long MOD = 1000000007;

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream is) {
            br = new BufferedReader(new InputStreamReader(is));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    static long power(long x, long y, long p) {
        long res = 1;
        x = x % p;

        while (y > 0) {
            if (y % 2 == 1)
                res = (res * x) % p;
            y = y >> 1;
            x = (x * x) % p;
        }
        return res;
    }

    static boolean[] sieveOfEratosthenes(int n) {
        boolean[] prime = new boolean[n + 1];
        Arrays.fill(prime, true);
        prime[0] = prime[1] = false;
        for (int p = 2; p * p <= n; p++) {
            if (prime[p]) {
                for (int i = p * p; i <= n; i += p)
                    prime[i] = false;
            }
        }
        return prime;
    }

    static boolean cp(long va) {
        long mm = (long) Math.sqrt(va * 1.0);
        return mm * mm == va;
    }

    static long[] get(long cc[], long tt[]) {
        return new long[] { cc[0] + (tt[0] * (tt[2])), cc[1] + (tt[1] * (tt[2])) };
    }

    static char getd(long cc[]) {
        if (cc[0] == 0 && cc[1] == 1) {
            return 'R';

        } else if (cc[0] == 0 && cc[1] == -1) {
            return 'L';
        } else if (cc[0] == -1 && cc[1] == 0) {
            return 'U';
        } else {
            return 'D';
        }
    }

    public static void main(String[] args) {
        FastScanner sc = new FastScanner(System.in);
        long acx = sc.nextLong();
        long acy = sc.nextLong();
        long bcx = sc.nextLong();
        long bcy = sc.nextLong();
        long n = sc.nextLong();
        long m = sc.nextLong();
        long l = sc.nextLong();
        Deque<long[]> dq1 = new ArrayDeque<>();
        Deque<long[]> dq2 = new ArrayDeque<>();
        ArrayList<long[]> a1 = new ArrayList<>();
        ArrayList<long[]> a2 = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            char s = sc.next().charAt(0);
            int x = sc.nextInt();
            if (s == 'U') {
                dq1.add(new long[] { -1, 0, x });
            } else if (s == 'D') {
                dq1.add(new long[] { 1, 0, x });
            } else if (s == 'L') {
                dq1.add(new long[] { 0, -1, x });
            } else if (s == 'R') {
                dq1.add(new long[] { 0, 1, x });
            }
        }
        for (int i = 0; i < l; i++) {
            char s = sc.next().charAt(0);
            int x = sc.nextInt();
            if (s == 'U') {
                dq2.add(new long[] { -1, 0, x });
            } else if (s == 'D') {
                dq2.add(new long[] { 1, 0, x });
            } else if (s == 'L') {
                dq2.add(new long[] { 0, -1, x });
            } else if (s == 'R') {
                dq2.add(new long[] { 0, 1, x });
            }
        }
        while (!dq1.isEmpty()) {
            long x[] = dq1.pollFirst();
            long y[] = dq2.pollFirst();
            if (y[2] > x[2]) {
                y[2] -= x[2];
                dq2.addFirst(y);
                a1.add(new long[] { x[0], x[1], x[2] });
                a2.add(new long[] { y[0], y[1], x[2] });
            } else if (x[2] == y[2]) {
                a1.add(new long[] { x[0], x[1], x[2] });
                a2.add(new long[] { y[0], y[1], x[2] });
            } else {
                x[2] -= y[2];
                dq1.addFirst(x);
                a1.add(new long[] { x[0], x[1], y[2] });
                a2.add(new long[] { y[0], y[1], y[2] });
            }
        }

        HashMap<String, Integer> hm1 = new HashMap<>();
        long ans = 0;
        for (int i = 0; i < a1.size(); i++) {
            char dira = getd(a1.get(i));
            char dirb = getd(a2.get(i));
            long nla[] = get(new long[] { acx, acy }, a1.get(i));
            long nlb[] = get(new long[] { bcx, bcy }, a2.get(i));
            if (nla[0] == nlb[0] && nla[1] == nlb[1]) {
                hm1.put(nla[0] + " " + nla[1], 1);
            }
            if ((dira == 'U' && dirb == 'D')
                    || (dira == 'U' && dirb == 'U')
                    || (dira == 'D' && dirb == 'D')
                    || (dira == 'D' && dirb == 'U')
                    || (dira == 'L' && dirb == 'R')
                    || (dira == 'R' && dirb == 'L')
                    || (dira == 'R' && dirb == 'R')
                    || (dira == 'L' && dirb == 'L')) {
                if (dira == 'U') {
                    if (acy == bcy) {
                        long ss = Math.max(Math.min(acx, nla[0]), Math.min(bcx, nlb[0]));
                        long ee = Math.min(Math.max(acx, nla[0]), Math.max(bcx, nlb[0]));
                        if (ss <= ee) {
                            if (ee != ss) {
                                ans += (ee - ss - 1);
                            }

                        }
                    }
                } else if (dira == 'L') {
                    if (acx == bcx) {
                        long ss = Math.max(Math.min(acy, nla[1]), Math.min(bcy, nlb[1]));
                        long ee = Math.min(Math.max(acy, nla[1]), Math.max(bcy, nlb[1]));
                        if (ss <= ee) {
                            if (ee != ss) {
                                ans += (ee - ss - 1);
                            }

                        }
                    }
                }

            } else {
                long ptx = -1;
                long pty = -1;
                if (dira == 'U' || dira == 'D') {
                    ptx = nla[0];
                    pty = nlb[1];
                    if ((ptx >= Math.min(nlb[0], bcx) && ptx <= Math.max(nlb[0], bcx))
                            && (pty >= Math.min(nla[1], acy) && pty <= Math.max(nla[1], acy))) {
                        hm1.put(ptx + " " + pty, 1);
                    }
                } else if (dira == 'L' || dira == 'R') {
                    pty = nla[1];
                    ptx = nlb[0];
                    if ((ptx >= Math.min(nla[0], acx) && ptx <= Math.max(nla[0], acx))
                            && (pty >= Math.min(nlb[1], bcy) && pty <= Math.max(nlb[1], bcy))) {
                        hm1.put(ptx + " " + pty, 1);
                    }
                }

            }
            acx = nla[0];
            acy = nla[1];
            bcx = nlb[0];
            bcy = nlb[1];
            if (nla[0] == nlb[0] && nla[1] == nlb[1]) {
                hm1.put(nla[0] + " " + nla[1], 1);
            }

        }

        System.out.println(ans + hm1.size());
    }
}