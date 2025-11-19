import java.util.*;

public class Main {
    static final int MOD = 998244353;
    static int N;
    static int[] A;
    static Map<String, Long> memo = new HashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        A = new int[N];

        List<Integer> unknowns = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
            if (A[i] == -1) {
                unknowns.add(i);
            }
        }

        System.out.println(countGoodSequences(unknowns, 0));
    }

    static long countGoodSequences(List<Integer> unknowns, int pos) {
        if (pos == unknowns.size()) {
            return isGoodSequence() ? 1 : 0;
        }

        String key = Arrays.toString(A) + ":" + pos;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        long result = 0;
        int idx = unknowns.get(pos);

        for (int val = 1; val <= N; val++) {
            A[idx] = val;
            if (canBeGood(unknowns, pos)) {
                result = (result + countGoodSequences(unknowns, pos + 1)) % MOD;
            }
        }

        A[idx] = -1;
        memo.put(key, result);
        return result;
    }

    static boolean canBeGood(List<Integer> unknowns, int pos) {

        return true;
    }

    static boolean isGoodSequence() {

        for (int l = 1; l <= N; l++) {
            for (int r = l; r <= N; r++) {
                if (!hasValidX(l, r)) {
                    return false;
                }
            }
        }
        return true;
    }

    static boolean hasValidX(int l, int r) {

        for (int x = l; x <= r; x++) {
            if (formsConnectedGraph(l, r, x)) {
                return true;
            }
        }
        return false;
    }

    static boolean formsConnectedGraph(int l, int r, int skip) {
        Set<Integer> vertices = new HashSet<>();
        List<int[]> edges = new ArrayList<>();

        for (int i = l; i <= r; i++) {
            vertices.add(i);
            if (i != skip && A[i-1] >= l && A[i-1] <= r) {
                edges.add(new int[]{i, A[i-1]});
            }
        }

        return edges.size() == vertices.size() - 1 && isConnected(vertices, edges);
    }

    static boolean isConnected(Set<Integer> vertices, List<int[]> edges) {
        if (vertices.size() <= 1) return true;

        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int v : vertices) adj.put(v, new ArrayList<>());

        for (int[] edge : edges) {
            if (vertices.contains(edge[0]) && vertices.contains(edge[1])) {
                adj.get(edge[0]).add(edge[1]);
                adj.get(edge[1]).add(edge[0]);
            }
        }

        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        int start = vertices.iterator().next();

        queue.add(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int neighbor : adj.get(curr)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }

        return visited.size() == vertices.size();
    }
}