import java.util.*;

public class Main {
    static final int N = 400000;
    static int n, q, totalComponents;
    static int[] parent = new int[N + 1], size = new int[N + 1];
    static Set<Integer>[][] op = new HashSet[2][N + 1];

    static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (size[rootX] < size[rootY]) {
                parent[rootY] = rootX;
                size[rootX] += size[rootY];
            } else {
                parent[rootX] = rootY;
                size[rootY] += size[rootX];
            }
            totalComponents--;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        q = sc.nextInt();
        totalComponents = n;

        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
            op[0][i] = new HashSet<>();
            op[1][i] = new HashSet<>();
        }

        for (int i = 0; i < q; i++) {
            String type = sc.next();
            int x = sc.nextInt(), y = sc.nextInt();
            if (x > y) { 
                int temp = x; 
                x = y; 
                y = temp; 
            }
            int graphIndex = type.equals("B") ? 1 : 0;

            if (op[graphIndex][x].contains(y)) {
                op[graphIndex][x].remove(y);
                op[graphIndex][y].remove(x);
                totalComponents++;
                // Should add back to union-find structure
            } else {
                op[graphIndex][x].add(y);
                op[graphIndex][y].add(x);
                union(x, y);
            }

            // Calculate number of edges to add
            int edgesToAdd = (totalComponents - (1 + (op[1][0].size() > 0 ? 1 : 0))) +
                              ((graphIndex == 0) ? (totalComponents - 1) : 0);
            System.out.println(edgesToAdd);
        }
    }
}