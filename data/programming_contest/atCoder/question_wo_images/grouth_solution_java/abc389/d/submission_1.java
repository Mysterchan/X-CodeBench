import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();

        long sum = 0;
        for (int i = 1; i < r; i++) {
            double y = i + 0.5;
            double x = Math.sqrt(Math.pow(r, 2) - Math.pow(y, 2));
            sum += (int) (x + 0.5);
        }
        System.out.println(sum * 4 + 1);
    }
}