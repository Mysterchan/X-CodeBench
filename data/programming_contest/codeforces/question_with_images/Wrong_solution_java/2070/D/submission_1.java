import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;
public class Main {
    static Scanner input = new Scanner(System.in);
    static Writer writer = new Writer();
    static final int MOD = 998244353;
    static List<Integer>[] children;
    static int[] level;
    static List<Integer>[] levels;
    static long[] dp;
    static long[] v;
    public static void main(String[] args) throws IOException {
        int t = input.nextInt();
        while(t --> 0) {
            int n = input.nextInt();
            children = new List[n];
            int p;
            for(int i = 1; i < n; ++i) {
                p = input.nextInt()-1;
                List<Integer> c = children[p];
                if(c == null) {
                    c = new ArrayList<Integer>();
                    children[p] = c;
                }
                c.add(i);
            }
            writer.write(solve(n) + "\n");
        }
        writer.flush();
    }
    static long solve(int n) {
        bfs(n);
        for(int i = dp.length-2; i > 0; --i) {
            for(int node : levels[i]) {
                long childrenV = 0;
                if(children[node] != null) {
                    for(int child : children[node]) {
                        childrenV += v[child];
                        if(childrenV >= MOD) childrenV -= MOD;
                    }
                }
                v[node] = (long)1 + dp[i+1] - childrenV;
                if(v[node] >= MOD) v[node] -= MOD;
                dp[i] += v[node];
                if(dp[i] >= MOD) dp[i] -= MOD;
            }
        }
        long answer = 1;
        if(children[0] != null) {
            for(int child : children[0]) {
                answer += v[child];
                if(answer >= MOD) answer -= MOD;
            }
        }
        return answer;
    }
    static void bfs(int n) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(0);
        int l = 0;
        level = new int[n];
        while(! queue.isEmpty()) {
            int levelSize = queue.size();
            while(levelSize --> 0) {
                int node = queue.poll();
                level[node] = l;
                if(children[node] != null) {
                    for(int child : children[node]) {
                        queue.add(child);
                    }
                }
            }
            ++l;
        }
        dp = new long[l];
        v = new long[n];
        levels = new List[l];
        for(int i = 0; i < l; ++i) {
            levels[i] = new ArrayList<Integer>();
        }
        for(int i = 0; i < n; ++i) {
            levels[level[i]].add(i);
        }
        for(int node : levels[l-1]) {
            ++dp[l-1];
            v[node] = 1;
        }
    }
    static class Writer {
        BufferedWriter writer;
        Writer() {
            writer = new BufferedWriter(new OutputStreamWriter(System.out));
        }
        public void write(String data) throws IOException {
            writer.write(data);
        }
        public void flush() throws IOException {
            writer.flush();
        }
    }
    static class Scanner {
        BufferedReader reader;
        StringTokenizer string;
        public Scanner(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
        }
        public String next() throws IOException {
            while(string == null || ! string.hasMoreElements()) {
                string = new StringTokenizer(reader.readLine());
            }
            return string.nextToken();
        }
        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }
    }
}
