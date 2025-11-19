import java.util.*;

public class Main {
    private static class Edge {
        int to;
        int weight;

        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        long[] weights = new long[n + 1];

        for (int i = 1; i <= n; i++) {
            weights[i] = sc.nextLong();
        }

        int[][] ranges = new int[n][2];
        for (int i = 0; i < n; i++) {
            ranges[i][0] = sc.nextInt();
            ranges[i][1] = sc.nextInt();
        }

        List<List<Edge>> adj = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }

        // Build the graph with only the necessary edges
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (ranges[i][1] < ranges[j][0] || ranges[j][1] < ranges[i][0]) {
                    adj.get(i + 1).add(new Edge(j + 1, weights[j + 1]));
                    adj.get(j + 1).add(new Edge(i + 1, weights[i + 1]));
                }
            }
        }

        int q = sc.nextInt();
        StringBuilder output = new StringBuilder();

        for (int i = 0; i < q; i++) {
            int s = sc.nextInt();
            int t = sc.nextInt();
            output.append(dijkstra(adj, s, t, weights)).append("\n");
        }

        System.out.print(output);
    }

    public static long dijkstra(List<List<Edge>> adj, int start, int end, long[] weights) {
        long[] minWeight = new long[weights.length];
        Arrays.fill(minWeight, Long.MAX_VALUE);
        minWeight[start] = weights[start];

        PriorityQueue<Edge> pq = new PriorityQueue<>(Comparator.comparingLong(e -> e.weight));
        pq.add(new Edge(start, minWeight[start]));

        while (!pq.isEmpty()) {
            Edge current = pq.poll();

            if (current.to == end) {
                return current.weight;
            }

            for (Edge neighbor : adj.get(current.to)) {
                long newWeight = current.weight + weights[neighbor.to];
                
                if (newWeight < minWeight[neighbor.to]) {
                    minWeight[neighbor.to] = newWeight;
                    pq.add(new Edge(neighbor.to, newWeight));
                }
            }
        }
        return -1; // No path found
    }
}