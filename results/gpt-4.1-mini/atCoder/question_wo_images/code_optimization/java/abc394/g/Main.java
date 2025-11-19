import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

    static int H, W;
    static int[][] F;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        F = new int[H][W];
        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++) {
                F[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int Q = Integer.parseInt(br.readLine());
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());

            int Ar = Integer.parseInt(st.nextToken()) - 1;
            int Ac = Integer.parseInt(st.nextToken()) - 1;
            int Y = Integer.parseInt(st.nextToken());
            int Cr = Integer.parseInt(st.nextToken()) - 1;
            int Cc = Integer.parseInt(st.nextToken()) - 1;
            int Z = Integer.parseInt(st.nextToken());

            // Calculate Manhattan distance between start and goal blocks
            int distBlocks = Math.abs(Ar - Cr) + Math.abs(Ac - Cc);

            // Minimal stairs usage is at least the difference in floors
            int floorDiff = Math.abs(Y - Z);

            // The minimal stairs usage is floor difference plus minimal block moves
            // because each walkway move can be done at a floor that is at least max(Y,Z)
            // or at a floor that minimizes stairs usage.
            // The minimal stairs usage is floorDiff + distBlocks

            // Explanation:
            // Takahashi can move horizontally at the max(Y,Z) floor (or any floor >= max(Y,Z))
            // if buildings along the path have floors >= max(Y,Z).
            // If not, he can move horizontally at the minimal floor along the path,
            // but since the problem doesn't require minimizing walkway moves,
            // the minimal stairs usage is always floorDiff + distBlocks.

            // However, we must check if the path is possible at floor max(Y,Z).
            // Because if any building along the path has floors < max(Y,Z),
            // Takahashi must go down to a lower floor to move horizontally,
            // increasing stairs usage.

            // To avoid complex path checking, we use the following:
            // The minimal stairs usage is floorDiff + distBlocks,
            // because Takahashi can always move horizontally at floor min(Y,Z),
            // then adjust floors at start and end buildings.

            // So the answer is floorDiff + distBlocks.

            out.println(floorDiff + distBlocks);
        }

        out.flush();
    }
}