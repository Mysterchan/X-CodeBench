import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int count = 0;

        // Iterate over the first quadrant only
        for (int i = 0; i <= r; i++) {
            for (int j = 0; j <= r; j++) {
                // Check if the square centered at (i, j) is completely within the circle
                if (i * i + j * j <= (r - 0.5) * (r - 0.5)) {
                    count++;
                }
            }
        }

        // Since the circle is symmetric, multiply by 4 and add the center square
        System.out.println(count * 4 + 1);
    }
}