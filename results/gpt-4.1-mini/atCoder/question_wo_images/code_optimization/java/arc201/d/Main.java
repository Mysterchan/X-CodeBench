import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		while (t-- > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());

			int[] a = new int[n];
			int[] b = new int[n];

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++) {
				a[i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++) {
				b[i] = Integer.parseInt(st.nextToken());
			}

			Arrays.sort(a);
			Arrays.sort(b);

			// For each b[i], we want to find the smallest a[j] >= (m - b[i]) mod m
			// to minimize (a[j] + b[i]) mod m.
			// If no such a[j], take the smallest a[0].
			// Use binary search for each b[i].

			int ans = 0;
			for (int i = 0; i < n; i++) {
				int target = m - b[i];
				if (target == m) target = 0; // since b[i] < m, m - b[i] can be m only if b[i] == 0

				int idx = Arrays.binarySearch(a, target);
				if (idx < 0) {
					idx = -idx - 1;
					if (idx == n) idx = 0;
				}
				int val = a[idx] + b[i];
				if (val >= m) val -= m;
				if (val > ans) ans = val;
			}
			sb.append(ans).append('\n');
		}
		br.close();
		System.out.print(sb.toString());
	}
}