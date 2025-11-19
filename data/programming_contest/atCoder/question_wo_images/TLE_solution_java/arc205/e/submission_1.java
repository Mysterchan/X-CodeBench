import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int N=sc.nextInt();
        long mod=998244353;
        long[] arr=new long[N];
        for(int i=0;i<N;i++){
            arr[i]=sc.nextLong();
        }
        for(int k=0;k<N;k++){
            long prod=1;
            for(int i=0;i<=k;i++){
                if((arr[i]|arr[k])==arr[k]){
                    prod=(prod*arr[i])%mod;
                }
            }
            System.out.println(prod);
        }
    }
}