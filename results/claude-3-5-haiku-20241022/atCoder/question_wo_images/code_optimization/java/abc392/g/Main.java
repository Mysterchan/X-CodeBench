import java.util.Scanner;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] S = new int[N];
        HashSet<Integer> set = new HashSet<>();
        
        for (int i = 0; i < N; i++) {
            S[i] = sc.nextInt();
            set.add(S[i]);
        }

        sc.close();

        long count = 0;

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                int A = S[i];
                int C = S[j];
                
                if ((A + C) % 2 == 0) {
                    int B = (A + C) / 2;
                    if (set.contains(B)) {
                        count++;
                    }
                }
            }
        }

        System.out.println(count);
    }
}