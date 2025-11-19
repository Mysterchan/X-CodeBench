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

	void check() {
		Random rnd = new Random();
		for (int q =0 ;q < 100; ++q) {
			int N = 10;
			int[] L = new int[N];
			int[] R = new int[N];
			long[] W = new long[N];
			for (int i = 0; i < L.length; ++i) {
				L[i] = rnd.nextInt(1, 2 * N + 1);
				R[i] = rnd.nextInt(L[i], 2 * N + 1);
				W[i] = rnd.nextInt(1, 10);
			}
			int Q = 1;
			int s = rnd.nextInt(N);
			int t = rnd.nextInt(N);
			if (s==t) continue;
			long x=new Solver(N, W, L, R).query(s, t);
			long y=new Solver2(N, W, L, R).query(s, t);
			if (x != y) {
				System.out.println(N);
				for (int i = 0; i < N; ++i) System.out.print(W[i] + (i == N - 1 ? "\n" : " "));
				for (int i = 0; i < N; ++i) {
					System.out.println(L[i] + " " + R[i]);
				}
				System.out.println(Q);
				System.out.println(s + 1);
				System.out.println(t + 1);
				tr(x,y);
				throw new AssertionError();
			}
		}
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
		Solver solver = new Solver(N,W,L,R);
		int Q = sc.nextInt();
		for (int q = 0; q < Q; ++q) {

			int s = sc.nextInt() - 1;
			int t = sc.nextInt() - 1;
			pw.println(solver.query(s, t));
		}
		pw.close();

	}

	class Solver {
		int N;
		long[] minR;
		long[] minL;
		int[] L;
		int[] R;
		long[] W;
		long INF = Long.MAX_VALUE / 3;

		public Solver(int N, long[] W, int[] L, int[] R) {
			this.N = N;
			this.W = Arrays.copyOf(W, N);
			this.L = Arrays.copyOf(L, N);
			this.R = Arrays.copyOf(R, N);
			this.minR = new long[2 * N + 2];
			this.minL = new long[2 * N + 2];
			Arrays.fill(minR, INF);
			Arrays.fill(minL, INF);
			for (int i = 0; i < N; ++i) {
				minR[R[i]] = Math.min(minR[R[i]], W[i]);
				minL[L[i]]	= Math.min(minL[L[i]], W[i]);
			}
			for (int i = 1; i < minR.length; ++i) {
				minR[i] = Math.min(minR[i], minR[i - 1]);
			}
			for (int i = minL.length - 2; i >= 0; --i) {
				minL[i] = Math.min(minL[i], minL[i + 1]);
			}
		}

		boolean cross(int L0, int R0, int L1, int R1) {
			if (R0 < L1) return false;
			if (R1 < L0) return false;
			return true;
		}

		boolean in(int L0, int R0, int L1, int R1) {
			if (L0 <= L1 && R1 <= L0) return true;
			if (L1 <= L0 && R0 <= L1) return true;
			return false;
		}

		long query(int s, int t) {
			if (!cross(L[s], R[s], L[t], R[t])) {
				return W[s] + W[t];
			} else {
				long ret = INF;
				int left = Math.min(L[s], L[t]);
				int right = Math.max(R[s], R[t]);
				if (left > 0 && minR[left - 1] != INF) {
					ret = Math.min(ret, W[s] + W[t] +  minR[left - 1]);
				}
				if (minR[right] != INF && right + 1 < minL.length) {
					ret = Math.min(ret, W[s] + W[t] +  minL[right + 1]);
				}

				if (R[s] + 1 < minL.length && !in(L[s],R[s],L[t],R[t]) && L[t] <= R[s]) {
					ret = Math.min(ret, W[s] + minL[R[s] + 1] + minR[L[t] - 1] + W[t]);
				}
				if (R[t] + 1 < minL.length && !in(L[s],R[s],L[t],R[t]) && L[s] <= R[t]){
					ret = Math.min(ret, W[s] + minR[L[s] - 1] + minL[R[t] + 1] + W[t]);
				}
				return (ret == INF ? -1 : ret);
			}

		}

	}

	class Solver2 {
		int N;
		long[] W;
		long INF = Long.MAX_VALUE / 3;
		int[] L;
		int[] R;

		public Solver2(int N, long[] W, int[] L, int[] R) {
			this.N = N;
			this.W = Arrays.copyOf(W, N);
			this.L = Arrays.copyOf(L, N);
			this.R = Arrays.copyOf(R, N);
		}

		boolean cross(int L0, int R0, int L1, int R1) {
			if (R0 < L1) return false;
			if (R1 < L0) return false;
			return true;
		}

		long query(int s, int t) {

			long[] dp = new long[N];
			Arrays.fill(dp, INF);
			dp[s] = W[s];
			for (int q = 0; q < N; ++q) {
				for (int src = 0; src < N; ++src) {
					for (int dst = 0; dst < N; ++dst) {
						if (!cross(L[src], R[src], L[dst], R[dst])) {
							dp[dst] = Math.min(dp[dst], dp[src] + W[dst]);
						}
					}
				}
			}
			return dp[t] == INF ? -1 : dp[t];

		}

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