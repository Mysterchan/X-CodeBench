import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)){
			char S[] = sc.next().toCharArray();
			int n = S.length;
			
			if(n % 2 == 1) {
				System.out.println("No");
				return;
			}

			char[] stack = new char[n];
			int top = -1;
			
			for(int i = 0; i < n; i++) {
				char c = S[i];
				
				if(top >= 0 && isPairBracket(stack[top], c)) {
					top--;
				} else {
					stack[++top] = c;
				}
			}

			if(top == -1) {
				System.out.println("Yes");
			} else {
				System.out.println("No");
			}
		}
	}

	private static boolean isPairBracket(char a, char b) {
		return (a == '(' && b == ')') || (a == '[' && b == ']') || (a == '<' && b == '>');
	}
}