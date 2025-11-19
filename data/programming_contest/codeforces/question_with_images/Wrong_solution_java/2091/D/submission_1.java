import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int k = sc.nextInt();
            int l = 0;
            int r = m;
            while(l+1 < r){
                int mid = l+(r-l)/2;
                if((m/(mid+1) * mid + m % (mid+1)) *n >= k){
                    r = mid;
                }else {
                    l = mid;
                }
            }
            System.out.println(r);
        }
    }
}
