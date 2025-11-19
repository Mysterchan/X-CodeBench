import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        StringBuilder output = new StringBuilder();
        
        while (T-- > 0) {
            int n = sc.nextInt(), k = sc.nextInt();
            List<List<Integer>> tree = new ArrayList<>(n + 1);
            for (int i = 0; i <= n; i++) {
                tree.add(new ArrayList<>());
            }

            // Read parents and build the tree
            for (int i = 2; i <= n; i++) {
                int parent = sc.nextInt();
                tree.get(parent).add(i);
            }

            // Array to store the minimum distance to leaves
            int[] minLeaves = new int[n + 1];
            Arrays.fill(minLeaves, Integer.MAX_VALUE);
            
            // Perform DFS to calculate the minimum depth to leaves
            int maxDepth = dfs(tree, 1, minLeaves);
            
            // Calculate the maximum number of common prefixes possible
            int beauty = 0;
            int zerosAvailable = k;
            int onesAvailable = n - k;
            for (int depth = 0; depth < maxDepth; depth++) {
                if (zerosAvailable > 0 && onesAvailable > 0) {
                    // If we can use both zeros and ones, we can extend the common subsequence
                    beauty++;
                    zerosAvailable--;
                    onesAvailable--;
                } else if (zerosAvailable > 0) {
                    // If we only have zeros left
                    if (minLeaves[depth] <= zerosAvailable) {
                        beauty++;
                        zerosAvailable -= minLeaves[depth];
                    }
                    break;
                } else if (onesAvailable > 0) {
                    // If we only have ones left
                    if (minLeaves[depth] <= onesAvailable) {
                        beauty++;
                        onesAvailable -= minLeaves[depth];
                    }
                    break;
                } else {
                    break;
                }
            }

            output.append(beauty).append("\n");
        }
        System.out.print(output);
    }
    
    private static int dfs(List<List<Integer>> tree, int node, int[] minLeaves) {
        if (tree.get(node).isEmpty()) {
            minLeaves[0]++; // A leaf node found
            return 1; // Depth at this level
        }
        
        int depth = 0;
        for (int child : tree.get(node)) {
            depth = Math.max(depth, dfs(tree, child));
        }
        
        return depth + 1; // Return the depth of the node
    }
}