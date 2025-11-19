import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		int[] A = new int[N];
		for(int i=0; i<N; i++) A[i] = sc.nextInt();

		int len = N+1;

		for(int i=0; i<N; i++) {
			for(int j=i+1; j<Math.min(N, i+len); j++) {
				if(A[i] == A[j]) {
					len = Math.min(len, j-i + 1);
					break;
				}
			}
		}

		System.out.println(len == N + 1 ? -1 : len);
	}
}