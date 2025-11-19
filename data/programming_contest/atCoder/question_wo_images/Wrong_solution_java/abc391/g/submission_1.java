import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
	private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
	public static void main(String[] args) throws IOException {

		st = new StringTokenizer(reader.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(reader.readLine());
		String S = st.nextToken();
		int all = (int)Math.pow(2, N);
		int patarn[][] = new int [all][26];
		int mod = 998244353;
		for(int i = 0;i < all;i++) {
			int olddp[] = new int[N+1];
			for(int n = N-1;n >= 0;n--) {
				if(((i >> n) & 1) == 1) {
					olddp[N-n] = olddp[N-n-1]+1;
				}else {
					olddp[N-n] = olddp[N-n-1];
				}
			}
			for(int c = 0;c < 26;c++) {
				int newdp[] = new int [N+1];
				for(int n = 1;n <= N;n++) {
					int one = olddp[n];
					int two = newdp[n-1];
					int three = -10;
					if(S.charAt(n-1)-'a' == c) {

						three = olddp[n-1]+1;
					}
					newdp[n] = Math.max(one, Math.max(two, three));
				}
				int ans = 0;

				for(int n = 1;n <= N;n++) {
					ans *= 2;
					if(newdp[n-1] < newdp[n]) {
						ans += 1;
					}
				}
				patarn[i][c] = ans;

			}
		}

		int aggregate[] = new int[all];
		int oldagg[] = new int[all];
		oldagg[0] = 1;
		for(int i = 0;i < M;i++) {

			for(int p = 0;p < all;p++) {

				if(oldagg[p] <= 0)continue;
				for(int c = 1;c <= 26;c++) {

					aggregate[patarn[p][c-1]] += oldagg[p];
					aggregate[patarn[p][c-1]] %= mod;
				}
			}
			oldagg = java.util.Arrays.copyOf(aggregate, all);
			Arrays.fill(aggregate, 0);
		}
		aggregate = oldagg;

		int ans[] = new int[N+1];
		for(int i = 0;i < all;i++) {
			ans[Integer.bitCount(i)] += aggregate[i];
		}
		for(int i = 0;i <= N;i++) {
			System.out.print(ans[i]+" ");
		}
	}
}