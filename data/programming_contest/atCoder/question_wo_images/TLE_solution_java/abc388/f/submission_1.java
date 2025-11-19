import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.NoSuchElementException;

class Main implements Runnable {
    public static void main(String[] args) {
        new Thread(null, new Main(), "", 1024 * 1024 * 1024).start();
	}

	public void run() {
		FastScanner sc = FastScanner.getInstance();
		PrintWriter pw = new PrintWriter(System.out);

		long N=sc.nextLong();
		int M=sc.nextInt();
		int A=sc.nextInt();
		int B=sc.nextInt();
		long[]L=new long[M];
		long[]R=new long[M];
		for(int i=0;i<M;++i) {
			L[i]=sc.nextLong();
			R[i]=sc.nextLong();
		}
		boolean[][]vis=new boolean[21][1];
		vis[0][0]=true;
		boolean[][] adj=new boolean[21][21];
			for(int j=A;j<=B;++j) {
				adj[0][j-1]=true;
			}
		for(int i=1;i<=20;++i) {
			adj[i][i-1]=true;
		}
		long cur=1;
		for(int i=0;i<M;++i) {
			int j=i;
			while(j+1<M&&R[j]==L[j+1]+1)++j;
			vis=mul(pow(adj,L[i]-cur-1),vis);
			cur=L[i]-1;
			if(R[j]-L[i]+1>=20) {
				System.out.println("No");
				return;
			}
			{
				boolean[][] nvis=new boolean[21][1];
				int w=(int)(R[j]-L[i]+1);
				for(int k=A;k<=B;++k) {
					int id=k-w-1;
					if(0<=id&&id<nvis.length)
						nvis[0][0]|=vis[id][0];
				}
				for(int k=0;k<vis.length;++k) {
					if(k+1+w<nvis.length)
						nvis[k+1+w][0]=vis[k][0];
				}
				vis=nvis;
				cur=R[j]+1;
			}

			i=j;
		}
		vis=mul(pow(adj,N-cur),vis);
		System.out.println(vis[0][0]?"Yes":"No");
	}

	boolean[][] mul(boolean[][] a, boolean[][] b) {
		boolean[][] c=new boolean[a.length][b[0].length];
		for(int i=0;i<a.length;++i) {
			for(int j=0;j<b[0].length;++j) {
				for(int k=0;k<a[i].length;++k) {
					c[i][j]|=a[i][k]&&b[k][j];
				}
			}
		}
		return c;
	}

	boolean[][] pow(boolean[][] a, long n) {
		if(n==0) {
			boolean[][] ret=new boolean[a.length][a.length];
			for(int i=0;i<a.length;++i)ret[i][i]=true;
			return ret;
		}
		boolean[][] ret=pow(mul(a, a), n/2);
		if(n%2==1)ret=mul(ret,a);
		return ret;
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}

class FastScanner {
    private static FastScanner instance = null;

    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;

    private FastScanner() {}

    public static FastScanner getInstance() {
        if (instance == null) {
            instance = new FastScanner();
        }
        return instance;
    }

    private boolean hasNextByte() {
        if (ptr < buflen) return true;
        ptr = 0;
        try {
            buflen = in.read(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return buflen > 0;
    }

    private int readByte() {
        if (hasNextByte()) return buffer[ptr++];
        else return -1;
    }

    private boolean isPrintableChar(int c) {
        return 33 <= c && c <= 126;
    }

    public boolean hasNext() {
        while (hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;
        return hasNextByte();
    }

    public String next() {
        if (!hasNext()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = readByte();
        while (isPrintableChar(b)) {
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
        while (b >= '0' && b <= '9') {
            n = n * 10 + (b - '0');
            b = readByte();
        }
        return minus ? -n : n;
    }

    public int nextInt() {
        return (int) nextLong();
    }

    public long[] nextLongs(int n) {
    	long[] a = new long[n];
    	for (int i = 0; i < n; ++i) {
    		a[i] = nextLong();
    	}
    	return a;
    }

    public int[] nextInts(int n) {
    	int[] a = new int[n];
    	for (int i = 0; i < n; ++i) {
    		a[i] = nextInt();
    	}
    	return a;
    }
}