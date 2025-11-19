import java.util.*;
import java.io.*;
public class Main{
    public static int n,sz[],ds[],idx,q,fa[];
    public static long h[];
    public static ArrayList<Integer>sk[];
    public static class pair{
        int fi,se;
        pair(int fi,int se){this.fi=fi;this.se=se;}
    }
    public static void dfs(int f,int cur){
        idx++;
        sz[cur]=1;
        ds[cur]=idx;
        for(int x:sk[cur]){
            if(x==f) continue;
            fa[x]=cur;
            dfs(cur,x);
            sz[cur]+=sz[x];
        }
    }
    public static int lowbit(int x){
         return (x&-x);
    }
    public static void in(int x,int v){
        for(int i=x;i<=n;i+=lowbit(i)) h[i]+=v;
    }
    public static long Q(int x){
        long res=0;
        for(int i=x;i>0;i-=lowbit(i)) res+=h[i];
        return res;
    }
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        n=s.nextInt();
        ds=new int [n+10];
        h=new long [n+10];
        fa=new int [n+10];
        sk=new ArrayList [n+10];
        sz=new int [n+10];
        pair dts[]=new pair [n+10];
        for(int i=1;i<=n;i++){
            sk[i]=new ArrayList<>();
            in(i,1);
        }
        for(int i=1;i<n;i++){
            int u=s.nextInt(),v=s.nextInt();
            dts[i]=new pair(u,v);
            sk[u].add(v);
            sk[v].add(u);
        }
        dfs(0,1);

        q=s.nextInt();
        long sum=n;

        while(q-->0){
            int ty=s.nextInt();
            if(ty==1){
                int x=s.nextInt(),w=s.nextInt();
                in(ds[x],w);
                sum+=w;
            }
            else{
                int y=s.nextInt();
                int u=dts[y].fi,v=dts[y].se;
                long tem=0;
                if(fa[v]==u) tem=Q(ds[v]+sz[v]-1)-Q(ds[v]-1);
                else{

                    tem=Q(ds[u]+sz[u]-1)-Q(ds[u]-1);
                }

                System.out.println(Math.abs(sum-2*tem));
            }
        }
    }
}