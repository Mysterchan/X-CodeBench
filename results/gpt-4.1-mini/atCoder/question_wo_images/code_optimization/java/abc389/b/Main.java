import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        long fact = 1L;
        int i = 1;
        while (fact < x) {
            i++;
            fact *= i;
        }
        System.out.println(i);
    }
}