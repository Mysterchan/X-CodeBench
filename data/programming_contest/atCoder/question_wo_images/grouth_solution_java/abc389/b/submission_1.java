import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long X = sc.nextLong();

        long N = 1;

        while (X > 1) {
            N++;
            X = X / N;
        }

        System.out.println(N);

        sc.close();
    }
}