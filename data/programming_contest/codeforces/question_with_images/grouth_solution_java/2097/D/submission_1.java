import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    private static final class LB {
        private final Map<Integer, BigInteger> m = new HashMap<>();
        void add(BigInteger v) {
            while (!v.equals(BigInteger.ZERO)) {
                int p = v.bitLength() - 1;
                BigInteger w = m.get(p);
                if (w == null) {
                    m.put(p, v);
                    return;
                }
                v = v.xor(w);
            }
        }
        boolean has(BigInteger v) {
            while (!v.equals(BigInteger.ZERO)) {
                int p = v.bitLength() - 1;
                BigInteger w = m.get(p);
                if (w == null) return false;
                v = v.xor(w);
            }
            return true;
        }
        int size() { return m.size(); }
    }

    public static void main(String[] args) throws IOException {
        FS sc = new FS(System.in);
        StringBuilder out = new StringBuilder();
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            String s = sc.next(), u = sc.next();
            if (s.equals(u)) {
                out.append("Yes\n");
                continue;
            }
            if ((n & 1) == 1) {
                out.append("No\n");
                continue;
            }
            int g = Integer.lowestOneBit(n), m = n / g;
            LB bs = new LB();
            for (int i = 0; i < g; i++) {
                BigInteger v = new BigInteger(s.substring(i * m, (i + 1) * m), 2);
                bs.add(v);
            }
            int d = bs.size();
            boolean ok = true;
            for (int i = 0; i < g && ok; i++) {
                BigInteger v = new BigInteger(u.substring(i * m, (i + 1) * m), 2);
                if (!bs.has(v)) ok = false;
            }
            if (!ok) {
                out.append("No\n");
                continue;
            }
            LB bt = new LB();
            for (int i = 0; i < g; i++) {
                BigInteger v = new BigInteger(u.substring(i * m, (i + 1) * m), 2);
                bt.add(v);
            }
            out.append(d == bt.size() ? "Yes\n" : "No\n");
        }
        System.out.print(out);
    }

    private static final class FS {
        private final byte[] buf = new byte[1 << 16];
        private int len = 0, ptr = 0;
        private final InputStream in;
        FS(InputStream in) { this.in = in; }
        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buf);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buf[ptr++];
        }
        String next() throws IOException {
            StringBuilder sb = new StringBuilder();
            int c;
            while ((c = read()) <= ' ') if (c == -1) return "";
            do { sb.append((char) c); } while ((c = read()) > ' ');
            return sb.toString();
        }
        int nextInt() throws IOException { return Integer.parseInt(next()); }
    }
}
