import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int z = 0; z < t; z++) {
			String[] sa = br.readLine().split(" ");
			int n = Integer.parseInt(sa[0]);
			int m = Integer.parseInt(sa[1]);
			sa = br.readLine().split(" ");
			int[] a = new int[n];
			for (int i = 0; i < n; i++) {
				a[i] = Integer.parseInt(sa[i]);
			}
			sa = br.readLine().split(" ");
			int[] b = new int[n];
			for (int i = 0; i < n; i++) {
				b[i] = Integer.parseInt(sa[i]);
			}
			Arrays.sort(a);
			reverse(a);
			Arrays.sort(b);

			int ans = m;
			int lo = 0, hi = m - 1;
			
			while (lo <= hi) {
				int mid = lo + (hi - lo) / 2;
				if (canAchieve(a, b, n, m, mid)) {
					ans = mid;
					hi = mid - 1;
				} else {
					lo = mid + 1;
				}
			}
			sb.append(ans).append('\n');
		}
		br.close();
		System.out.print(sb.toString());
	}

	static boolean canAchieve(int[] a, int[] b, int n, int m, int target) {
		for (int s = 0; s < n; s++) {
			boolean valid = true;
			for (int i = 0; i < n; i++) {
				int si = s + i;
				if (si >= n) {
					si -= n;
				}
				int val = a[si] + b[i];
				if (val >= m) {
					val -= m;
				}
				if (val > target) {
					valid = false;
					break;
				}
			}
			if (valid) {
				return true;
			}
		}
		return false;
	}

	static void reverse(int[] a) {
		for (int i = 0; i < a.length / 2; i++) {
			int tmp = a[i];
			a[i] = a[a.length - 1 - i];
			a[a.length - 1 - i] = tmp;
		}
	}
}