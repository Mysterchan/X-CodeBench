import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for(int i = 0; i < t; i++) {
            solve(sc);
        }
    }

    static void solve(Scanner sc) {

        int n = sc.nextInt();
        double a[] = Arrays.stream(new double[n]).map(e -> sc.nextInt()).sorted().toArray();

        long sum[] = new long[n + 1];
        for(int i = 1; i <= n; i++) {
            sum[i] = sum[i - 1] + (int)a[i - 1];
        }

        int result = 0;
        for(int i = 1; i <= n; i++) {
            double key = (int)Math.ceil((double)sum[i] / i);

            if(sum[i] % i == 0) {
                key++;
            }

            int index = Arrays.binarySearch(a, 0, i, key - 0.5);

            if(index < 0) {
                index++;
                index *= -1;
            }

            result = Math.max(result, i - index);
        }

        System.out.println(result);

    }
}