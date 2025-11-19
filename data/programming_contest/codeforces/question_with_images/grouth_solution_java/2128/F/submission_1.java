import java.util.*;


public class Main {
    static class Line {
        int u;
        int v;
        long l;
        long r;
    }

    static class DijNode implements Comparable<DijNode> {
            int v;
            long w;

            public DijNode(int v, long w) {
                this.v = v;
                this.w = w;
            }

            @Override
            public int compareTo(DijNode other) {
                return Long.compare(this.w, other.w);
            }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int tc = 0; tc < T; tc++) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int k = scanner.nextInt();
            k--;

            List<List<Line>> line = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                line.add(new ArrayList<>());
            }

            for (int i = 0; i < m; i++) {
                Line lx = new Line();
                int u = scanner.nextInt();
                lx.v = scanner.nextInt();
                lx.l = scanner.nextLong();
                lx.r = scanner.nextLong();
                u--;
                lx.v--;
                line.get(u).add(lx);
                Line lxReverse = new Line();
                lxReverse.u = lx.v;
                lxReverse.v = u;
                lxReverse.l = lx.l;
                lxReverse.r = lx.r;
                line.get(lx.v).add(lxReverse);
            }

            long[] disk = new long[n];
            Arrays.fill(disk, Long.MAX_VALUE);
            boolean[] vis = new boolean[n];
            PriorityQueue<DijNode> p = new PriorityQueue<>();
            p.add(new DijNode(k, 0));
            disk[k] = 0;

            while (!p.isEmpty()) {
                DijNode current = p.poll();
                int t = current.v;
                if (vis[t]) continue;
                vis[t] = true;
                disk[t] = current.w;
                for (Line edge : line.get(t)) {
                    int nextV = edge.v;
                    long nextW = disk[t] + edge.r;
                    if (!vis[nextV] && nextW < disk[nextV]) {
                        disk[nextV] = nextW;
                        p.add(new DijNode(nextV, nextW));
                    }
                }
            }

            long[] dis0 = new long[n];
            Arrays.fill(dis0, Long.MAX_VALUE);
            Arrays.fill(vis, false);
            p.clear();
            p.add(new DijNode(0, -disk[0]));
            dis0[0] = -disk[0];

            while (!p.isEmpty()) {
                DijNode current = p.poll();
                int t = current.v;
                if (vis[t]) continue;
                if (disk[t] <= current.w) continue;
                vis[t] = true;
                dis0[t] = current.w;
                for (Line edge : line.get(t)) {
                    int nextV = edge.v;
                    long nextW = Math.max(dis0[t] + edge.l, -disk[nextV]);
                    if (!vis[nextV] && nextW < dis0[nextV]) {
                        dis0[nextV] = nextW;
                        p.add(new DijNode(nextV, nextW));
                    }
                }
            }

            if (vis[n - 1]) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        scanner.close();
    }
}
