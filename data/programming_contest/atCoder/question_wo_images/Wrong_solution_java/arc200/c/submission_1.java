import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
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
		StringBuilder out = new StringBuilder();
		for (int t = 0; t < T; t++) {
			int N = sc.nextInt();
			int[] L = new int[N];
			int[] R = new int[N];
			for (int i = 0; i < N; i++) {
				L[i] = sc.nextInt() - 1;
				R[i] = sc.nextInt() - 1;
			}
			int[] a = solve0(N, L, R);
			for (int i = 0; i < N; i++) {
				out.append(a[i]);
				out.append(SPACE);
			}
			out.deleteCharAt(out.length() - 1);
			out.append(LF);
		}

		System.out.print(out.toString());
	}
	int[] solve0(int N, int[] L, int[] R) {
		Guest[] guest = new Guest[N];
		for (int i = 0; i < N; i++) {
			guest[i] = new Guest(L[i], R[i], i);
		}
		Guest[] gs0 = Arrays.copyOf(guest, N);
		Arrays.sort(gs0, (g0, g1) -> {
			return g0.L - g1.L;
		});
		ArrayList<Guest> arr = new ArrayList<>();
		for (Guest g: gs0) {
			int t = g.L;
			int ii = 0;
			for (int i = 0; i < arr.size(); i++) {
				Guest p = arr.get(i);
				if ( g.R < p.R ) {
					break;
				} else if ( g.id < p.id ) {
					break;
				} else {
					ii = i + 1;
				}
			}
			arr.add(ii, g);
		}
		int[] ret = new int[N];
		for (int i = 0; i < N; i++) {
			Guest g = arr.get(i);
			ret[g.id] = i + 1;
		}
		return ret;
	}

	class Guest {
		int L = 0;
		int R = 0;
		int id = 0;
		Guest(int L, int R, int id) {
			this.L = L;
			this.R = R;
			this.id = id;
		}
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
		public int[] nextIntArray(int N) { return nextIntArray(N, 0); }
		public int[] nextIntArray(int N, int offset) {
			int[] ret = new int[N];
			for (int i = 0; i < N; i++) ret[i] = nextInt() - offset;
			return ret;
		}
		public long[] nextLongArray(int N) {
			long[] ret = new long[N];
			for (int i = 0; i < N; i++) ret[i] = nextLong();
			return ret;
		}
		public String[] nextStringArray(int N) {
			String[] ret = new String[N];
			for (int i = 0; i < N; i++) ret[i] = next();
			return ret;
		}
	}
}