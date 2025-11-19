import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int[] P = new int[N];
		int[] Q = new int[N];

		for(int i = 0;i < N;i++) {
			P[i] = scanner.nextInt() - 1;
		}

		for(int i = 0;i < N;i++) {
			Q[i] = scanner.nextInt() - 1;
		}

		int[] S = new int[N];

		for(int i = 0;i < N;i++) {
			int myZekken = Q[i];
			int targetPerson = P[i];
			int targetZekken = Q[targetPerson];

			S[myZekken] = targetZekken;
		}

		for(int i : S) {
			System.out.print(i + 1 + " ");
		}
	}

}