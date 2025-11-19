import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int nextInt() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(br.readLine());
        }
        return Integer.parseInt(st.nextToken());
    }

    static int n, m, x;
    static int N = (int) 2e5 + 5;

    static ArrayList<Integer> g[][]=new ArrayList[N][2];

    static long dis[][]=new long[N][2];

    static class Node implements Comparable<Node> {
        int u, x;
        long cost;

        public Node(int u, int x, long cost) {
            this.u = u;
            this.x = x;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node other) {
            return Long.compare(this.cost, other.cost);
        }
    }

    static void dijkstra(int s) {
        for (int u = 1; u <= n; u++) {
            Arrays.fill(dis[u], Long.MAX_VALUE);
        }
        dis[s][0] = 0;
        PriorityQueue<Node> q = new PriorityQueue<>();
        q.add(new Node(s, 0, 0));

        while (!q.isEmpty()) {
            Node curr = q.poll();
            int u = curr.u;
            int newx = curr.x;
            long cost = curr.cost;

            if (cost > dis[u][newx]) {
                continue;
            }

            for (int v : g[u][newx]) {
                if (dis[v][newx] > cost + 1) {
                    dis[v][newx] = cost + 1;
                    q.add(new Node(v, newx, dis[v][newx]));
                }
            }

            int cnt = 1 - newx;
            for (int v : g[u][cnt]) {
                if (dis[v][cnt] > cost + 1 + x) {
                    dis[v][cnt] = cost + 1 + x;
                    q.add(new Node(v, cnt, dis[v][cnt]));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        n = nextInt();
        m = nextInt();
        x = nextInt();
        for (int u = 1; u <= n; u++) {
            g[u][0] = new ArrayList<>();
            g[u][1] = new ArrayList<>();
        }

        for (int i = 1; i <= m; i++) {
            int u = nextInt();
            int v = nextInt();
            g[u][0].add(v);
            g[v][1].add(u);
        }

        dijkstra(1);

        long ans = Math.min(dis[n][0], dis[n][1]);
        System.out.println(ans);
    }
}