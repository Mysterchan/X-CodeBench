import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int R = sc.nextInt();
        int C = sc.nextInt();
        String S = sc.next();

        // We track the relative position of the target cell (R,C) in the smoke's coordinate system.
        // At time t, smoke cells are all positions reachable by applying the inverse of the wind moves t times,
        // plus possibly (0,0) if no smoke at (0,0).
        // Instead of simulating all smoke cells, we track the position of (R,C) in the "smoke origin" frame.
        // If at time t, the position of (R,C) in the smoke frame is (0,0), then smoke is at (R,C) at time t+0.5.

        int r = R;
        int c = C;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            char d = S.charAt(i);
            // Move (r,c) opposite to the wind direction to track if smoke can reach (R,C)
            if (d == 'N') r++;
            else if (d == 'S') r--;
            else if (d == 'E') c--;
            else if (d == 'W') c++;

            // If after inverse move, (r,c) == (0,0), smoke is at (R,C) at time i+1+0.5
            sb.append((r == 0 && c == 0) ? '1' : '0');
        }

        System.out.println(sb.toString());
    }
}