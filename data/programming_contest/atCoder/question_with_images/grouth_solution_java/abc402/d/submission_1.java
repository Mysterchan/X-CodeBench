import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        long[] count = new long[N];

        for (int i = 0; i < M; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            count[(A + B) % N]++;
        }

        long ans = (long) M * (M - 1) / 2;
        for (long c : count) ans -= c * (c - 1) / 2;

        System.out.println(ans);
    }
}