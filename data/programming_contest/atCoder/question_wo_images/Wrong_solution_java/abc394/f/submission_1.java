import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Arrays;

public class Main {

    static List<Integer>[] adj;

    static final long INVALID = -1;

    static long pack(long size, boolean has_deg4) {
        if (size < 0) return INVALID;
        return (size << 1) | (has_deg4 ? 1 : 0);
    }

    static long unpack_size(long packed) {
        if (packed == INVALID) return -1;
        return packed >> 1;
    }

    static boolean unpack_has(long packed) {
        if (packed == INVALID) return false;
        return (packed & 1) == 1;
    }

    static long merge(long p1, long p2) {
        if (p1 == INVALID || p2 == INVALID) {
            return INVALID;
        }
        return pack(unpack_size(p1) + unpack_size(p2), unpack_has(p1) || unpack_has(p2));
    }

    static long best_of(long p1, long p2) {
        if (p1 == INVALID) return p2;
        if (p2 == INVALID) return p1;

        return Math.max(p1, p2);
    }

    static long best_of(long p1, long p2, long p3) {
        return best_of(p1, best_of(p2, p3));
    }

    static long[] solve(int u, int p) {

        long[] K = new long[5];
        Arrays.fill(K, INVALID);
        K[0] = pack(0, false);

        long best_child_alkanes = pack(0, false);

        for (int v : adj[u]) {
            if (v == p) continue;

            long[] res_v = solve(v, u);
            long v_alkane = res_v[0];
            long v_connect = best_of(res_v[1], res_v[2]);

            best_child_alkanes = merge(best_child_alkanes, v_alkane);

            for (int d = 4; d >= 0; d--) {
                if (K[d] == INVALID) continue;

                if (d < 4 && v_connect != INVALID) {
                    K[d + 1] = best_of(K[d + 1], merge(K[d], v_connect));
                }

            }
        }

        long u_L = pack(1, false);
        long u_I = pack(1, true);

        long alkane_L = merge(u_L, merge(K[1], best_child_alkanes));

        long alkane_I = merge(u_I, merge(K[4], best_child_alkanes));

        long alkane_out = best_child_alkanes;

        long best_alkane = best_of(alkane_L, alkane_I, alkane_out);
        long my_res0 = (best_alkane != INVALID && unpack_has(best_alkane)) ? best_alkane : INVALID;

        long my_res1 = merge(u_L, merge(K[0], best_child_alkanes));

        long my_res2 = merge(u_I, merge(K[3], best_child_alkanes));

        return new long[]{my_res0, my_res1, my_res2};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        adj = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }
        sc.close();

        if (N == 1) {
             System.out.println(-1);
             return;
        }

        long[] root_res = solve(1, 0);
        long final_packed = root_res[0];

        if (final_packed != INVALID) {
            System.out.println(unpack_size(final_packed));
        } else {
            System.out.println(-1);
        }
    }
}