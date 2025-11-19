import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String S = sc.next();
            
            if (S.length() % 2 == 1) {
                System.out.println("No");
                return;
            }

            Stack<Character> stack = new Stack<>();
            for (char c : S.toCharArray()) {
                if (c == '(' || c == '[' || c == '<') {
                    stack.push(c);
                } else {
                    if (stack.isEmpty() || !isMatchingPair(stack.pop(), c)) {
                        System.out.println("No");
                        return;
                    }
                }
            }

            System.out.println(stack.isEmpty() ? "Yes" : "No");
        }
    }

    private static boolean isMatchingPair(char opening, char closing) {
        return (opening == '(' && closing == ')') ||
               (opening == '[' && closing == ']') ||
               (opening == '<' && closing == '>');
    }
}