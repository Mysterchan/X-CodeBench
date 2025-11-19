import java.util.*;

public class Main {

    private static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt();
            List<List<Integer>> adj = new ArrayList<>(n + 1);
            for (int i = 0; i <= n; i++) {
                adj.add(new ArrayList<>());
            }

            for (int i = 0; i < n - 1; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();
                adj.get(u).add(v);
                adj.get(v).add(u);
            }

            long totalCoolness = solve(n, adj);
            System.out.println(totalCoolness);
        }
        scanner.close();
    }

    private static long solve(int n, List<List<Integer>> adj) {
        long totalCoolness = 0;
        for (int d = 1; d < n; ++d) {
            long count = countColoringsWithDistance(n, adj, d);
            totalCoolness = (totalCoolness + (d * count) % MOD) % MOD;
        }
        return totalCoolness;
    }

    private static long countColoringsWithDistance(int n, List<List<Integer>> adj, int distance) {
        long count = 0;
        List<Pair> pairs = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                if (getDistance(i, j, adj) == distance) {
                    pairs.add(new Pair(i, j));
                }
            }
        }

        if (pairs.isEmpty()) {
            return 0;
        }
        for (Pair pair : pairs) {
            int redNode = pair.u;
            int blueNode = pair.v;
            long validColoringsForPair = 0;

            for (int i = 0; i < power(3, n); ++i) {
                int[] colors = new int[n + 1];
                int temp = i;
                for (int j = 1; j <= n; ++j) {
                    colors[j] = temp % 3;
                    temp /= 3;
                }
                boolean hasRed = false;
                boolean hasBlue = false;
                int maxDistForThisColoring = 0;

                if (colors[redNode] == 0 && colors[blueNode] == 1)
                {
                    hasRed = true;
                    hasBlue = true;
                    for (int u = 1; u <= n; ++u)
                    {
                        if (colors[u] == 0)
                        {
                            for (int v = 1; v <= n; ++v)
                            {
                                if (colors[v] == 1)
                                {
                                    maxDistForThisColoring = Math.max(maxDistForThisColoring, getDistance(u,v,adj));
                                }
                            }
                        }
                    }
                    if (maxDistForThisColoring == distance)
                        validColoringsForPair++;
                }
                else if (colors[redNode] == 1 && colors[blueNode] == 0)
                {
                    hasRed = true;
                    hasBlue = true;
                    for (int u = 1; u <= n; ++u)
                    {
                        if (colors[u] == 0)
                        {
                            for (int v = 1; v <= n; ++v)
                            {
                                if (colors[v] == 1)
                                {
                                    maxDistForThisColoring = Math.max(maxDistForThisColoring, getDistance(u,v,adj));
                                }
                            }
                        }
                    }
                    if (maxDistForThisColoring == distance)
                        validColoringsForPair++;
                }
                else
                {
                     for (int u = 1; u <= n; u++) {
                        if (colors[u] == 0) {
                            hasRed = true;
                            for (int v = 1; v <= n; v++) {
                                if (colors[v] == 1) {
                                    hasBlue = true;
                                    maxDistForThisColoring = Math.max(maxDistForThisColoring, getDistance(u, v, adj));
                                }
                            }
                        }
                    }
                    if (hasRed && hasBlue && maxDistForThisColoring == distance)
                        validColoringsForPair++;
                }


            }
            count = (count + validColoringsForPair) % MOD;
        }

        return count;
    }

    private static int getDistance(int start, int end, List<List<Integer>> adj) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        Map<Integer, Integer> distance = new HashMap<>();
        distance.put(start, 0);
        Set<Integer> visited = new HashSet<>();
        visited.add(start);

        while (!queue.isEmpty()) {
            int u = queue.poll();
            if (u == end) {
                return distance.get(end);
            }
            for (int v : adj.get(u)) {
                if (!visited.contains(v)) {
                    visited.add(v);
                    distance.put(v, distance.get(u) + 1);
                    queue.offer(v);
                }
            }
        }
        return -1;
    }

    private static long power(long base, long exp, long mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }

    private static long power(long base, long exp) {
        long res = 1;
        while (exp > 0) {
            if (exp % 2 == 1) res *= base;
            base *= base;
            exp >>= 1;
        }
        return res;
    }

    private static class Pair {
        int u;
        int v;

        public Pair(int u, int v) {
            this.u = u;
            this.v = v;
        }
    }
}
