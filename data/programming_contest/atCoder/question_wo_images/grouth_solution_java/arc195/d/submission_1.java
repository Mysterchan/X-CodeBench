import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.NoSuchElementException;

public class Main implements Runnable {
	public static void main(String[] args) {
		new Thread(null, new Main(), "", Runtime.getRuntime().maxMemory()).start();
	}

	final static long mod=998244353;
	int MAX=10000;
	long[] fac=new long[MAX];
	long[] ifac=new long[MAX];
	long[] inv=new long[MAX];
	{
		Arrays.fill(fac, 1);
		Arrays.fill(ifac, 1);
		Arrays.fill(inv, 1);
		for (int i=2;i<MAX;++i) {
			fac[i]=i*fac[i-1]%mod;
			inv[i]=mod-(mod/i)*inv[(int)(mod%i)]%mod;
			ifac[i]=inv[i]*ifac[i-1]%mod;
		}
	}

	static long pow(long a, long n) {
		if (n==0) return 1;
		return pow(a*a%mod,n/2)*(n%2==1?a:1)%mod;
	}

	static long inv(long a) {
		return pow(a,mod-2);
	}

	long comb(int n, int k) {
		if (k<0||n-k<0)return 0;
		return fac[n]*ifac[n-k]%mod*ifac[k]%mod;
	}

	public void run() {
		FastScanner sc = new FastScanner();
		PrintWriter pw = new PrintWriter(System.out);

		int T=sc.nextInt();
		for (int testcase=0;testcase<T;testcase++) {
			int N=sc.nextInt();
			int[]A=new int[N];
			for(int i=0;i<N;++i) {
				A[i]=sc.nextInt();
			}
			long INF=Long.MAX_VALUE/3;
			long[][]dp=new long[N+1][2];

			for(int i=0;i<dp.length;++i) {
				for(int j=0;j<dp[i].length;++j) {
					dp[i][j]=-INF;
				}
			}
			dp[0][0]=0;
			for(int i=0;i<N;++i) {
				for(int swapped=0;swapped<=1;++swapped) {
					if (dp[i][swapped]==-INF)continue;
					int last=i>0?A[i-1]:-1;
					if (swapped==1&&i>=0) {
						last=A[i-2];
					}
					{
						dp[i+1][0]=Math.max(dp[i+1][0], dp[i][swapped]+(last==A[i]?1:0));
					}
					if(i+2<N&&A[i]!=A[i+1]){
						dp[i+2][1]=Math.max(dp[i+2][1], dp[i][swapped]+((last==A[i+1])?1:0)-1);
					}
				}
			}

			long max=0;
			max=Math.max(dp[N][0], max);
			max=Math.max(dp[N][1], max);
			long ans=N-max;
			pw.println(ans);
		}

		pw.close();
	}

	void tr(Object... objects) {
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
		} else {
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

	private int readByte() {
		if (hasNextByte())
			return buffer[ptr++];
		else
			return -1;
	}

	private static boolean isPrintableChar(int c) {
		return 33 <= c && c <= 126;
	}

	private void skipUnprintable() {
		while (hasNextByte() && !isPrintableChar(buffer[ptr]))
			ptr++;
	}

	public boolean hasNext() {
		skipUnprintable();
		return hasNextByte();
	}

	public String next() {
		if (!hasNext())
			throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while (isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}

	public long nextLong() {
		if (!hasNext())
			throw new NoSuchElementException();
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
		while (true) {
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			} else if (b == -1 || !isPrintableChar(b)) {
				return minus ? -n : n;
			} else {
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}

	public int nextInt() {
		return (int) nextLong();
	}
}