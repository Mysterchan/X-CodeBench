import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        int T = sc.nextInt();
        while (T-- > 0) {
            solve();
        }
        out.close();
    }

    static void solve() {
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        int pt = 0;
        int len = 2 * n + 5;
        int[] l = new int[len], r = new int[len];
        int prev = a[0];
        int ll = 0;
        PriorityQueue<int[]> p = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]);
        int[] v = new int[len];
        int[] L = new int[len];
        for (int i = 0; i < n; i++) {
            if (a[i] != prev) {
                p.offer(new int[]{prev, i - ll, pt});
                v[pt] = prev;
                L[pt] = i - ll;
                ll = i;
                pt++;
                prev = a[i];
            }
        }
        p.offer(new int[]{prev, n - ll, pt});
        v[pt] = prev;
        L[pt] = n - ll;

        pt++;

        for (int i = 0; i < pt; i++) {
            if (i > 0) l[i] = i - 1;
            if (i < pt - 1) r[i] = i + 1;
        }
        l[0] = -1;
        r[pt - 1] = -1;
        boolean[] inP = new boolean[len];
        for (int i = 0; i < pt; i++) {
            inP[i] = true;
        }
        int op = 0;
        long ans = 0;
        int xx = pt;
        while (op < xx) {
            int[] z = p.poll();
            assert z != null;
            int val = z[0], lens = z[1], id = z[2];

            if (!inP[id]) continue;
            inP[id] = false;
            op++;
            if (op == xx) {
                while (lens > 1) {
                    if (lens % 2 == 1) {
                        ans++;
                        lens = (lens + 1) / 2;
                    } else {
                        lens /= 2;
                    }
                }
                break;
            }

            boolean left = true;
            int idx = -1, min = Integer.MAX_VALUE;
            if (l[id] != -1) {
                if (v[l[id]] < min) {
                    min = v[l[id]];
                    idx = l[id];
                }
            }
            if (r[id] != -1) {
                if (v[r[id]] < min) {
                    min = v[r[id]];
                    idx = r[id];
                    left = false;
                }
            }
            inP[idx] = false;
            if (left) {
                while (val < min && lens > 1) {
                    if (lens % 2 == 1) {
                        ans++;
                        lens = (lens + 1) / 2;
                    } else {
                        lens /= 2;
                    }
                    val++;
                }
                if (val == min) {
                    L[pt] = lens + L[idx];
                    v[pt] = min;
                } else {
                    ans += min - val;
                    L[pt] = lens + L[idx];
                    v[pt] = min;
                }
                if (l[idx] != -1) {
                    r[l[idx]] = pt;
                    l[pt] = l[idx];
                } else {
                    l[pt] = -1;
                }
                if (r[id] != -1) {
                    l[r[id]] = pt;
                    r[pt] = r[id];
                } else {
                    r[pt] = -1;
                }

            } else {
                while (val < min && lens > 1) {
                    ans += lens % 2;
                    lens /= 2;
                    val++;
                }
                if (val == min) {
                    L[pt] = lens + L[idx];
                    v[pt] = min;
                } else {
                    ans += min - val;
                    L[pt] = lens + L[idx];
                    v[pt] = min;
                }
                if (r[idx] != -1) {
                    l[r[idx]] = pt;
                    r[pt] = r[idx];
                } else {
                    r[pt] = -1;
                }
                if (l[id] != -1) {
                    r[l[id]] = pt;
                    l[pt] = l[id];
                } else {
                    l[pt] = -1;
                }
            }

            inP[pt] = true;
            p.offer(new int[]{v[pt], L[pt], pt});

            pt++;

        }

        out.println(ans);

    }

    static Kattio sc = new Kattio();
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    static class Kattio {
        static BufferedReader r;
        static StringTokenizer st;

        public Kattio() {
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

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}