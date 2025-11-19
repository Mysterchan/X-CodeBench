import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());
        
        int[] pigeonPos = new int[N + 1];
        int[] nestCount = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            pigeonPos[i] = i;
            nestCount[i] = 1;
        }
        
        int overCount = 0;  // number of nests with count >= 2
        StringBuilder sb = new StringBuilder();
        
        for (int qi = 0; qi < Q; qi++) {
            st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            if (type == 1) {
                int p = Integer.parseInt(st.nextToken());
                int h = Integer.parseInt(st.nextToken());
                int oldNest = pigeonPos[p];
                
                // remove from oldNest
                int beforeOld = nestCount[oldNest];
                nestCount[oldNest] = beforeOld - 1;
                if (beforeOld == 2) {
                    // it was >=2 and drops to 1 => decrease overCount
                    overCount--;
                }
                
                // add to new nest h
                int beforeNew = nestCount[h];
                nestCount[h] = beforeNew + 1;
                if (beforeNew == 1) {
                    // it was 1 and rises to 2 => increase overCount
                    overCount++;
                }
                
                pigeonPos[p] = h;
            } else {
                sb.append(overCount).append('\n');
            }
        }
        
        System.out.print(sb.toString());
    }
}