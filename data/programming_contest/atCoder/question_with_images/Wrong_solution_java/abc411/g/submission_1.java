import java.io.*;
import java.util.*;

class Main {
	static final int MOD = 998244353;
	int N, M;
	long[][] e;

	void main() {
		int[] ns = nextInts();
		N = ns[0]; M = ns[1];
		e = new long[N][N];
		for (int i = 0; i < M; i++) {
			int[] uv = nextInts();
			int u = uv[0] - 1, v = uv[1] - 1;
			e[u][v]++; e[v][u]++;
		}
		long s = 0;
		for (int i = 0; i < N; i++)
			for (int j = i+1; j < N; j++)
				s = (s + e[i][j] * (e[i][j] - 1) %MOD) %MOD;

		for (int p = 3; p <= N; p++) {
			long[][] dp = new long[1 << p][p];
			dp[1 << (p-1)][p-1] = 1;
			for (int bp = 1 << (p-1); bp < (1 << p); bp++) {
				int bc = Integer.bitCount(bp);
				for (int i = 0; i < p; i++) {
					if ((bp & (1 << i)) == 0) continue;
					if (bc >= 3) s = (s + dp[bp][i] * e[i][p - 1] %MOD) %MOD;
					for (int j = 0; j < p; j++) {
						if ((bp & (1 << j)) != 0) continue;
						dp[bp | 1 << j][j] = (dp[bp | 1 << j][j] + dp[bp][i] * e[i][j] %MOD) %MOD;
					}
				}
			}
		}
		System.out.println(s/2);
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
}