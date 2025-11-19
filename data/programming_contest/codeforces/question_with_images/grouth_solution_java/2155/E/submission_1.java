import java.util.HashSet;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int t = input.nextInt();
		for(int test = 0; test < t; test++) {
			int n = input.nextInt();
			input.nextInt();
			int k = input.nextInt();
			HashSet<Integer> odds = new HashSet<Integer>();
			for(int i = 0; i < k; i++) {
				input.nextInt();
				int a = input.nextInt();
				if(odds.contains(a)) {
					odds.remove(a);
				}else if(a > 1){
					odds.add(a);
				}
			}
			if(n == 1) {
				if(!odds.contains(2)) {
					System.out.println("Yuyu");
				}else {
					System.out.println("Mimo");
				}
			}else {
				if(odds.isEmpty()) {
					System.out.println("Yuyu");
				}else {
					System.out.println("Mimo");
				}
			}
		}
		input.close();
	}

}
