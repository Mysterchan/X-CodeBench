import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        String s = scanner.next();
        
        int[] indices = new int[N];
        int count = 0;

        // Collect the indices of '1's
        for (int i = 0; i < N; i++) {
            if (s.charAt(i) == '1') {
                indices[count++] = i;
            }
        }

        // If there's only one '1', no swaps are needed
        if (count <= 1) {
            System.out.println(0);
            return;
        }

        // The target position to gather all '1's in the middle
        int target = indices[count / 2];
        int moves = 0;

        // Calculate the number of swaps needed to align '1's contiguously
        for (int i = 0; i < count; i++) {
            moves += Math.abs(indices[i] - (target - (count / 2) + i));
        }

        System.out.println(moves);
    }
}