import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static int[] subPathCount;
    private static boolean[] hasMonster;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCaseCount = scanner.nextInt();
        StringBuilder output = new StringBuilder();
        while (testCaseCount-- > 0) {
            int n = scanner.nextInt();
            hasMonster = new boolean[n + 1];
            subPathCount = new int[n + 1];
            List<List<Integer>> tree = new ArrayList<>();
            for (int i = 0; i <= n; i++) {
                tree.add(new ArrayList<>());
            }

            for (int i = 1; i <= n; i++) {
                hasMonster[i] = scanner.nextInt() == 1;
            }

            for (int i = 0; i < n - 1; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();
                tree.get(u).add(v);
                tree.get(v).add(u);
            }

            int initialPaths = dfs(tree, 1, -1);
            output.append(initialPaths).append("\n");

            int q = scanner.nextInt();
            while (q-- > 0) {
                int v = scanner.nextInt();
                updateMonsterStatus(tree, v, -1);
                int newPaths = dfs(tree, 1, -1);
                output.append(newPaths).append("\n");
            }
        }
        System.out.print(output.toString());
    }

    private static int dfs(List<List<Integer>> tree, int node, int parent) {
        int paths = 0;
        boolean hasMonstersInChild = false;
        for (int neighbor : tree.get(node)) {
            if (neighbor == parent) continue;
            int childPaths = dfs(tree, neighbor, node);
            paths += childPaths;
            if (childPaths > 0 || hasMonster[neighbor]) {
                hasMonstersInChild = true;
            }
        }
        if (hasMonstersInChild || hasMonster[node]) {
            paths++;
        }
        return paths;
    }

    private static void updateMonsterStatus(List<List<Integer>> tree, int node, int parent) {
        hasMonster[node] = !hasMonster[node];
        for (int neighbor : tree.get(node)) {
            if (neighbor != parent) {
                updateMonsterStatus(tree, neighbor, node);
            }
        }
    }
}