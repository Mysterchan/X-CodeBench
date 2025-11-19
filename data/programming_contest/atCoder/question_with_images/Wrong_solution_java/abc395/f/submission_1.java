import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int nextInt() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(br.readLine());
        }
        return Integer.parseInt(st.nextToken());
    }
    static int n,x;
    static int N=(int)2e5+5;
    static int u[]=new int[N];
    static int d[]=new int[N];
    static boolean check(long x){
        long l=Math.max(0,x-d[1]),r=Math.min(u[1],x);
        if(l>r) return false;
        for (int i=2;i<=n;i++){
            long cntl=Math.max(0,x-d[i]);
            long cntr= Math.min(u[i],x);
            cntl= Math.max(cntl,l-x);
            cntr= Math.min(cntr,r+x);
            if(cntl>cntr) return false;
            l=cntl;
            r=cntr;
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        n=nextInt();
        x=nextInt();
        long sum=0;
        for (int i=1;i<=n;i++){
            u[i]=nextInt();
            d[i]=nextInt();
            sum+=u[i]+d[i];
        }
        long l=0,r=(int)1e9;
        long ans=0;
        while(l<=r){
            long mid=l+r>>1;
            if(check(mid)){
                ans=mid;
                l=mid+1;
            }else{
                r=mid-1;
            }
        }
        System.out.println(sum-n*ans);
    }
}