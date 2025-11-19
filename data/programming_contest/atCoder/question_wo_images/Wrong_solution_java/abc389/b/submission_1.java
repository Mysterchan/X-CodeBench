import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long X = sc.nextLong();
        long work = 1;
        for (long i = 1; i < X; i++) {
            work *= i;
            if (work == X) {
                System.out.print(i);
                return;
            }
        }
    }
}