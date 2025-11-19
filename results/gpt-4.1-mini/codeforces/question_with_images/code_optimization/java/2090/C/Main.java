import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

    // Precompute the order of seats in a table by (x,y) priority
    // The order is: (3x+1,3y+1), (3x+1,3y+2), (3x+2,3y+1), (3x+2,3y+2)
    // This order matches the problem's tie-breaking rules.

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int q = Integer.parseInt(br.readLine());
        // We will maintain two pointers for tables:
        // For t_i=0 guests: assign the next completely free table (all 4 seats free)
        // For t_i=1 guests: assign the next free seat in order, possibly in partially occupied tables

        // Since sum of n <= 50000, we can preallocate arrays for seats and tables.

        // For each test case, we reset pointers.

        for (int _ = 0; _ < q; _++) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] t = new int[n];
            for (int i = 0; i < n; i++) {
                t[i] = Integer.parseInt(st.nextToken());
            }

            // Pointer to next free table for t_i=0 guests
            int nextTable = 0;
            // Pointer to next free seat for t_i=1 guests
            int nextSeat = 0;

            // Each table has 4 seats, so seat index = nextSeat
            // seat number in table = nextSeat % 4
            // table number for seat = nextSeat / 4

            // For t_i=0 guests, assign table number = nextTable, seat 0 (3*table+1, 3*table+1)
            // then nextTable++

            // For t_i=1 guests, assign seat number = nextSeat, seat position depends on seat index mod 4
            // then nextSeat++

            // The coordinates for seats in table x,y:
            // seat 0: (3x+1, 3y+1)
            // seat 1: (3x+1, 3y+2)
            // seat 2: (3x+2, 3y+1)
            // seat 3: (3x+2, 3y+2)

            // We need to map seat index to (x,y) coordinates.
            // The order of tables is by increasing (x+y), then by x.
            // So we need to generate tables in order of (x+y), then x.

            // We'll generate tables on the fly by their index in the order of (x+y), x.

            // To do this, we can precompute a mapping from table index to (x,y) coordinates.

            // But since n <= 50000, max tables needed <= n (worst case all t_i=0)
            // For seats, max seats needed <= n

            // So max tables needed <= n

            // We'll generate tables in order of (x+y), then x.

            // Let's precompute tables coordinates in order.

            // The maximum sum (x+y) needed to cover n tables is about sqrt(2*n) because number of tables with x+y <= s is (s+1)(s+2)/2

            // We'll generate tables until we have at least n tables.

            int maxSum = 0;
            while ((maxSum + 1) * (maxSum + 2) / 2 < n) {
                maxSum++;
            }

            // Precompute tables coordinates in order
            int totalTables = (maxSum + 1) * (maxSum + 2) / 2;
            int[] tableX = new int[totalTables];
            int[] tableY = new int[totalTables];
            int idx = 0;
            for (int s = 0; s <= maxSum; s++) {
                for (int x = 0; x <= s; x++) {
                    int y = s - x;
                    tableX[idx] = x;
                    tableY[idx] = y;
                    idx++;
                }
            }

            // Now for seats, seat index maps to table index = seatIndex / 4, seat position = seatIndex % 4

            // For each guest:
            // if t_i == 0:
            //   assign seat 0 of table nextTable, then nextTable++
            // if t_i == 1:
            //   assign seat nextSeat % 4 of table nextSeat / 4, then nextSeat++

            // Output coordinates accordingly.

            for (int i = 0; i < n; i++) {
                if (t[i] == 0) {
                    // assign seat 0 of table nextTable
                    int x = tableX[nextTable];
                    int y = tableY[nextTable];
                    out.println((3 * x + 1) + " " + (3 * y + 1));
                    nextTable++;
                } else {
                    int seatIndex = nextSeat;
                    int tableIndex = seatIndex / 4;
                    int seatPos = seatIndex % 4;
                    int x = tableX[tableIndex];
                    int y = tableY[tableIndex];
                    int cx = 3 * x + 1;
                    int cy = 3 * y + 1;
                    switch (seatPos) {
                        case 0 -> out.println(cx + " " + cy);
                        case 1 -> out.println(cx + " " + (cy + 1));
                        case 2 -> out.println((cx + 1) + " " + cy);
                        case 3 -> out.println((cx + 1) + " " + (cy + 1));
                    }
                    nextSeat++;
                }
            }
        }
        out.flush();
    }
}