import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static kattio sc = new kattio();
	static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

	public static void main(String[] args) {
		int t = sc.nextint();
		while (t-- > 0) {
			solve();
		}
		out.close();
	}

	static void solve() {
		int n = sc.nextint();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextint();
		}
		Arrays.sort(arr);
		
		if (arr[0] == arr[n - 1]) {
			out.println(0);
			return;
		}
		
		long[] prefix = new long[n + 1];
		for (int i = 0; i < n; i++) {
			prefix[i + 1] = prefix[i] + arr[i];
		}
		
		int ans = 0;
		for (int i = 1; i < n; i++) {
			int l = i, r = n - 1;
			while (l < r) {
				int mid = (l + r + 1) / 2;
				long sumRight = prefix[mid + 1] - prefix[i];
				int cntRight = mid - i + 1;
				
				boolean valid = false;
				for (int j = 0; j < i; j++) {
					long totalSum = sumRight + prefix[j + 1];
					int totalCnt = cntRight + j + 1;
					if ((long) totalCnt * arr[i] > totalSum) {
						valid = true;
						break;
					}
				}
				
				if (valid) {
					l = mid;
				} else {
					r = mid - 1;
				}
			}
			ans = Math.max(ans, r - i + 1);
		}
		
		out.println(ans);
	}
}

class kattio extends PrintWriter {
	BufferedReader r;
	StringTokenizer st;

	public kattio() {
		this(System.in, System.out);
	}

	public kattio(InputStream i, OutputStream o) {
		super(o);
		r = new BufferedReader(new InputStreamReader(i));
	}

	public String next() {
		try {
			while (st == null || !st.hasMoreTokens()) {
				st = new StringTokenizer(r.readLine());
			}
			return st.nextToken();
		} catch (Exception e) {
			return null;
		}
	}

	public int nextint() {
		return Integer.parseInt(next());
	}
}