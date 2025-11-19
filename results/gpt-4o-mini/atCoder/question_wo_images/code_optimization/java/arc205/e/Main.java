import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long mod = 998244353;
        long[] arr = new long[N];
        long[] result = new long[N];
        
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextLong();
        }

        long prod = 1;
        long currentOR = 0;

        for (int k = 0; k < N; k++) {
            currentOR |= arr[k];
            prod = 1; // Reset product for each k

            for (int i = 0; i <= k; i++) {
                if ((arr[i] | arr[k]) == arr[k]) {
                    prod = (prod * arr[i]) % mod;
                }
            }

            result[k] = prod;
        }

        for (long res : result) {
            System.out.println(res);
        }
    }
}