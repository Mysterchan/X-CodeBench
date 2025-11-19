import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] tokens = br.readLine().split(" ");
        
        long mod = 998244353;
        long[] arr = new long[N];
        for(int i = 0; i < N; i++){
            arr[i] = Long.parseLong(tokens[i]);
        }
        
        // Group elements by their bit pattern
        Map<Long, Long> maskToProduct = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        
        for(int k = 0; k < N; k++){
            long currentMask = arr[k];
            long prod = 1;
            
            // Check all previously seen masks that are subsets of current mask
            for(Map.Entry<Long, Long> entry : maskToProduct.entrySet()){
                long mask = entry.getKey();
                // Check if mask is a subset of currentMask
                if((mask | currentMask) == currentMask){
                    prod = (prod * entry.getValue()) % mod;
                }
            }
            
            // Update or add current element
            if(maskToProduct.containsKey(currentMask)){
                long existing = maskToProduct.get(currentMask);
                maskToProduct.put(currentMask, (existing * arr[k]) % mod);
            } else {
                maskToProduct.put(currentMask, arr[k]);
            }
            
            sb.append(prod).append('\n');
        }
        
        System.out.print(sb);
    }
}