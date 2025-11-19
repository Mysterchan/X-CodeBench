import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int[] deg = new int[n + 1];
            List<Integer>[] g = new ArrayList[n + 1];
            for (int i = 1; i <= n; i++) {
                g[i] = new ArrayList<>();
            }
            for (int i = 1; i < n; i++) {
                String[] parts = br.readLine().split(" ");
                int u = Integer.parseInt(parts[0]);
                int v = Integer.parseInt(parts[1]);
                g[u].add(v);
                g[v].add(u);
                deg[u]++;
                deg[v]++;
            }
            if (n <= 3) {
                sb.append("0\n");
                continue;
            }
            int allLeafs = 0;
            for (int i = 1; i <= n; i++) {
                if (deg[i] == 1) allLeafs++;
            }
            int maxLeafsAdj = 0;
            for (int i = 1; i <= n; i++) {
                int leafCount = 0;
                for (int adj : g[i]) {
                    if (deg[adj] == 1) leafCount++;
                }
                if (leafCount > maxLeafsAdj) maxLeafsAdj = leafCount;
            }
            sb.append(allLeafs - maxLeafsAdj).append('\n');
        }
        System.out.print(sb);
    }
}