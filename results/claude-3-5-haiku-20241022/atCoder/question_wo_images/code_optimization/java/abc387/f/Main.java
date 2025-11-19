import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 998244353;
    static int timeStamp = 1;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] first = br.readLine().split(" ");
        int n = Integer.parseInt(first[0]);
        int m = Integer.parseInt(first[1]);
        
        String[] second = br.readLine().split(" ");
        
        int[] dfn = new int[n + 1];
        int[] low = new int[n + 1];
        int[] parent = new int[n + 1];
        long[][] count = new long[n + 1][m + 1];
        
        ArrayList<Integer>[] path = new ArrayList[n + 1];
        boolean[] inStack = new boolean[n + 1];
        
        for (int i = 1; i <= n; i++) {
            path[i] = new ArrayList<>();
            parent[i] = i;
        }
        
        for (int i = 1; i <= n; i++) {
            int a = Integer.parseInt(second[i - 1]);
            if (a != i) {
                path[a].add(i);
            }
        }
        
        int[] stack = new int[n + 1];
        int stackTop = 0;
        
        for (int i = 1; i <= n; i++) {
            if (dfn[i] == 0) {
                tarjan(i, dfn, low, parent, path, inStack, stack, stackTop);
            }
        }
        
        boolean[] isSon = new boolean[n + 1];
        ArrayList<Integer>[] newPath = buildDAG(n, path, parent, isSon);
        
        long ans = 1;
        for (int i = 1; i <= n; i++) {
            if (i == parent[i]) {
                computeCount(i, m, newPath, count);
                if (!isSon[i]) {
                    ans = ans * count[i][m] % MOD;
                }
            }
        }
        
        System.out.println(ans);
    }
    
    static ArrayList<Integer>[] buildDAG(int n, ArrayList<Integer>[] path, int[] parent, boolean[] isSon) {
        ArrayList<Integer>[] ans = new ArrayList[n + 1];
        boolean[][] added = new boolean[n + 1][n + 1];
        
        for (int i = 1; i <= n; i++) {
            ans[i] = new ArrayList<>();
        }
        
        for (int i = 1; i <= n; i++) {
            int pi = parent[i];
            for (int a : path[i]) {
                int pa = parent[a];
                if (pa != pi && !added[pa][pi]) {
                    ans[pi].add(pa);
                    added[pa][pi] = true;
                    isSon[pa] = true;
                }
            }
        }
        
        return ans;
    }
    
    static void computeCount(int k, int m, ArrayList<Integer>[] path, long[][] count) {
        Arrays.fill(count[k], 1, m + 1, 1);
        count[k][0] = 0;
        
        for (int a : path[k]) {
            computeCount(a, m, path, count);
            for (int i = 1; i <= m; i++) {
                count[k][i] = count[k][i] * count[a][i] % MOD;
            }
        }
        
        for (int i = 1; i <= m; i++) {
            count[k][i] = (count[k][i] + count[k][i - 1]) % MOD;
        }
    }
    
    static int tarjan(int k, int[] dfn, int[] low, int[] parent, ArrayList<Integer>[] path, 
                      boolean[] inStack, int[] stack, int stackTop) {
        dfn[k] = low[k] = timeStamp++;
        inStack[k] = true;
        stack[stackTop++] = k;
        
        for (int a : path[k]) {
            if (dfn[a] == 0) {
                stackTop = tarjan(a, dfn, low, parent, path, inStack, stack, stackTop);
                low[k] = Math.min(low[k], low[a]);
            } else if (inStack[a]) {
                low[k] = Math.min(low[k], dfn[a]);
            }
        }
        
        if (dfn[k] == low[k]) {
            while (stackTop > 0) {
                int a = stack[--stackTop];
                parent[a] = k;
                inStack[a] = false;
                if (a == k) break;
            }
        }
        
        return stackTop;
    }
}