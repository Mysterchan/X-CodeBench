import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        sc.close();

        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);

            if (c == '(' || c == '[' || c == '<') {
                stack.push(c);
            } else {

                if (stack.isEmpty()) {

                    System.out.println("No");
                    return;
                }

                char opener = stack.pop();

                if (c == ')' && opener != '(') {
                    System.out.println("No");
                    return;
                }
                if (c == ']' && opener != '[') {
                    System.out.println("No");
                    return;
                }
                if (c == '>' && opener != '<') {
                    System.out.println("No");
                    return;
                }

            }
        }

        if (stack.isEmpty()) {
            System.out.println("Yes");
        } else {

            System.out.println("No");
        }
    }
}