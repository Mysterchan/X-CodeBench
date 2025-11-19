import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] A = new int[N];
        for(int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        
        HashMap<Integer, Integer> lastPos = new HashMap<>();
        int minLen = N + 1;
        
        for(int i = 0; i < N; i++) {
            if(lastPos.containsKey(A[i])) {
                int prevPos = lastPos.get(A[i]);
                minLen = Math.min(minLen, i - prevPos + 1);
            }
            lastPos.put(A[i], i);
        }
        
        System.out.println(minLen == N + 1 ? -1 : minLen);
    }
}