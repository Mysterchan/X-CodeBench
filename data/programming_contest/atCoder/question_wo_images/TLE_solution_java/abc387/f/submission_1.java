import java.util.*;
public class Main{
    static int mod=998244353,timeStamp=1;
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(),m=sc.nextInt(),dfn[]=new int[n+5],low[]=new int[n+5],parent[]=new int[n+5];
        long ans=1,count[][]=new long[n+5][m+5];
        Stack<Integer> stack=new Stack<>();
        List<Integer> path[]=new List[n+5];
        boolean has[]=new boolean[n+5];
        for(int i=1;i<=n;i++){
            path[i]=new ArrayList<>();
            parent[i]=i;
        }
        for(int i=1;i<=n;i++){
            int a=sc.nextInt();
            if(a!=i){
                path[a].add(i);
            }
        }
        for(int i=1;i<=n;i++){
            if(dfn[i]==0){
                tarjan(i,dfn,low,parent,path,has,stack);
            }
        }
        Arrays.fill(has,false);
        path=find(n,path,parent,has);
        for(int i=1;i<=n;i++){
            if(i==parent[i]){
                find(i,m,path,count);
                if(!has[i]){
                    ans=ans*count[i][m]%mod;
                }
            }
        }
        System.out.println(ans);
    }
    static List<Integer>[] find(int n,List<Integer> path[],int parent[],boolean isSon[]){
        List<Integer> ans[]=new List[n+5];
        boolean has[][]=new boolean[n+5][n+5];
        for(int i=1;i<=n;i++){
            ans[i]=new ArrayList<>();
        }
        for(int i=1;i<=n;i++){
            for(int a:path[i]){
                if(parent[a]!=parent[i]&&!has[parent[a]][parent[i]]){
                    ans[parent[i]].add(parent[a]);
                    has[parent[i]][parent[a]]=isSon[parent[a]]=true;
                }
            }
        }
        return ans;
    }
    static void find(int k,int m,List<Integer> path[],long count[][]){
        Arrays.fill(count[k],1);
        count[k][0]=0;
        for(int a:path[k]){
            find(a,m,path,count);
            for(int i=1;i<=m;i++){
                count[k][i]=count[k][i]*count[a][i]%mod;
            }
        }
        for(int i=1;i<=m;i++){
            count[k][i]=(count[k][i]+count[k][i-1])%mod;
        }
    }
    static void tarjan(int k,int dfn[],int low[],int parent[],List<Integer> path[],boolean has[],Stack<Integer> stack){
        dfn[k]=low[k]=timeStamp++;
        has[k]=true;
        stack.push(k);
        for(int a:path[k]){
            if(dfn[a]==0){
                tarjan(a,dfn,low,parent,path,has,stack);
                low[k]=Math.min(low[k],low[a]);
            }
            else if(has[a]){
                low[k]=Math.min(low[k],dfn[a]);
            }
        }
        if(dfn[k]==low[k]){
            while(!stack.isEmpty()){
                int a=stack.pop();
                parent[a]=k;
                has[a]=false;
                if(a==k){
                    break;
                }
            }
        }
    }
}