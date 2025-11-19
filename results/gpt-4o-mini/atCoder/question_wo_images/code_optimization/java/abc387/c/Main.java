import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final long L = sc.nextLong();
        final long R = sc.nextLong();
        long total = 0;

        // Generate Snake numbers
        for (int d = 1; d <= 9; d++) { // Top digit from 1 to 9
            for (int len = 1; len <= 18; len++) { // Length of the number
                long snakeNumber = createSnakeNumber(d, len);
                if (snakeNumber >= L && snakeNumber <= R) {
                    total++;
                }
            }
        }

        System.out.println(total);
    }

    private static long createSnakeNumber(int topDigit, int length) {
        // Create the smallest Snake number with the given top digit and length
        StringBuilder sb = new StringBuilder();
        sb.append(topDigit);
        for (int i = 1; i < length; i++) {
            sb.append(0); // Fill with zeros to make it a valid Snake number
        }
        return Long.parseLong(sb.toString());
    }
}