import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int N = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        long[] arr = new long[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(input[i]);
        }
        
        Set<Long> possibleXORs = new HashSet<>();
        long totalXOR = 0;
        for (long num : arr) {
            totalXOR ^= num;
        }
        
        possibleXORs.add(totalXOR);
        for (long num : arr) {
            possibleXORs.add(totalXOR ^ num);
        }
        
        pw.println(possibleXORs.size());
        pw.close();
    }
}