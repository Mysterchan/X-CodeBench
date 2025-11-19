import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long Rt = sc.nextLong();
        long Ct = sc.nextLong();
        long Ra = sc.nextLong();
        long Ca = sc.nextLong();
        long n = sc.nextLong();
        int m = sc.nextInt();
        int L = sc.nextInt();

        long[] movesT = new long[4]; // U, D, L, R
        long[] movesA = new long[4]; // U, D, L, R

        for (int i = 0; i < m; i++) {
            String direction = sc.next();
            long times = sc.nextLong();
            switch (direction.charAt(0)) {
                case 'U': movesT[0] += times; break;
                case 'D': movesT[1] += times; break;
                case 'L': movesT[2] += times; break;
                case 'R': movesT[3] += times; break;
            }
        }

        for (int i = 0; i < L; i++) {
            String direction = sc.next();
            long times = sc.nextInt();
            switch (direction.charAt(0)) {
                case 'U': movesA[0] += times; break;
                case 'D': movesA[1] += times; break;
                case 'L': movesA[2] += times; break;
                case 'R': movesA[3] += times; break;
            }
        }

        // Calculate final position after all moves
        long finalT = Rt - movesT[0] + movesT[1]; // U - D
        long finalC = Ct - movesT[2] + movesT[3]; // L - R
        long finalA = Ra - movesA[0] + movesA[1]; // U - D
        long finalB = Ca - movesA[2] + movesA[3]; // L - R

        // Total U-D and L-R displacement of Takahashi and Aoki
        long deltaR = finalT - finalA;
        long deltaC = finalC - finalB;

        // Compute the number of times they meet;
        long totalMovesT = movesT[0] + movesT[1]; // Total vertical moves
        long totalMovesA = movesA[0] + movesA[1]; // Total vertical moves
        long totalMoves = Math.min(totalMovesT, totalMovesA);

        // Mapping the conditions of vertical and horizontal movements
        long meetings = 0;
        if (deltaR == 0 && deltaC == 0) {
            meetings = totalMoves + 1; // They would be at the same position every step
        } else if (deltaR == 0) {
            if (Math.abs(deltaC) <= (totalMovesT - movesT[2] + movesT[3]) && Math.abs(deltaC) <= (totalMovesA - movesA[2] + movesA[3])) {
                meetings = totalMoves + 1; // Horizontal line meeting only
            }
        } else if (deltaC == 0) {
            if (Math.abs(deltaR) <= (totalMovesT - movesT[0] + movesT[1]) && Math.abs(deltaR) <= (totalMovesA - movesA[0] + movesA[1])) {
                meetings = totalMoves + 1; // Vertical line meeting only
            }
        }

        System.out.println(meetings);
    }
}