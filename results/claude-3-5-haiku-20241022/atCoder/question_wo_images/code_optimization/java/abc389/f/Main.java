import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int n = Integer.parseInt(br.readLine());
        int[][] contests = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().split(" ");
            contests[i][0] = Integer.parseInt(parts[0]);
            contests[i][1] = Integer.parseInt(parts[1]);
        }
        
        int q = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < q; i++) {
            int x = Integer.parseInt(br.readLine());
            int rating = x;
            
            for (int j = 0; j < n; j++) {
                if (rating >= contests[j][0] && rating <= contests[j][1]) {
                    rating++;
                }
            }
            
            sb.append(rating).append("\n");
        }
        
        System.out.print(sb);
    }
}