import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int[] A = new int[N];

		for (int i = 0; i < N; i++) {
			A[i] = scanner.nextInt();
		}

		long count = 0;
		int j = 0;
		for (int i = 0; i < N; i++) {
			while (j < N && A[j] < 2L * A[i]) {
				j++;
			}
			if (j < N) {
				count += N - j;
			}
		}

		System.out.println(count);
	}
}