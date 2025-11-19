import java.util.*;
public class Main{
    static final int mod=998244353;
    static int timeStamp=1;
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(),m=sc.nextInt();
        int[] A=new int[n+1];
        for(int i=1;i<=n;i++) A[i]=sc.nextInt();

        // Build graph: edges from A[i] to i if A[i]!=i
        List<Integer>[] graph=new List[n+1];
        for(int i=1;i<=n;i++) graph[i]=new ArrayList<>();
        for(int i=1;i<=n;i++){
            if(A[i]!=i) graph[A[i]].add(i);
        }

        // Tarjan's SCC to find strongly connected components
        int[] dfn=new int[n+1], low=new int[n+1], parent=new int[n+1];
        boolean[] inStack=new boolean[n+1];
        Stack<Integer> stack=new Stack<>();
        timeStamp=1;
        for(int i=1;i<=n;i++) parent[i]=i;
        for(int i=1;i<=n;i++){
            if(dfn[i]==0) tarjan(i, dfn, low, parent, graph, inStack, stack);
        }

        // Build condensed graph of SCCs
        // Each node is a SCC represented by its parent[i]
        // Build edges between SCCs
        List<Integer>[] condensed=new List[n+1];
        for(int i=1;i<=n;i++) condensed[i]=new ArrayList<>();
        boolean[][] added=new boolean[n+1][n+1];
        boolean[] hasParent=new boolean[n+1];
        for(int u=1;u<=n;u++){
            int pu=parent[u];
            for(int v:graph[u]){
                int pv=parent[v];
                if(pu!=pv && !added[pu][pv]){
                    condensed[pu].add(pv);
                    added[pu][pv]=true;
                    hasParent[pv]=true;
                }
            }
        }

        // DP arrays: count[scc][value] = number of sequences for SCC scc with max value <= value
        // We'll do DFS on condensed graph and compute count bottom-up
        long[][] count=new long[n+1][m+1];
        boolean[] visited=new boolean[n+1];

        long ans=1;
        for(int i=1;i<=n;i++){
            if(parent[i]==i && !hasParent[i]){
                dfs(i,m,condensed,count,visited);
                ans=ans*count[i][m]%mod;
            }
        }
        System.out.println(ans);
    }

    static void dfs(int u,int m,List<Integer>[] condensed,long[][] count,boolean[] visited){
        if(visited[u]) return;
        visited[u]=true;
        // Initialize count[u][i] = 1 for i=1..m, count[u][0]=0
        Arrays.fill(count[u],1);
        count[u][0]=0;

        for(int v:condensed[u]){
            dfs(v,m,condensed,count,visited);
            for(int i=1;i<=m;i++){
                count[u][i]=(count[u][i]*count[v][i])%mod;
            }
        }
        // Prefix sums for count[u]
        for(int i=1;i<=m;i++){
            count[u][i]=(count[u][i]+count[u][i-1])%mod;
        }
    }

    static void tarjan(int u,int[] dfn,int[] low,int[] parent,List<Integer>[] graph,boolean[] inStack,Stack<Integer> stack){
        dfn[u]=low[u]=timeStamp++;
        stack.push(u);
        inStack[u]=true;
        for(int v:graph[u]){
            if(dfn[v]==0){
                tarjan(v,dfn,low,parent,graph,inStack,stack);
                low[u]=Math.min(low[u],low[v]);
            } else if(inStack[v]){
                low[u]=Math.min(low[u],dfn[v]);
            }
        }
        if(dfn[u]==low[u]){
            int x;
            do{
                x=stack.pop();
                inStack[x]=false;
                parent[x]=u;
            }while(x!=u);
        }
    }
}