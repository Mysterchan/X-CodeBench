import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        long factorial = 1L;
        int i = 1;

        while (factorial < x) {
            i++;
            factorial *= i;
        }

        System.out.println(i);
    }
}