import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(buff.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] a = new int[m + 1];
        int[] b = new int[m + 1];
        ArrayList<Integer>[] v = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            v[i] = new ArrayList<Integer>();
        }
        for (int i = 1; i <= m; i++) {
            st = new StringTokenizer(buff.readLine());
            a[i] = Integer.parseInt(st.nextToken());
            b[i] = Integer.parseInt(st.nextToken());
            v[a[i]].add(b[i]);
            v[b[i]].add(a[i]);
        }
        PrintWriter output = new PrintWriter(System.out);
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            Collections.sort(v[i]);
            for (int j = 0; j < v[i].size(); j++) {
                if(v[i].get(j) == i || (j != 0 && v[i].get(j-1) == v[i].get(j))) {
                    ans++;
                }
            }
        }
        output.println(ans/2);
        output.flush();
    }
}