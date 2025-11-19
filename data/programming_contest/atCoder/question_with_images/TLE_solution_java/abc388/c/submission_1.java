import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int[] A = new int[N];

		for(int i = 0;i < N;i++) {
			A[i] = scanner.nextInt();
		}
		int count = 0;
		for(int i = 0;i < N;i++) {
			for(int j = i + 1;j < N;j++) {
				if(A[j] / A[i] >= 2) {
					count += N - j;
					break;
				}
			}
		}
		System.out.println(count);

	}

}