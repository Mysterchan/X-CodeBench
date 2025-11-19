import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 0; t < T; t++) {
            int n = sc.nextInt();
            int[] a = new int[n];
            int[] b = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            for (int i = 0; i < n; i++) b[i] = sc.nextInt();

            boolean res = solve(a, b);
            System.out.println(res ? "Yes" : "No");
        }
    }

    static boolean solve(int[] a, int[] b) {
        int n = a.length;
        String tgt = str(b);
        Set<String> vis = new HashSet<>();
        Queue<int[]> q = new LinkedList<>();
        q.add(a);
        vis.add(str(a));

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (str(cur).equals(tgt)) return true;

            for (int i = 0; i < n; i++) {
                for (int j = i; j < n; j++) {
                    for (int k = j + 1; k < n; k++) {
                        for (int l = k; l < n; l++) {
                            if (sum(cur, i, j) == sum(cur, k, l)) {
                                int[] nxt = swap(cur, i, j, k, l);
                                String s = str(nxt);
                                if (!vis.contains(s)) {
                                    vis.add(s);
                                    q.add(nxt);
                                }
                            }
                        }
                    }
                }
            }
        }
        return false;
    }

    static int sum(int[] a, int i, int j) {
        int s = 0;
        for (int x = i; x <= j; x++) s += a[x];
        return s;
    }

    static int[] swap(int[] a, int i, int j, int k, int l) {
        List<Integer> r = new ArrayList<>();
        for (int x = 0; x < i; x++) r.add(a[x]);
        for (int x = k; x <= l; x++) r.add(a[x]);
        for (int x = j + 1; x < k; x++) r.add(a[x]);
        for (int x = i; x <= j; x++) r.add(a[x]);
        for (int x = l + 1; x < a.length; x++) r.add(a[x]);

        int[] res = new int[a.length];
        for (int x = 0; x < a.length; x++) res[x] = r.get(x);
        return res;
    }

    static String str(int[] a) {
        StringBuilder sb = new StringBuilder();
        for (int x : a) sb.append(x);
        return sb.toString();
    }
}