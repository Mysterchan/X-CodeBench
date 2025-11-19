import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static final int MOD = 998244353;

    public static void main(String[] args) {
        int t = sc.nextInt();
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < t; i++) {
            output.append(solve()).append("\n");
        }
        System.out.print(output);
    }

    static long solve() {
        int n = sc.nextInt();
        List<List<Integer>> tree = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) {
            tree.add(new ArrayList<>());
        }
        for (int i = 2; i <= n; i++) {
            int p = sc.nextInt();
            tree.get(p).add(i);
        }

        long[] res = new long[n + 1];
        Arrays.fill(res, 1); // Each node can begin its own sequence

        // DFS to count valid paths
        countPaths(1, tree, res);
        return res[1];
    }

    static void countPaths(int v, List<List<Integer>> tree, long[] res) {
        for (int child : tree.get(v)) {
            countPaths(child, tree, res);
            // Updating res[v] with valid paths from child, excluding direct connections
            res[v] = (res[v] * (res[child] + 1)) % MOD;
        }
    }
}