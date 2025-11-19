import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        
        int[] pigeonLocation = new int[n + 1];
        int[] nestCount = new int[n + 1];
        int multipigeonNests = 0;
        
        for (int i = 1; i <= n; i++) {
            pigeonLocation[i] = i;
            nestCount[i] = 1;
        }
        
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int judge = Integer.parseInt(st.nextToken());
            
            if (judge == 1) {
                int p = Integer.parseInt(st.nextToken());
                int h = Integer.parseInt(st.nextToken());
                
                int oldNest = pigeonLocation[p];
                pigeonLocation[p] = h;
                
                if (nestCount[oldNest] == 2) {
                    multipigeonNests--;
                }
                nestCount[oldNest]--;
                
                if (nestCount[h] == 1) {
                    multipigeonNests++;
                }
                nestCount[h]++;
            } else {
                sb.append(multipigeonNests).append('\n');
            }
        }
        
        System.out.print(sb);
    }
}