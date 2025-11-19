import java.util.*;

public class Main {

    public static long countplus(long l, long r, long x) {
        long count = 0;
        if (l % x == 0) {
            count++;
            count += (r - l) / x;
        } else {
            long a = x - l % x;
            if (l + a <= r) {
                count++;
                count += (r - (l + a)) / x;
            }
        }
        return count;
    }


    public static long factorial(long a) {
        long x = 1000000 * 1000 + 7;
        if (a == 0) {
            return 1;
        } else {
            return (a * factorial(a - 1)) % x;
        }
    }

    public static long gcd(long a, long b) {

        if (a >= b) {
            while (a % b != 0) {
                long temp = b;
                b = a % b;
                a = temp;
            }
            return b;
        } else {
            while (b % a != 0) {
                long temp = a;
                a = b % a;
                b = temp;
            }
            return a;
        }


    }

    public static void sieve(int N) {
        boolean[] isPrime = new boolean[N + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i * i <= N; i++) {
            if (isPrime[i]) {

                for (int j = i * i; j <= N; j += i) {
                    if (isPrime[j]) {
                        isPrime[j] = false;
                    }
                }

            }
        }

        for (int i = 0; i <= N; i++) {
            if (isPrime[i]) System.out.println(i);
        }


    }


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();

        while (t-- > 0) {

            int  n = in.nextInt();

            int m = in.nextInt();

            int[] arr = new int[n];

            arr[0] = 1;
            arr[1] = 2;
            for(int i =2;i<n;i++){
                arr[i] = arr[i-1] + arr[i-2];
            }

            StringBuilder s = new StringBuilder();

            while(m-->0){
                int w  = in.nextInt();
                int l  = in.nextInt();
                int h  = in.nextInt();

                if(h>=arr[n-1]+arr[n-2]){
                    if(Math.min(w,l)>=arr[n-1]){
                        s.append('1');
                    }
                    else{
                        s.append('0');
                    }
                }
                else if(h>=arr[n-1]){
                    if(Math.max(w,l)>=arr[n-1]+arr[n-2] && Math.min(w,l)>=arr[n-2]){

                        s.append('1');

                    }
                    else{
                        s.append('0');
                    }
                }


                else{
                   s.append('0');
                }
            }

            System.out.println(s);





        }
    }
}
