import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String S = sc.next();

        char firstChar = S.charAt(0);

        char thirdChar = S.charAt(2);

        int n1 = firstChar - '0';
        int n2 = thirdChar - '0';

        System.out.println(n1 * n2);

        sc.close();
    }
}