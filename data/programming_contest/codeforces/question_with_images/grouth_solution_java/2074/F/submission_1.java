import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0) {
           int l1 = sc.nextInt();
           int r1 = sc.nextInt();
           int l2 = sc.nextInt();
           int r2 = sc.nextInt();
           int res1[] = f(l1,r1);
           int res2[] = f(l2,r2);
           long ans = (long)res1[0]*(long)res2[0];
           for(int i=1;i<=20;i++)
           {
               if(res1[i]<=0||res2[i]<=0) continue;
               ans = ans - 3L*res1[i]*res2[i];
           }
           System.out.println(ans);
           }
        }
    public static int[] f(int l1,int r1) {
        int res[] = new int[21];
        res[0] = r1-l1;
        for(int i=1;i<=20;i++)
        {
            int k = 1<<i;
            res[i] = helper(r1,k) - helper(l1-1,k) - (l1>0?1:0);
        }
        return res;
    }
    public static int helper(int n, int k) {
        int cnt = n/k;
        return Math.max(0,cnt);
    }
}
