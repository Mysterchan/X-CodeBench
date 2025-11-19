import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            long x = sc.nextLong();
            long y = sc.nextLong();

            if (y > x) {
                System.out.println(2);
            } else if (x > y + 1) {
                System.out.println(3);
            } else {
                System.out.println(-1);
            }
        }
        sc.close();
    }
}
