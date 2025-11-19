import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long Rt = sc.nextLong();
        long Ct = sc.nextLong();
        long Ra = sc.nextLong();
        long Ca = sc.nextLong();
        long N = sc.nextLong();
        int M = sc.nextInt();
        int L = sc.nextInt();

        // Read Takahashi's moves in compressed form
        char[] sChars = new char[M];
        long[] sCounts = new long[M];
        for (int i = 0; i < M; i++) {
            sChars[i] = sc.next().charAt(0);
            sCounts[i] = sc.nextLong();
        }

        // Read Aoki's moves in compressed form
        char[] tChars = new char[L];
        long[] tCounts = new long[L];
        for (int i = 0; i < L; i++) {
            tChars[i] = sc.next().charAt(0);
            tCounts[i] = sc.nextLong();
        }

        // Directions mapping for convenience
        // U: r-1, D: r+1, L: c-1, R: c+1
        int[] drMap = new int[256];
        int[] dcMap = new int[256];
        drMap['U'] = -1; dcMap['U'] = 0;
        drMap['D'] = 1;  dcMap['D'] = 0;
        drMap['L'] = 0;  dcMap['L'] = -1;
        drMap['R'] = 0;  dcMap['R'] = 1;

        // We'll process the moves in a two-pointer manner over the compressed sequences
        int i = 0, j = 0;
        long remS = sCounts[0];
        long remT = tCounts[0];

        // Current positions
        long rT = Rt, cT = Ct;
        long rA = Ra, cA = Ca;

        long count = 0;

        while (i < M && j < L) {
            // Number of moves to process in this step
            long step = Math.min(remS, remT);

            // Movement deltas for this step
            int drS = drMap[sChars[i]];
            int dcS = dcMap[sChars[i]];
            int drT = drMap[tChars[j]];
            int dcT = dcMap[tChars[j]];

            // Relative movement per step
            long drDiff = drS - drT;
            long dcDiff = dcS - dcT;

            // Current relative position
            long rr = rT - rA;
            long cc = cT - cA;

            if (drDiff == 0 && dcDiff == 0) {
                // Both move the same way, relative position doesn't change
                // If currently same cell, all steps count
                if (rr == 0 && cc == 0) {
                    count += step;
                }
                // Update positions after step
                rT += drS * step;
                cT += dcS * step;
                rA += drT * step;
                cA += dcT * step;
            } else {
                // Relative position changes by (drDiff, dcDiff) each move
                // We want to find number of moves x in [1, step] such that:
                // rr + drDiff * x == 0 and cc + dcDiff * x == 0
                // Both must be zero at the same x

                // Solve for x:
                // If drDiff != 0: x = -rr / drDiff (must be integer and 1 <= x <= step)
                // If dcDiff != 0: x = -cc / dcDiff (must be integer and 1 <= x <= step)
                // Both must be equal

                // Handle cases carefully:

                if (drDiff == 0) {
                    // Then rr must be 0 for any solution
                    if (rr != 0) {
                        // No solution
                        // Just update positions
                        rT += drS * step;
                        cT += dcS * step;
                        rA += drT * step;
                        cA += dcT * step;
                    } else {
                        // rr == 0, so only check cc + dcDiff * x == 0
                        // x = -cc / dcDiff
                        if (dcDiff != 0) {
                            long x = -cc / dcDiff;
                            if (x >= 1 && x <= step && cc + dcDiff * x == 0) {
                                count++;
                            }
                        }
                        // Update positions
                        rT += drS * step;
                        cT += dcS * step;
                        rA += drT * step;
                        cA += dcT * step;
                    }
                } else if (dcDiff == 0) {
                    // Then cc must be 0 for any solution
                    if (cc != 0) {
                        // No solution
                        rT += drS * step;
                        cT += dcS * step;
                        rA += drT * step;
                        cA += dcT * step;
                    } else {
                        // cc == 0, check rr + drDiff * x == 0
                        long x = -rr / drDiff;
                        if (x >= 1 && x <= step && rr + drDiff * x == 0) {
                            count++;
                        }
                        rT += drS * step;
                        cT += dcS * step;
                        rA += drT * step;
                        cA += dcT * step;
                    }
                } else {
                    // Both drDiff and dcDiff != 0
                    // Check if -rr/drDiff == -cc/dcDiff and both are integers
                    if ((-rr) * dcDiff == (-cc) * drDiff) {
                        // Check if division is exact
                        if ((-rr) % drDiff == 0 && (-cc) % dcDiff == 0) {
                            long x = -rr / drDiff;
                            if (x >= 1 && x <= step) {
                                count++;
                            }
                        }
                    }
                    rT += drS * step;
                    cT += dcS * step;
                    rA += drT * step;
                    cA += dcT * step;
                }
            }

            // Update remaining counts and indices
            remS -= step;
            remT -= step;
            if (remS == 0) {
                i++;
                if (i < M) remS = sCounts[i];
            }
            if (remT == 0) {
                j++;
                if (j < L) remT = tCounts[j];
            }
        }

        System.out.println(count);
    }
}