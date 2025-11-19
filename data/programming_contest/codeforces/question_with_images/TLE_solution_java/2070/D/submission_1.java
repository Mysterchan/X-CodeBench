import java.sql.SQLOutput;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static int MOD = 998244353;
    static TreeMap<Integer, HashSet<Integer>> verByLevel;
    static HashMap<Integer, HashSet<Integer>> children;
    static long[] res;
    static int[] ver;

    public static void main(String[] args) {
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            solve();
        }
    }

    static void solve() {
        int n = sc.nextInt();
        verByLevel = new TreeMap<>(Comparator.reverseOrder());
        children = new HashMap<>();
        ver = new int[n + 1];
        for (int i = 2; i < n + 1; i++) {
            int p = sc.nextInt();
            ver[i] = ver[p] + 1;
            verByLevel.computeIfAbsent(ver[i], k -> new HashSet<>()).add(i);
            children.computeIfAbsent(p, k -> new HashSet<>()).add(i);
        }

        res = new long[n + 1];
        for (Map.Entry<Integer, HashSet<Integer>> e: verByLevel.entrySet()) {
            for (Integer v: e.getValue()) {
                countPaths(v);
            }
        }
        countPaths(1);
        System.out.println(res[1] % MOD);
    }

    static long countPaths(int v) {
        if (res[v] != 0) return res[v];
        HashSet<Integer> nextLowerLevel = verByLevel.get(ver[v] + 1);
        if (nextLowerLevel == null) {
            res[v] = 1;
            return res[v];
        }
        HashSet<Integer> validPaths = new HashSet<>(nextLowerLevel);
        if (v != 1) validPaths.removeAll(children.getOrDefault(v, new HashSet<>()));
        long r = 0;
        for (Integer e: validPaths) {
            r += countPaths(e) % MOD;
        }
        res[v] = (1 + r) % MOD;
        return res[v];
    }
}
