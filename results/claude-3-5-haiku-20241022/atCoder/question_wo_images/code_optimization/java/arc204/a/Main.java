import java.io.IOException;
import java.io.InputStream;
import java.util.NoSuchElementException;

public class Main {
	public static void main(String[] args) {
		Main o = new Main();
		o.solve();
	}

	static final int MOD = 998244353;
	
	public void solve() {
		FastScanner sc = new FastScanner(System.in);
		int N = sc.nextInt();
		int L = sc.nextInt();
		int R = sc.nextInt();
		int[] A = sc.nextIntArray(N);
		int[] B = sc.nextIntArray(N);
		
		int[] cumA = new int[N + 1];
		int[] cumB = new int[N + 1];
		for (int i = 0; i < N; i++) {
			cumA[i + 1] = cumA[i] + A[i];
			cumB[i + 1] = cumB[i] + B[i];
		}
		
		int tot = cumB[N] - cumA[N];
		
		// Use 2D arrays instead of 3D - only need current and previous states
		int[][] dp0 = new int[N + 1][N + 1];
		int[][] dp1 = new int[N + 1][N + 1];
		
		int sum = tot;
		if (R < sum) {
			dp0[0][0] = 0;
			dp1[0][0] = 0;
		} else if (L <= sum) {
			dp0[0][0] = 0;
			dp1[0][0] = 1;
		} else {
			dp0[0][0] = 1;
			dp1[0][0] = 0;
		}
		
		for (int bi = 0; bi <= N; bi++) {
			for (int ai = bi; ai <= N; ai++) {
				if (ai == 0 && bi == 0) continue;
				
				sum = cumB[bi] - cumA[ai];
				int threshold = tot - sum;
				
				int val0 = 0, val1 = 0;
				
				if (threshold < R) {
					if (threshold >= L) {
						// L <= threshold < R
						if (ai > bi) {
							val1 = dp0[ai - 1][bi];
							if (dp1[ai - 1][bi] > 0) {
								val1 += dp1[ai - 1][bi];
								if (val1 >= MOD) val1 -= MOD;
							}
						}
						if (bi > 0) {
							if (dp0[ai][bi - 1] > 0) {
								val1 += dp0[ai][bi - 1];
								if (val1 >= MOD) val1 -= MOD;
							}
							if (dp1[ai][bi - 1] > 0) {
								val1 += dp1[ai][bi - 1];
								if (val1 >= MOD) val1 -= MOD;
							}
						}
					} else {
						// threshold < L
						if (ai > bi) {
							val0 = dp0[ai - 1][bi];
							val1 = dp1[ai - 1][bi];
						}
						if (bi > 0) {
							if (dp0[ai][bi - 1] > 0) {
								val0 += dp0[ai][bi - 1];
								if (val0 >= MOD) val0 -= MOD;
							}
							if (dp1[ai][bi - 1] > 0) {
								val1 += dp1[ai][bi - 1];
								if (val1 >= MOD) val1 -= MOD;
							}
						}
					}
				}
				
				dp0[ai][bi] = val0;
				dp1[ai][bi] = val1;
			}
		}
		
		System.out.println(dp1[N][N]);
	}

	static class FastScanner {
		private final InputStream in;
		private final byte[] buf = new byte[1024];
		private int ptr = 0;
		private int buflen = 0;
		FastScanner(InputStream source) { this.in = source; }
		private boolean hasNextByte() {
			if (ptr < buflen) return true;
			ptr = 0;
			try { buflen = in.read(buf); } catch (IOException e) { e.printStackTrace(); }
			return buflen > 0;
		}
		private int readByte() { return hasNextByte() ? buf[ptr++] : -1; }
		private boolean isPrintableChar(int c) { return 33 <= c && c <= 126; }
		private boolean isNumeric(int c) { return '0' <= c && c <= '9'; }
		private void skipToNextPrintableChar() { while (hasNextByte() && !isPrintableChar(buf[ptr])) ptr++; }
		public boolean hasNext() { skipToNextPrintableChar(); return hasNextByte(); }
		public int nextInt() {
			if (!hasNext()) throw new NoSuchElementException();
			int ret = 0;
			int b = readByte();
			boolean negative = false;
			if (b == '-') { negative = true; b = readByte(); }
			if (!isNumeric(b)) throw new NumberFormatException();
			while (true) {
				if (isNumeric(b)) ret = ret * 10 + b - '0';
				else if (b == -1 || !isPrintableChar(b)) return negative ? -ret : ret;
				else throw new NumberFormatException();
				b = readByte();
			}
		}
		public int[] nextIntArray(int N) {
			int[] ret = new int[N];
			for (int i = 0; i < N; i++) ret[i] = nextInt();
			return ret;
		}
	}
}