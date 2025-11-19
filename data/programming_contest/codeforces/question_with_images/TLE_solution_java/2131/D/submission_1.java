import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        while (T-- > 0) {
            int n = scanner.nextInt();
            Map<Integer, List<Integer>> g = new HashMap<>();
            Map<Integer, Integer> deg = new HashMap<>();
            int u,v;
            for(int i=0; i<n; i++) {
                g.put(i+1, new ArrayList<>());
                deg.put(i+1, 0);
            }
            for (int i = 1; i < n; i++) {
                u = scanner.nextInt();
                v = scanner.nextInt();
                g.get(u).add(v);
                g.get(v).add(u);
                deg.put(u, deg.get(u)+1);
                deg.put(v, deg.get(v)+1);
            }
            if ( n <= 3) {
                System.out.println(0);
                continue;
            }
            var allLeafs = deg.values().stream().mapToInt(e -> e == 1 ? 1 : 0).sum();
            var mx = g.values().stream()
                    .map(adj -> adj.stream().mapToInt(e -> deg.get(e) == 1 ? 1 : 0).sum())
                    .max(Integer::compareTo).get();
            System.out.println(allLeafs - mx);
        }

    }

}
