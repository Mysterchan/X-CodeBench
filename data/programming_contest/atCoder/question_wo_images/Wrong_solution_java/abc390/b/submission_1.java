import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int[] A = new int[N];

		for(int i = 0;i < N;i++) {
			A[i] = scanner.nextInt();
		}

		double count = (double)A[1] / (double)A[0];

		for(int i = 0;i < N - 1;i++) {
			if(count != (double)A[i + 1] / (double)A[i]) {
				System.out.println("No");
				return;
			}
		}
		System.out.println("Yes");

	}

}