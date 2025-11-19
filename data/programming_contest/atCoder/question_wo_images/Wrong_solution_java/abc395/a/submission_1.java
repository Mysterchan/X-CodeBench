import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int pre = 0;
        for (int i = 0; i < n; i++) {

            int temp = sc.nextInt();
            if (temp < pre) {
                System.out.println("No");
                return;
            }
            pre = temp;
        }
        System.out.println("Yes");
    }
}