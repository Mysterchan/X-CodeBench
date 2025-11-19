import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bu = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(bu.readLine());
        
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(bu.readLine());
            String[] input = bu.readLine().split(" ");
            Map<Integer, Long> freqMap = new HashMap<>();
            
            for (int i = 0; i < N; i++) {
                int num = Integer.parseInt(input[i]);
                freqMap.put(num, freqMap.getOrDefault(num, 0L) + 1);
            }

            long insertions = 0;
            long currentCount = 0;

            // Iterate through possible values starting from the lowest
            for (int i = 1; i <= 200000; i++) {
                long count = freqMap.getOrDefault(i, 0L);
                currentCount += count;

                // If currentCount is odd, we need one more to make it even
                if (currentCount % 2 != 0) {
                    insertions++;
                    currentCount++; // imagine we added a number to make it even
                }
            }

            sb.append(insertions).append("\n");
        }
        
        System.out.print(sb);
    }
}