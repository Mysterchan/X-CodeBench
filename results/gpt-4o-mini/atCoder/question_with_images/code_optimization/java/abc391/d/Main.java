import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int w = sc.nextInt();
        
        // Store the blocks in a list of pairs (x, y)
        List<int[]> blocks = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            blocks.add(new int[]{x, y});
        }

        // Sort blocks by their y-coordinate (row)
        blocks.sort(Comparator.comparingInt(b -> b[1]));

        // Map to track the lowest row for each column
        int[] lowestRow = new int[w + 1];
        Arrays.fill(lowestRow, 1); // Initially, the lowest row is 1 for all columns

        // Set to track existing blocks
        Set<Integer> existingBlocks = new HashSet<>();
        for (int i = 0; i < n; i++) {
            existingBlocks.add(i + 1);
        }

        // Process blocks to determine their final positions
        for (int i = 0; i < n; i++) {
            int x = blocks.get(i)[0];
            int y = blocks.get(i)[1];

            // Calculate how many rows the block can move down
            if (y >= lowestRow[x]) {
                int moveDown = Math.min(y - lowestRow[x] + 1, n - i);
                lowestRow[x] += moveDown;
                if (moveDown > 0) {
                    existingBlocks.remove(i + 1);
                }
            }
        }

        // Prepare to answer queries
        int q = sc.nextInt();
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < q; i++) {
            long t = sc.nextLong();
            int a = sc.nextInt();

            // Determine if the block exists at time t + 0.5
            int blockIndex = a - 1;
            int x = blocks.get(blockIndex)[0];
            int y = blocks.get(blockIndex)[1];

            // Calculate the effective position of the block at time t + 0.5
            if (t >= lowestRow[x] - 1) {
                result.append("No\n");
            } else {
                result.append("Yes\n");
            }
        }

        System.out.print(result);
    }
}