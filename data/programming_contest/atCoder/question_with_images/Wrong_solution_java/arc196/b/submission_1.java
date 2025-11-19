import java.util.*;

public class Main {
    static final int MOD = 998244353;
    static class DSU {
        int[] parent, rank, parity;
        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            parity = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int x) {
            if (parent[x] != x) {
                int orig = parent[x];
                parent[x] = find(parent[x]);
                parity[x] ^= parity[orig];
            }
            return parent[x];
        }
        boolean union(int x, int y, int d) {
            int rx = find(x);
            int ry = find(y);
            if (rx == ry) {
                return (parity[x] ^ parity[y]) == d;
            }
            parent[ry] = rx;
            parity[ry] = parity[x] ^ parity[y] ^ d;
            return true;
        }
    }
    static long modPow(long a, long b, int mod) {
        long res = 1;
        while (b > 0) {
            if ((b & 1) == 1) res = res * a % mod;
            a = a * a % mod;
            b >>= 1;
        }
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        while (T-- > 0) {
            int H = sc.nextInt();
            int W = sc.nextInt();
            sc.nextLine();
            String[] S = new String[H];
            for (int i = 0; i < H; i++) {
                S[i] = sc.nextLine().trim();
            }
            DSU dsu = new DSU(H * W);
            boolean ok = true;
            for (int i = 0; i < H && ok; i++) {
                for (int j = 0; j < W && ok; j++) {
                    int curr = i * W + j;
                    char c = S[i].charAt(j);
                    int right = i * W + ((j + 1) % W);
                    int down = ((i + 1) % H) * W + j;
                    if (c == 'A') {
                        if (!dsu.union(curr, right, 1) || !dsu.union(curr, down, 1)) {
                            ok = false;
                        }
                    } else {
                        if (!dsu.union(right, down, 0)) {
                            ok = false;
                        }
                    }
                }
            }
            if (!ok) {
                sb.append("0\n");
            } else {
                Set<Integer> components = new HashSet<>();
                for (int i = 0; i < H * W; i++) {
                    components.add(dsu.find(i));
                }
                int comps = components.size();
                sb.append(modPow(2, comps, MOD)).append("\n");
            }
        }
        System.out.print(sb);
    }
}