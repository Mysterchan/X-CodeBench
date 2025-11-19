import java.util.*; import java.io.*; import java.math.*;
import java.util.concurrent.*;
import java.text.*;
public class Main{

	static class InputIterator{
		ArrayList<String> inputLine = new ArrayList<>(1024);
		int index = 0; int max; String read;
		InputIterator(){
			try{
				BufferedReader br = new BufferedReader(new InputStreamReader(System.in, "UTF-8"));
				while((read = br.readLine()) != null){
					inputLine.addAll(Arrays.asList(read.split(" ")));
				}
			}catch(IOException e){}
			max = inputLine.size();
		}
		boolean hasNext(){return (index < max);}
		String next(){
			if(hasNext()){
				return inputLine.get(index++);
			}else{
				throw new IndexOutOfBoundsException("There is no more input");
			}
		}
	}
	static HashMap<Integer, String> CONVSTR = new HashMap<>();
	static InputIterator ii = new InputIterator();
	static PrintWriter out = new PrintWriter(System.out);
	static void flush(){out.flush();}
	static void myout(Object t){out.println(t);}
	static void myerr(Object... t){System.err.print("debug:");System.err.println(Arrays.deepToString(t));}
	static String next(){return ii.next();}
	static boolean hasNext(){return ii.hasNext();}
	static int nextInt(){return Integer.parseInt(next());}
	static long nextLong(){return Long.parseLong(next());}
	static double nextDouble(){return Double.parseDouble(next());}
	static ArrayList<String> nextCharArray(){return myconv(next(), 0);}
	static ArrayList<String> nextStrArray(int size){
		ArrayList<String> ret = new ArrayList<>(size);
		for(int i = 0; i < size; i++){
			ret.add(next());
		}
		return ret;
	}
	static ArrayList<Integer> nextIntArray(int size){
		ArrayList<Integer> ret = new ArrayList<>(size);
		for(int i = 0; i < size; i++){
			ret.add(Integer.parseInt(next()));
		}
		return ret;
	}
	static ArrayList<Long> nextLongArray(int size){
		ArrayList<Long> ret = new ArrayList<>(size);
		for(int i = 0; i < size; i++){
			ret.add(Long.parseLong(next()));
		}
		return ret;
	}
	@SuppressWarnings("unchecked")
	static String myconv(Object list, int no){
		StringBuilder sb = new StringBuilder("");
		String joinString = CONVSTR.get(no);
		if(list instanceof String[]){
			return String.join(joinString, (String[])list);
		}else if(list instanceof long[]){
			long[] tmp = (long[])list;
			if(tmp.length == 0){
				return "";
			}
			sb.append(String.valueOf(tmp[0]));
			for(int i = 1; i < tmp.length; i++){
				sb.append(joinString).append(String.valueOf(tmp[i]));
			}
			return sb.toString();
		}else if(list instanceof int[]){
			int[] tmp = (int[])list;
			if(tmp.length == 0){
				return "";
			}
			sb.append(String.valueOf(tmp[0]));
			for(int i = 1; i < tmp.length; i++){
				sb.append(joinString).append(String.valueOf(tmp[i]));
			}
			return sb.toString();
		}else if(list instanceof ArrayList){
			ArrayList tmp = (ArrayList)list;
			if(tmp.size() == 0){
				return "";
			}
			sb.append(tmp.get(0));
			for(int i = 1; i < tmp.size(); i++){
				sb.append(joinString).append(tmp.get(i));
			}
			return sb.toString();
		}else{
			throw new ClassCastException("Don't join");
		}
	}
	static ArrayList<String> myconv(String str, int no){
		String splitString = CONVSTR.get(no);
		return new ArrayList<String>(Arrays.asList(str.split(splitString)));
	}
	static ArrayList<String> myconv(String str, String no){
		return new ArrayList<String>(Arrays.asList(str.split(no)));
	}
	public static void main(String[] args){
		CONVSTR.put(8, " "); CONVSTR.put(9, "\n"); CONVSTR.put(0, "");
		solve();flush();
	}

	static void solve(){
		H = nextInt();
		W = nextInt();
		int N = H * W;
		list = new long[H][W];
		access = new int[H][W];
		for(int i = 0; i < H; i++){
			for(int j = 0; j < W; j++){
				list[i][j] = nextLong();

			}
		}
		for(int i = 0; i < (1 << N); i++){

			for(int j = 0; j < N; j++){
				int hi = j / W;
				int wi = j % W;
				if((i & (1 << j)) != 0){
					access[hi][wi] = -1;
				}else{
					access[hi][wi] = 0;
				}
			}
			ok = true;
			c = 0;
			for(int j = 0; j < N; j++){
				int hi = j / W;
				int wi = j % W;
				if(access[hi][wi] == 0){
					dfs(hi, wi);
				}
				if(c % 2 == 1){
					ok = false;
				}
			}
			if(ok){
				v = 0;
				try{
					Thread.sleep(1000);
				}catch(Exception e){}
				myerr(i);
				for(int j = 0; j < H; j++){
					myerr(access[j]);
				}
				for(int j = 0; j < N; j++){
					int hi = j / W;
					int wi = j % W;
					if(access[hi][wi] == -1){
						v ^= list[hi][wi];
					}
				}
				max = Math.max(max, v);
			}
		}
		myout(max);

	}

static int H;
static int W;
static long[][] list;
static int[][] access;
static boolean ok;
static int c;
static long max = 0;
static long v;
static int[][] d = {{-1,0}, {1,0}, {0,-1}, {0,1}};
static void dfs(int y, int x){
	c++;
	access[y][x] = 1;
	for(int i = 0; i < d.length; i++){
		int nextY = y + d[i][0];
		int nextX = x + d[i][1];
		if(0 <= nextY && nextY < H && 0 <= nextX && nextX < W){
			if(access[nextY][nextX] == 0){
				dfs(nextY, nextX);
			}
		}
	}
}

}