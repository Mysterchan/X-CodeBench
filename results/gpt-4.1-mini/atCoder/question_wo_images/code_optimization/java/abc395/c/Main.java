import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] A = new int[N];
		for (int i = 0; i < N; i++) A[i] = sc.nextInt();

		int len = N + 1;
		int[] lastPos = new int[1_000_001]; // since A_i ≤ 10^6
		for (int i = 0; i <= 1_000_000; i++) lastPos[i] = -1;

		for (int i = 0; i < N; i++) {
			int val = A[i];
			if (lastPos[val] != -1) {
				int dist = i - lastPos[val] + 1;
				if (dist < len) len = dist;
			}
			lastPos[val] = i;
		}

		System.out.println(len == N + 1 ? -1 : len);
	}
}