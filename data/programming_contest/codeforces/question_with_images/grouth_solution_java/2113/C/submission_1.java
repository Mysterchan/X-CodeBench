import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
         int n=sc.nextInt();
         int m=sc.nextInt();
         int k=sc.nextInt();
         String[] arr=new String[n];
         int prefix[][]=new int[n+1][m+1];
         int cnt=0;
         ArrayList<int[]> l=new ArrayList<>();
         for(int i=0;i<n;i++){
            arr[i]=sc.next();
            for(int j=0;j<m;j++){
               prefix[i+1][j+1]=prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j];
               if(arr[i].charAt(j)=='g') {prefix[i+1][j+1]++;cnt++;}
               if(arr[i].charAt(j)=='.') l.add(new int[]{i,j});
            }
         }
         int maxans=0;
         for(int a[]:l){
            int str=Math.max(0,a[0]-(k-1));
            int stc=Math.max(0,a[1]-(k-1));
            int endr=Math.min(n-1,a[0]+(k-1));
            int endc=Math.min(m-1,a[1]+k-1);
            int c = prefix[endr+1][endc+1] - prefix[str][endc+1] - prefix[endr+1][stc] + prefix[str][stc];

            maxans=Math.max(maxans,cnt-c);
         }
         System.out.println(maxans);
        }
        sc.close();
    }
}
