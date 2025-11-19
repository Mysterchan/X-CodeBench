import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int q = Integer.parseInt(br.readLine());
        
        for (int caseIndex = 0; caseIndex < q; caseIndex++) {
            int n = Integer.parseInt(br.readLine());
            String[] guests = br.readLine().split(" ");
            
            boolean[][] occupied = new boolean[200][200]; // Track the occupancy of table cells
            LinkedList<int[]> seats = new LinkedList<>(); // List for nearest available (x, y) coordinates

            for (int i = 0; i < 200; i++) {
                for (int j = 0; j < 200; j++) {
                    // Add table positions based on (3x + 1, 3y + 1) to (3x + 2, 3y + 2)
                    if ((i % 3 != 0) && (j % 3 != 0)) {
                        seats.add(new int[]{3 * i + 1, 3 * j + 1});
                        if (i % 3 == 1 && j % 3 == 1) {
                            seats.add(new int[]{3 * i + 1, 3 * j + 2});
                            seats.add(new int[]{3 * i + 2, 3 * j + 1});
                            seats.add(new int[]{3 * i + 2, 3 * j + 2});
                        }
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                boolean t = guests[i].equals("1");
                int[] bestSeat = null;

                if (t) { // Look for the nearest available seat
                    for (int[] seat : seats) {
                        if (!occupied[seat[0]][seat[1]]) {
                            bestSeat = seat;
                            occupied[seat[0]][seat[1]] = true;
                            break;
                        }
                    }
                } else { // Look for the nearest empty table
                    for (int[] seat : seats) {
                        if (!occupied[seat[0]][seat[1]] && (seat[0] % 3 == 1 && seat[1] % 3 == 1)) {
                            bestSeat = seat;
                            occupied[seat[0]][seat[1]] = true; // Occupying the table
                            break;
                        }
                    }
                }

                // Output the chosen seat coordinates
                out.println(bestSeat[0] + " " + bestSeat[1]);
                
                // If we selected from the list, remove it to prevent future selection
                seats.remove(bestSeat);
            }
        }
        out.flush();
    }
}