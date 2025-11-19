import java.util.*;
import java.io.*;

public class Main {
    public static int n, q;
    public static long[] weights;
    public static ArrayList<Integer>[] tree;
    public static int[] parent, subtreeSize;
    public static long totalWeight;

    public static void dfs(int node, int par) {
        parent[node] = par;
        subtreeSize[node] = 1;
        for (int neighbor : tree[node]) {
            if (neighbor == par) continue;
            dfs(neighbor, node);
            subtreeSize[node] += subtreeSize[neighbor];
        }
    }

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        n = s.nextInt();
        
        tree = new ArrayList[n + 1];
        weights = new long[n + 1];
        parent = new int[n + 1];
        subtreeSize = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            tree[i] = new ArrayList<>();
            weights[i] = 1; // Initialize weights to 1
        }
        
        for (int i = 0; i < n - 1; i++) {
            int u = s.nextInt();
            int v = s.nextInt();
            tree[u].add(v);
            tree[v].add(u);
        }
        
        dfs(1, -1);
        
        totalWeight = n; // Initial total weight (every vertex weight is 1)
        q = s.nextInt();
        StringBuilder output = new StringBuilder();

        for (int i = 0; i < q; i++) {
            int type = s.nextInt();
            if (type == 1) {
                int x = s.nextInt();
                long w = s.nextInt();
                weights[x] += w; // Increase the weight of vertex x
                totalWeight += w; // Update the total weight
            } else {
                int y = s.nextInt();
                int u = parent[y];
                long weightSubtree = weights[y]; // Weight of the subtree containing y
                
                // Calculate the total weight of subtree rooted at y
                int sizeY = subtreeSize[y];
                long weightRootSubtree = totalWeight - weightSubtree; // Weight of the other subtree
                
                output.append(Math.abs(weightSubtree - weightRootSubtree)).append('\n');
            }
        }
        
        System.out.print(output.toString());
    }
}