import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	private static StringBuffer ret = new StringBuffer();
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static StringTokenizer st;
	static int N, X, U[], D[], min;
	static long sum;

	public static void main(String[] args) throws Exception {

		problem();

		System.out.print(ret.toString());
	}

	@Override
	public void finalize() throws Exception {
		br.close();
	}

	private static void problem() throws Exception {
		setInput();
		solve();
	}

	private static void setInput() throws Exception {
		st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		X = Integer.parseInt(st.nextToken());
		sum = 0;
		min = Integer.MAX_VALUE;
		U = new int[N];
		D = new int[N];
		String str[];
		for (int i = 0; i < N; i++) {
			str = br.readLine().split(" ");
			U[i] = Integer.parseInt(str[0]);
			D[i] = Integer.parseInt(str[1]);
			sum += U[i] + D[i];
			min = Math.min(min, U[i] + D[i]);
		}
	}

	private static void solve() throws Exception {
		int l = 0, r = min + 1, m;
		while (l < r) {
			m = (l + r) / 2;
			if (check(m) == false) {
				r = m;
			} else
				l = m + 1;
		}
		ret.append(sum - ((long) (r - 1) * N));
	}

	private static boolean check(int h) {
		int upper = U[0];
		int lower = Math.max(h - D[0], 0);

		for (int i = 1; i < N; i++) {
			upper = Math.min(U[i], upper + X);
			lower = Math.max(h - D[i], lower - X);
			lower = Math.max(lower, 0);
			if (lower > upper)
				return false;
		}
		return true;
	}
}