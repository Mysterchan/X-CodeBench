import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        long m=998244353;
        while(t-->0){
            int n=sc.nextInt();
            int p[]=new int[n+1];
            int l[]=new int[n+1];
            l[1]=0;
            int ml=0;
            for(int i=2;i<=n;i++){
                p[i]=sc.nextInt();
                l[i]=l[p[i]]+1;
                ml=Math.max(ml, l[i]);
            }
            long sl[]=new long[ml+1];
            for(int i=1;i<=n;i++){
                sl[l[i]]++;
            }
            long pr=1,r=1;
            for(int i=1;i<=ml;i++){
                if(i>=2){
                    pr=(pr*(sl[i-1]-1))%m;
                }
                r=(r+(pr*sl[i]))%m;
            }
            System.out.println(r);
        }
    }

}
