import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        long N = 1L;
        long i = 1L;
        while (true) {
            N = N * i;
            if (N == x) {
                System.out.println(i);
                break;
            }
            i++;
        }
    }
}