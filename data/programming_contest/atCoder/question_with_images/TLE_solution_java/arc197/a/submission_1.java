import java.util.*;

class Main {
    static Set<Long> s;

    static void a(String[] x) {
        Scanner n = new Scanner(System.in);
        int t = n.nextInt();
        int i = 0;
        while (i < t) {
            b(n);
            i++;
        }
        n.close();
    }

    static void b(Scanner n) {
        int h = n.nextInt();
        int w = n.nextInt();
        String z = n.next();
        s = new HashSet<>();
        int[] p = c(z.toCharArray());
        int d = p[0], r = p[1], q = p[2];
        int u = h - 1 - d;
        int v = w - 1 - r;
        if (u < 0 || v < 0 || u + v > q) {
            d(z.toCharArray());
        } else {
            e(z.toCharArray(), h - 1, w - 1);
        }
        System.out.println(s.size());
    }

    static int[] c(char[] z) {
        int d = 0, r = 0, q = 0;
        int i = 0;
        while (i < z.length) {
            if (z[i] == 'D') d++;
            else if (z[i] == 'R') r++;
            else q++;
            i++;
        }
        return new int[]{d, r, q};
    }

    static void d(char[] z) {
        int h = 1, w = 1;
        s.add(((long)h << 20) + w);
        int i = 0;
        while (i < z.length) {
            if (z[i] == 'D') h++;
            else if (z[i] == 'R') w++;
            s.add(((long)h << 20) + w);
            i++;
        }
    }

    static void e(char[] z, int d, int r) {
        char[] p = new char[z.length];
        f(z, 0, 1, 1, 0, 0, d, r, p);
    }

    static void f(char[] z, int i, int h, int w, int d, int r, int x, int y, char[] p) {
        if (i == z.length) {
            if (d == x && r == y) {
                g(p);
            }
            return;
        }
        if (z[i] == 'D' || z[i] == '?') {
            if (d < x && h < x + 1) {
                p[i] = 'D';
                f(z, i + 1, h + 1, w, d + 1, r, x, y, p);
            }
        }
        if (z[i] == 'R' || z[i] == '?') {
            if (r < y && w < y + 1) {
                p[i] = 'R';
                f(z, i + 1, h, w + 1, d, r + 1, x, y, p);
            }
        }
    }

    static void g(char[] p) {
        int h = 1, w = 1;
        s.add(((long)h << 20) + w);
        int i = 0;
        while (i < p.length) {
            if (p[i] == 'D') h++;
            else w++;
            s.add(((long)h << 20) + w);
            i++;
        }
    }

    public static void main(String[] args) {
        a(args);
    }
}