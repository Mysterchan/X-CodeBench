import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            char[] S = sc.next().toCharArray();
            if (S.length % 2 == 1) {
                System.out.println("No");
                return;
            }

            // Use a stack to check for valid colorful bracket sequence
            // Push opening brackets, pop when matching closing bracket found
            int top = -1;
            char[] stack = new char[S.length];

            for (char c : S) {
                if (c == '(' || c == '[' || c == '<') {
                    stack[++top] = c;
                } else {
                    if (top < 0) {
                        System.out.println("No");
                        return;
                    }
                    char open = stack[top];
                    if ((open == '(' && c == ')') ||
                        (open == '[' && c == ']') ||
                        (open == '<' && c == '>')) {
                        top--;
                    } else {
                        System.out.println("No");
                        return;
                    }
                }
            }

            System.out.println(top == -1 ? "Yes" : "No");
        }
    }
}