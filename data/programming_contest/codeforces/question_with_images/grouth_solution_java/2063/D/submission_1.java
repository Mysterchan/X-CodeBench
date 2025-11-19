import java.util.*;
import java.io.*;
public class Main{
    public static BufferedReader rd=new BufferedReader(new InputStreamReader(System.in));
    public static BufferedWriter wd=new BufferedWriter(new OutputStreamWriter(System.out));
    public static void solve()throws Exception{
        String dr[]=rd.readLine().split(" ");
        int n=Integer.parseInt(dr[0]),m=Integer.parseInt(dr[1]);
        long p[]=new long [n+10],h[]=new long [n+10];
        long p2[]=new long [m+10],h2[]=new long [m+10];
        long g[]=new long [n+10],g2[]=new long [m+10];
        long a[]=new long [n+10],b[]=new long [m+10];
        dr=rd.readLine().split(" ");
        for(int i=0;i<n;i++) a[i+1]=Long.parseLong(dr[i]);
        dr=rd.readLine().split(" ");
        for(int i=0;i<m;i++) b[i+1]=Long.parseLong(dr[i]);
        Arrays.sort(a,1,n+1);Arrays.sort(b,1,m+1);
        for(int i=1;i<=n;i++) p[i]=p[i-1]+a[i];
        for(int i=n;i>=1;i--) h[i]=h[i+1]+a[i];
        for(int i=1;i<=m;i++) p2[i]=p2[i-1]+b[i];
        for(int i=m;i>=1;i--) h2[i]=h2[i+1]+b[i];
        for(int i=1;i<=n;i++) g[i]=h[n-i+1]-p[i];
        for(int i=1;i<=m;i++) g2[i]=h2[m-i+1]-p2[i];
        long as[]=new long [n+m+10];
        int tot=0;
        for(int k=1;k<=Math.min(n,m);k++){
            int l=Math.max(0,2*k-m),r=Math.min(Math.min(k,m),n-k);
            if(l > r) break;
            while(l < r){
                int mid = l + r >> 1;
                int lmid = mid, rmid = mid + 1;
                if(g[lmid] + g2[k-lmid] > g[rmid] + g2[k-rmid]) r = rmid-1;
                else if(g[lmid] + g2[k-lmid] < g[rmid] + g2[k-rmid]) l = lmid+1;
                else r = rmid - 1;
            }
            as[++tot]=g[l]+g2[k-l];
        }
        wd.write(tot+"\n");
        for(int i=1;i<=tot;i++) wd.write(as[i]+" ");
        wd.write("\n");
    }
    public static void main(String args[])throws Exception{
        int t=Integer.parseInt(rd.readLine());
        while(t-->0){
            solve();
            wd.flush();
        }
    }
}
