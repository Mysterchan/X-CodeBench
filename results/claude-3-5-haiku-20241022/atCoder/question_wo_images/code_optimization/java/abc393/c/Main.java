import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        Set<Long> edges = new HashSet<>();
        int result = 0;
        
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            
            if(u == v){
                result++;
            } else {
                // Normalize edge: smaller vertex first
                int min = Math.min(u, v);
                int max = Math.max(u, v);
                
                // Encode edge as single long value
                long edge = ((long)min << 32) | max;
                
                if(!edges.add(edge)){
                    result++;
                }
            }
        }
        
        System.out.println(result);
    }
}