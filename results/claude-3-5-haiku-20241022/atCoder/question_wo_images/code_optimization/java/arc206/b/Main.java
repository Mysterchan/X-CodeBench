import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        String[] powerStr = br.readLine().split(" ");
        String[] colorStr = br.readLine().split(" ");
        
        int[] power = new int[n];
        int[] color = new int[n];
        
        for (int i = 0; i < n; i++) {
            power[i] = Integer.parseInt(powerStr[i]);
            color[i] = Integer.parseInt(colorStr[i]);
        }
        
        ArrayList<Integer>[] groupedByColor = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++)
            groupedByColor[i] = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            groupedByColor[color[i]].add(power[i]);
        }
        
        long totalCost = 0L;
        
        for (int col = 1; col <= n; col++) {
            ArrayList<Integer> sequence = groupedByColor[col];
            int size = sequence.size();
            if (size == 0) continue;
            
            int[] lisTails = new int[size];
            int lisLength = 0;
            
            for (int value : sequence) {
                int left = 0, right = lisLength;
                while (left < right) {
                    int mid = (left + right) >>> 1;
                    if (lisTails[mid] >= value)
                        right = mid;
                    else
                        left = mid + 1;
                }
                lisTails[left] = value;
                if (left == lisLength)
                    lisLength++;
            }
            
            totalCost += (long) (size - lisLength) * col;
        }
        
        System.out.println(totalCost);
    }
}