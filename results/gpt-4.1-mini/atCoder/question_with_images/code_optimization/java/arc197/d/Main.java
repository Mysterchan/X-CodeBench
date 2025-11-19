import java.util.Scanner;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        // Since sum of N^2 over all test cases <= 400^2,
        // we can safely process each test case independently.

        StringBuilder sb = new StringBuilder();
        for (int _t = 0; _t < T; _t++) {
            int n = sc.nextInt();
            int[][] A = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    A[i][j] = sc.nextInt();
                }
            }
            sb.append(solve(n, A)).append('\n');
        }
        sc.close();
        System.out.print(sb);
    }

    // Explanation of approach:
    // The problem describes a tree G rooted at vertex 1,
    // and the matrix A encodes the ancestor-descendant relations.
    //
    // A[i][j] = 1 iff j is ancestor of i or i is ancestor of j in G rooted at 1.
    //
    // This means A[i][j] = 1 iff the path from 1 to i and the path from 1 to j
    // share vertex j or i respectively, i.e., the paths intersect at j or i.
    //
    // The matrix A is symmetric and has 1 on diagonal.
    //
    // The problem reduces to counting the number of trees G rooted at 1
    // consistent with A.
    //
    // Key insight:
    // For each vertex v, define S_v = {u | A[v][u] = 1} = the set of vertices on the path from 1 to v.
    //
    // The sets S_v form a laminar family (nested or disjoint).
    //
    // The problem reduces to counting the number of ways to build a rooted tree
    // with these sets as paths.
    //
    // The original code uses a recursive approach with sets and BFS to find connected components.
    //
    // We optimize by:
    // - Using bitsets for fast set operations.
    // - Avoiding TreeSet and HashSet overhead.
    // - Using arrays and adjacency lists.
    // - Precomputing factorials for permutations.
    //
    // The main bottleneck is the recursive decomposition of the vertex set.
    //
    // We implement the same logic but with arrays and bitsets for speed.

    static int solve(int n, int[][] A) {
        // Check if vertex 1 (index 0) is connected to all vertices (A[0][*] == 1)
        for (int i = 0; i < n; i++) {
            if (A[0][i] == 0) return 0;
        }

        // Build adjacency lists for each vertex: neighbors are those j where A[i][j] == 1
        // We'll store neighbors excluding vertex 0 (root) for convenience
        int[][] neighbors = new int[n][];
        int[] deg = new int[n];
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 1) count++;
            }
            neighbors[i] = new int[count];
            int idx = 0;
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 1) neighbors[i][idx++] = j;
            }
            deg[i] = count;
        }

        // We will implement the recursive counting function:
        // Input: subset of vertices (excluding 0), represented as boolean array or bitset
        // Output: number of valid trees on that subset with root 0 connected to all

        // To speed up, we use an int[] to store the subset vertices and a boolean[] to mark membership.

        // Precompute factorials up to n for permutations
        long[] fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }

        // Prepare data structures for recursion
        boolean[] inSet = new boolean[n];
        for (int i = 1; i < n; i++) inSet[i] = true;

        return (int) count(inSet, neighbors, fact, n);
    }

    static long count(boolean[] inSet, int[][] neighbors, long[] fact, int n) {
        // Count number of vertices in inSet
        int size = 0;
        for (int i = 1; i < n; i++) if (inSet[i]) size++;
        if (size == 0) return 1;
        if (size == 1) return 1;

        // Find vertices in inSet that are connected to all other vertices in inSet
        // i.e. neighbors[i] contains all vertices in inSet (except possibly 0)
        // These vertices can be considered "roots" of the current subtree

        // To check quickly, we count how many neighbors in inSet each vertex has
        // and compare with size (since A[i][i] = 1, neighbors include self)
        // But neighbors include vertex 0, which is not in inSet, so we must count carefully.

        // We'll count how many neighbors in inSet each vertex has (excluding 0)
        // and check if count == size (full connection)

        // Also, root candidates must be in inSet

        int rootCount = 0;
        for (int v = 1; v < n; v++) {
            if (!inSet[v]) continue;
            int cnt = 0;
            for (int u : neighbors[v]) {
                if (u == 0) continue; // exclude root 0
                if (inSet[u]) cnt++;
            }
            if (cnt == size) rootCount++;
        }

        long res = 1;
        if (rootCount > 1) {
            // multiply by rootCount! modulo MOD
            res = fact[rootCount];
        }

        // Remove root candidates from inSet
        for (int v = 1; v < n; v++) {
            if (!inSet[v]) continue;
            int cnt = 0;
            for (int u : neighbors[v]) {
                if (u == 0) continue;
                if (inSet[u]) cnt++;
            }
            if (cnt == size) {
                inSet[v] = false;
            }
        }

        // Now, the remaining vertices in inSet form connected components
        // We find connected components and recurse on each

        // Build adjacency for remaining vertices
        // We'll do BFS to find components

        boolean[] visited = new boolean[n];
        for (int v = 1; v < n; v++) visited[v] = !inSet[v];

        for (int v = 1; v < n; v++) {
            if (!visited[v]) {
                // BFS
                int[] queue = new int[n];
                int head = 0, tail = 0;
                queue[tail++] = v;
                visited[v] = true;

                // Collect vertices in this component
                // We'll create a new inSet array for recursion
                boolean[] compSet = new boolean[n];
                compSet[v] = true;

                while (head < tail) {
                    int cur = queue[head++];
                    for (int w : neighbors[cur]) {
                        if (w == 0) continue; // root 0 not in subset
                        if (inSet[w] && !visited[w]) {
                            visited[w] = true;
                            compSet[w] = true;
                            queue[tail++] = w;
                        }
                    }
                }

                // Recurse on this component
                long subRes = count(compSet, neighbors, fact, n);
                res = (res * subRes) % MOD;
            }
        }

        return res;
    }
}