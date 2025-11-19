import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int t, n, m, d, l, r, mod = 998244353;
	public static void main(String[] args) {
		t = sc.nextInt();
		while(t-- > 0) {
			int ans = solve();
			System.out.println(ans);
		}
	}

	public static int solve() {
		n = sc.nextInt();
		m = sc.nextInt();
		d = sc.nextInt();
		char[][]map = new char[n][m+1];
		for(int i = 0; i < n; i++) {
			String s = sc.next();
			for(int j = 1; j <= m; j++) {
				map[i][j] = s.charAt(j-1);
			}
		}
		long[] p0, p1;
		long[][][] dp = new long[n][m+1][2];

		for(int j = 1; j <= m; j++) {
			dp[n-1][j][0] = map[n-1][j] == 'X' ? 1 : 0;
		}

		p0 = getP(dp[n-1], 0);

		for(int j = 1; j <= m; j++) {
			if(map[n-1][j] == '#') continue;
			l = Math.max(1, j-d);
			r = Math.min(m, j+d);
			dp[n-1][j][1] = p0[r] - p0[l-1] - dp[n-1][j][0];
		}

		p1 = getP(dp[n-1], 1);

		for(int i = n-2; i >= 0; i--) {
			for(int j = 1; j <= m; j++) {
				if(map[i][j] == '#') continue;
				l = Math.max(1, j-d+1);
				r = Math.min(m, j+d-1);
				dp[i][j][0] += p0[r] - p0[l-1] + p1[r] - p1[l-1];
				dp[i][j][0] %= mod;
			}

			p0 = getP(dp[i], 0);

			for(int j = 1; j <= m; j++) {
				if(map[i][j] == '#') continue;
				l = Math.max(1, j-d);
				r = Math.min(m, j+d);
				dp[i][j][1] += p0[r] - p0[l-1] - dp[i][j][0];
				dp[i][j][1] %= mod;
			}

			p1 = getP(dp[i], 1);
		}

		long ans = 0;

		for(int i = 1; i <= m; i++) {
			ans += dp[0][i][0] + dp[0][i][1];
			ans %= mod;
		}
		return (int)ans;
	}

	public static long[] getP(long[][]f, int k) {
		long [] p = new long[m+1];
		for(int i = 1; i <= m; i++) {
			p[i] += f[i][k] + p[i-1];
		}
		return p;
	}

}
