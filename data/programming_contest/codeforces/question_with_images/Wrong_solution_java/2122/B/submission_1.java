import java.util.*;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            int n = sc.nextInt();
            long ans = 0;
            for(int i=0;i<n;i++){
                int arr[] = new int[4];
                arr[0] = sc.nextInt();
                arr[1] = sc.nextInt();
                arr[2] = sc.nextInt();
                arr[3] = sc.nextInt();
                if(arr[0] > arr[2]){
                    arr[0] -= arr[2];
                    ans += arr[0];
                }
                if(arr[1] > arr[3]){
                    ans += arr[1] - arr[3] + arr[0];
                }
            }
            System.out.println(ans);
        }
    }
}
