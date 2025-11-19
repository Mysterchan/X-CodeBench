import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        sc.close();

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);

            if (c == '2') {
                result.append(c);
            }
        }

        System.out.println(result.toString());
    }
}