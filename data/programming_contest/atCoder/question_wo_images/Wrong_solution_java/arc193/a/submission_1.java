import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.Random;

public class Main implements Runnable {

	public static void main(String[] args) throws FileNotFoundException {
		new Main().run();

	}

	int[] randomPerm(int N) {
		int[] ret = new int[N];
		Arrays.setAll(ret, i -> i);
		Random rnd = new Random();
		for (int i = 0; i < N; ++i) {
			int j = rnd.nextInt(i + 1);
			if (i != j) {
				ret[i] ^= ret[j];
				ret[j] ^= ret[i];
				ret[i] ^= ret[j];
			}
		}
		return ret;
	}

	boolean cross(int L0, int R0, int L1, int R1) {
		if (R0 < L1) return false;
		if (R1 < L0) return false;
		return true;
	}

	public void run() {
		FastScanner sc = new FastScanner();
		PrintWriter pw = new PrintWriter(System.out);
		int N = sc.nextInt();
		long[] W = new long[N];
		for (int i = 0; i < N; ++i) {
			W[i] = sc.nextLong();
		}
		int[] L = new int[N];
		int[] R = new int[N];
		for (int i = 0; i < N; ++i) {
			L[i] = sc.nextInt();
			R[i] = sc.nextInt();
		}
		long[] f = new long[2 * N + 2];
		long[] g = new long[2 * N + 2];
		long INF = Long.MAX_VALUE / 3;
		Arrays.fill(f, INF);
		Arrays.fill(g, INF);
		for (int i = 0; i < N; ++i) {
			f[R[i]] = Math.min(f[R[i]], W[i]);
			g[L[i]]	= Math.min(f[L[i]], W[i]);
		}
		for (int i = 1; i < f.length; ++i) {
			f[i] = Math.min(f[i], f[i - 1]);
		}
		for (int i = g.length - 2; i >= 0; --i) {
			g[i] = Math.min(g[i], g[i + 1]);
		}

		int Q = sc.nextInt();
		for (int q = 0; q < Q; ++q) {

			int s = sc.nextInt() - 1;
			int t = sc.nextInt() - 1;
			if (!cross(L[s], R[s], L[t], R[t])) {
				pw.println(W[s] + W[t]);
			} else {
				long ret = INF;
				int left = Math.min(L[s], L[t]);
				int right = Math.max(R[s], R[t]);
				if (left > 0 && f[left - 1] != INF) {
					ret = Math.min(ret, W[s] + W[t] +  f[left - 1]);
				}
				if (f[right] != INF && right + 1 < g.length) {
					ret = Math.min(ret, W[s] + W[t] +  g[right + 1]);
				}
				pw.println(ret == INF ? -1 : ret);
			}
		}
		pw.close();
	}

	long powmod(long a, long n, long mod) {
		if (n == 0) return 1;
		return powmod(a * a % mod, n / 2, mod) * (n % 2 == 1 ? a : 1) % mod;
	}

	long pow(long a, long n) {
		if (n == 0) return 1;
		return pow(a * a, n / 2) * (n % 2 == 1 ? a : 1);
	}

	long gcd(long a, long b) {
		if (b == 0) return a;
		return gcd(b, a % b);
	}

	long lcm(long a, long b) {
		return a / gcd(a, b) * b;
	}

	static void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}

class FastScanner {
	private final InputStream in = System.in;
	private final byte[] buffer = new byte[1024];
	private int ptr = 0;
	private int buflen = 0;
	private boolean hasNextByte() {
		if (ptr < buflen) {
			return true;
		}else{
			ptr = 0;
			try {
				buflen = in.read(buffer);
			} catch (IOException e) {
				e.printStackTrace();
			}
			if (buflen <= 0) {
				return false;
			}
		}
		return true;
	}
	private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
	private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
	public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
	public String next() {
		if (!hasNext()) throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while(isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}
	public long nextLong() {
		if (!hasNext()) throw new NoSuchElementException();
		long n = 0;
		boolean minus = false;
		int b = readByte();
		if (b == '-') {
			minus = true;
			b = readByte();
		}
		if (b < '0' || '9' < b) {
			throw new NumberFormatException();
		}
		while(true){
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			}else if(b == -1 || !isPrintableChar(b)){
				return minus ? -n : n;
			}else{
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}
	public int nextInt() {
		long nl = nextLong();
		if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
		return (int) nl;
	}
	public double nextDouble() { return Double.parseDouble(next());}
}