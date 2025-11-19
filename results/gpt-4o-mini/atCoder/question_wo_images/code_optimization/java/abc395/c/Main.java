import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        HashMap<Integer, Integer> lastIndexMap = new HashMap<>();
        int minLength = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            if (lastIndexMap.containsKey(A[i])) {
                int length = i - lastIndexMap.get(A[i]) + 1;
                minLength = Math.min(minLength, length);
            }
            lastIndexMap.put(A[i], i);
        }

        System.out.println(minLength == Integer.MAX_VALUE ? -1 : minLength);
    }
}