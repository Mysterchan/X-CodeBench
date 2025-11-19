import java.io.*;
import java.util.*;

public class Main {

	public static void main (String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());

		for (int t = 1; t <= T; t++) {

			String[] in = br.readLine().split(" ");
			long n = Long.parseLong(in[0]);
			long m = Long.parseLong(in[1]);
			long a = Long.parseLong(in[2]);
			long b = Long.parseLong(in[3]);

			long turns = 0;

			while (n > 1 || m > 1) {

				long left = b-1;
				long max = left*n;
				long right =  m - b;
				if (max < right*n) max = right*n;

				long up = a-1;
				if (max < up*m) max = up*m;
				long down = n - a;
				if (max < down*m) max = down*m;

				if (max == left*n) {

					m = m - left;

				} else if (max == right*n) {

					m = b;

				} else if (max == up*m) {

					n = n - up;

				} else {

					n = a;

				}

				turns++;

				a = Math.max(1, (n+1)/2);
				b = Math.max(1, (m+1)/2);

			}

			bw.write(String.valueOf(turns));
			bw.newLine();

		}

		bw.flush();

	}

}
