import java.io.*;
import java.util.*;

class Main {
	int N, Q;
	int[] S;

	void main() {
		N = nextInt();
		S = nextInts();
		long[] a = new long[1000001];
		for (int i = 0; i < N; i++) {
			a[S[i]]++;
		}
		long[] x = convolution(a, Arrays.copyOf(a, a.length));
		int sum = 0;
		for (int i = 0; i < N; i++) {
			sum += (x[S[i] * 2] - 1) / 2;
		}
		System.out.println(sum);
	}

	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	String next() { try { return br.readLine(); } catch (Exception e) { return null; } }
	String[] nexts() { return next().split(" "); }

	static int i(String s) { return Integer.parseInt(s); }
	int nextInt() { return i(next()); }
	int[] nextInts() { return Arrays.stream(nexts()).mapToInt(Main::i).toArray(); }

	public static void main(String[] args) {
		new Main().main();
	}

	static final long MOD = 998244353;
	static final long gen = 3;
	static final long genInv = modPow(gen, MOD-2);

	private static long[] fft(long[] a, boolean inv) {
		int n = a.length;
		int c = 0;
		for (int i = 1; i < n; i++) {
			for (int j = n >> 1; j > (c ^= j); j >>= 1) { }
			if (c > i) {
				long d = a[c];
				a[c] = a[i];
				a[i] = d;
			}
		}

		long g = (inv)? genInv : gen;
		for (int i = 1; i < n; i <<= 1) {
			long z = modPow(g, (MOD - 1) / (2 * i));
			for (int j = 0; j < n; j += 2 * i) {
				long powZ = 1;
				for (int k = 0; k < i; k++) {
					long u = a[k + j];
					long v = a[k + j + i] * powZ % MOD;
					a[k + j] = (u + v) % MOD;
					a[k + j + i] = (u - v + MOD) % MOD;
					powZ = powZ * z % MOD;
				}
			}
		}
		return a;
	}

	static long[] convolution(long[] a, long[] b) {
		int n = Integer.highestOneBit(a.length + b.length - 2) << 1;
		a = fft(Arrays.copyOf(a, n), false);
		b = fft(Arrays.copyOf(b, n), false);
		for (int i = 0; i < n; ++i) a[i] = a[i] * b[i] % MOD;
		a = fft(a, true);
		long ninv = modPow(n, MOD - 2);
		for (int i = 0; i < n; ++i) a[i] = a[i] * ninv % MOD;
		return a;
	}

	private static long modPow(long a, long n) {
		long r = 1;
		for (; n > 0; n >>= 1) {
			if (n % 2 == 1) r = r * a % MOD;
			a = a * a % MOD;
		}
		return r;
	}
}