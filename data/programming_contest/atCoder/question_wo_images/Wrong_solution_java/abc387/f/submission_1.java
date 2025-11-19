import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static final int MOD = 998244353;
    static int[] A;
    static List<List<Integer>> revAdj;
    static int[] visited;
    static int[] path;
    static Set<Integer> cycleNodes;
    static Set<Integer> compNodes;
    static long[][] F;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        int N = sc.nextInt();
        int M = sc.nextInt();

        A = new int[N + 1];
        revAdj = new ArrayList<>(N + 1);
        for (int i = 0; i <= N; i++) {
            revAdj.add(new ArrayList<>());
        }

        for (int i = 1; i <= N; i++) {
            A[i] = sc.nextInt();
            revAdj.get(A[i]).add(i);
        }

        visited = new int[N + 1];
        path = new int[N + 1];
        F = new long[N + 1][M + 1];
        long totalAnswer = 1;

        for (int i = 1; i <= N; i++) {
            if (visited[i] == 0) {
                compNodes = new HashSet<>();
                cycleNodes = new HashSet<>();

                findCycle(i, 1);

                findAllNodesInComponent(i);

                Set<Integer> treeNodes = new HashSet<>(compNodes);
                treeNodes.removeAll(cycleNodes);

                int[] revOutDegree = new int[N + 1];

                List<List<Integer>> treeRevAdj = new ArrayList<>(N + 1);
                for(int k=0; k<=N; k++) treeRevAdj.add(new ArrayList<>());

                for (int j : treeNodes) {
                    int u = A[j];
                    if (treeNodes.contains(u)) {
                        revOutDegree[u]++;
                        treeRevAdj.get(u).add(j);
                    }
                }

                Queue<Integer> q = new ArrayDeque<>();
                for (int u : treeNodes) {
                    if (revOutDegree[u] == 0) {
                        q.add(u);
                    }
                }

                List<Integer> topOrder = new ArrayList<>();
                while (!q.isEmpty()) {
                    int u = q.poll();
                    topOrder.add(u);

                    int v = A[u];
                    if (treeNodes.contains(v)) {
                        revOutDegree[v]--;
                        if (revOutDegree[v] == 0) {
                            q.add(v);
                        }
                    }
                }

                for (int u : topOrder) {
                    for (int v = 1; v <= M; v++) {
                        long prod = 1;
                        for (int child : treeRevAdj.get(u)) {

                            prod = (prod * F[child][v]) % MOD;
                        }

                        long P_uv = prod;
                        F[u][v] = (F[u][v - 1] + P_uv) % MOD;
                    }
                }

                long compAnswer = 0;
                for (int k = 1; k <= M; k++) {
                    long waysK = 1;
                    for (int c : cycleNodes) {
                        for (int child : revAdj.get(c)) {
                            if (treeNodes.contains(child)) {
                                waysK = (waysK * F[child][k]) % MOD;
                            }
                        }
                    }
                    compAnswer = (compAnswer + waysK) % MOD;
                }
                totalAnswer = (totalAnswer * compAnswer) % MOD;
            }
        }

        out.println(totalAnswer);
        out.flush();
        sc.close();
    }

    static void findCycle(int u, int depth) {
        visited[u] = 1;
        path[depth] = u;
        int v = A[u];

        if (visited[v] == 1) {
            for (int i = depth; ; i--) {
                cycleNodes.add(path[i]);
                if (path[i] == v) break;
            }
        } else if (visited[v] == 0) {
            findCycle(v, depth + 1);
        }

        visited[u] = 2;
    }

    static void findAllNodesInComponent(int start) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        compNodes.add(start);

        while (!q.isEmpty()) {
            int u = q.poll();

            int v = A[u];
            if (visited[v] == 0) {
                visited[v] = 2;
                compNodes.add(v);
                q.add(v);
            }

            for (int neigh : revAdj.get(u)) {
                if (visited[neigh] == 0) {
                    visited[neigh] = 2;
                    compNodes.add(neigh);
                    q.add(neigh);
                }
            }
        }
    }
}