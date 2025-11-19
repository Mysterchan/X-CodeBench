import java.util.Scanner;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc;

		tc = sc.nextInt();
		while(tc > 0) {
			fnc(sc);
			tc = tc - 1;
		}
	}

	public static void fnc(Scanner sc) {

		int n = sc.nextInt();
		long[] x = new long[n];
		long[] y = new long[n];

		long[] X = new long[n];
		long[] Y = new long[n];

		for (int i = 0; i < n; i++) {
			x[i] = sc.nextLong();
			y[i] = sc.nextLong();
			X[i] = x[i];
			Y[i] = y[i];
		}

		Arrays.sort(X);
		Arrays.sort(Y);

		long ans = 1000000000000000000L;
		for (int i = 0; i < n; i++) {
			long xle, xri;
			long yle, yri;

			if (X[0] == x[i] && n != 1) {
				xle = X[1];
			}
			else {
				xle = X[0];
			}

			if (X[n - 1] == x[i] && n != 1) {
				xri = X[n - 2];
			}
			else {
				xri = X[n - 1];
			}

			if (Y[0] == y[i] && n != 1) {
				yle = Y[1];
			}
			else {
				yle = Y[0];
			}

			if (Y[n - 1] == y[i] && n != 1) {
				yri = Y[n - 2];
			}
			else {
				yri = Y[n - 1];
			}

			long row = yri - yle + 1;
			long col = xri - xle + 1;

			long tm = row * col;
			if (tm == n - 1) {
				tm += Math.min(row, col);
			}

			ans = Math.min(ans, tm);
		}

		System.out.println(ans);
	}

}
