import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        long fact = 1;
        for (int i = 1; ; i++) {
            fact *= i;
            if (fact == x) {
                System.out.println(i);
                break;
            }
            // since it's guaranteed that there is a solution, no extra checks needed
        }
        sc.close();
    }
}