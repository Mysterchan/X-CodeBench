import java.util.*;

public class Main {
    static boolean dfs(int curr, boolean[] vis, List<List<Integer>> adj, int dest, List<Integer> path){
        if(curr == dest){
            for (int i = 0; i < path.size(); i++) {
                System.out.print(path.get(i) + " ");
            }
            System.out.println(dest);
            return true;
        }

        vis[curr] = true;

        for (int v: adj.get(curr)){
            if(!vis[v]){
                path.add(curr);
                if(dfs(v, vis, adj, dest, path)) return true;
                path.remove(path.size()-1);
            }
        }

        return false;

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while (t-- > 0){
            int n = sc.nextInt();
            int m = sc.nextInt();

            int src = sc.nextInt();
            int dest = sc.nextInt();

            List<List<Integer>> adj = new ArrayList<>();

            for (int i = 0; i < n+1; i++) {
                adj.add(new ArrayList<>());
            }

            for (int i = 0; i < m; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();

                adj.get(u).add(v);
                adj.get(v).add(u);
            }

            for (int i = 0; i < n; i++) {
                Collections.sort(adj.get(i));
            }

            dfs(src, new boolean[n+1], adj, dest, new ArrayList<>());
        }
    }
}