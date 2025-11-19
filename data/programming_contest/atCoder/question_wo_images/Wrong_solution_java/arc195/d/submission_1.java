import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.function.IntFunction;
import java.util.function.LongFunction;

public class Main {
	public static void main(String[] args) {
		Main o = new Main();
		o.solve();
	}

	public void solve() {
		FastScanner sc = new FastScanner(System.in);
		int T = sc.nextInt();
		int[] ans = new int[T];
		for (int t = 0; t < T; t++) {
			int N = sc.nextInt();
			int[] A = new int[N];
			for (int i = 0; i < N; i++) {
				A[i] = sc.nextInt();
			}
			ans[t] = solve0(N, A);
		}

		print(ans, LF);
	}

	int solve0(int N, int[] A) {
		int[] X = Arrays.copyOf(A, N);
		int cnt = 0;
		int prev = -1;
		for (int i = 0; i < N; i++) {
			if ( prev == -1 ) {
				prev = X[i];
			} else if ( X[i] != prev ) {
				if ( i + 1 < N && X[i + 1] == prev ) {

						int tmp = X[i];
						X[i] = X[i + 1];
						X[i + 1] = tmp;
						cnt += 2;
						prev = -1;

				} else {
					cnt += 1;
					prev = X[i];
				}
			}
		}
		if ( prev != -1 ) {
			cnt += 1;
		}
		return cnt;
	}

	static final char LF = '\n';
	static final char SPACE = ' ';
	static final String YES = "Yes";
	static final String NO = "No";
	void print(int[] array, char sep) {
		print(array, sep, n -> n, 0, array.length);
	}
	void print(int[] array, char sep, IntFunction<Integer> conv) {
		print(array, sep, conv, 0, array.length);
	}
	void print(int[] array, char sep, IntFunction<Integer> conv, int start, int end) {
		StringBuilder ans = new StringBuilder();
		for (int i = start; i < end; i++) {
			ans.append(conv.apply(array[i]));
			ans.append(sep);
		}
		ans.deleteCharAt(ans.length() - 1);
		System.out.println(ans.toString());
	}
	void print(long[] array, char sep) {
		print(array, sep, n -> n, 0, array.length);
	}
	void print(long[] array, char sep, LongFunction<Long> conv) {
		print(array, sep, conv, 0, array.length);
	}
	void print(long[] array, char sep, LongFunction<Long> conv, int start, int end) {
		StringBuilder ans = new StringBuilder();
		for (int i = start; i < end; i++) {
			ans.append(conv.apply(array[i]));
			ans.append(sep);
		}
		ans.deleteCharAt(ans.length() - 1);
		System.out.println(ans.toString());
	}
	void printYesNo(boolean yesno) {
		System.out.println(yesno ? YES : NO);
	}
	void printDouble(double val, int digit) {
		System.out.println(String.format("%." + digit + "f", val));
	}

	class FastScanner {
		private final InputStream in;
		private final byte[] buf = new byte[1024];
		private int ptr = 0;
		private int buflen = 0;
		FastScanner( InputStream source ) { this.in = source; }
		private boolean hasNextByte() {
			if ( ptr < buflen ) return true;
			else {
				ptr = 0;
				try { buflen = in.read(buf); } catch (IOException e) { e.printStackTrace(); }
				if ( buflen <= 0 ) return false;
			}
			return true;
		}
		private int readByte() { if ( hasNextByte() ) return buf[ptr++]; else return -1; }
		private boolean isPrintableChar( int c ) { return 33 <= c && c <= 126; }
		private boolean isNumeric( int c ) { return '0' <= c && c <= '9'; }
		private void skipToNextPrintableChar() { while ( hasNextByte() && !isPrintableChar(buf[ptr]) ) ptr++; }
		public boolean hasNext() { skipToNextPrintableChar(); return hasNextByte(); }
		public String next() {
			if ( !hasNext() ) throw new NoSuchElementException();
			StringBuilder ret = new StringBuilder();
			int b = readByte();
			while ( isPrintableChar(b) ) { ret.appendCodePoint(b); b = readByte(); }
			return ret.toString();
		}
		public long nextLong() {
			if ( !hasNext() ) throw new NoSuchElementException();
			long ret = 0;
			int b = readByte();
			boolean negative = false;
			if ( b == '-' ) { negative = true; if ( hasNextByte() ) b = readByte(); }
			if ( !isNumeric(b) ) throw new NumberFormatException();
			while ( true ) {
				if ( isNumeric(b) ) ret = ret * 10 + b - '0';
				else if ( b == -1 || !isPrintableChar(b) ) return negative ? -ret : ret;
				else throw new NumberFormatException();
				b = readByte();
			}
		}
		public int nextInt() { return (int)nextLong(); }
		public double nextDouble() { return Double.parseDouble(next()); }
	}
}