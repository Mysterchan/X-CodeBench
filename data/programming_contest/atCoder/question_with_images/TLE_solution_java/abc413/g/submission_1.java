import java.util.*; import java.util.stream.*;
public class Main
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int H = Integer.valueOf(scan.next());
        int W = Integer.valueOf(scan.next());
        int K = Integer.valueOf(scan.next());
        Grid[][] square = new Grid[H][W];
        for (int h = 0;h < H;h++)
        {
            for (int w = 0;w < W;w++)
            {
                square[h][w] = new Grid('.');
            }
        }
        for (int k = 0;k < K;k++)
        {
            int r = Integer.valueOf(scan.next()) - 1;
            int c = Integer.valueOf(scan.next()) - 1;
            square[r][c].mass = '#';
        }
        scan.close();
        int[][] d = {{-1,0},{1,0},{0,-1},{0,1}};
        ArrayDeque<Place> next = new ArrayDeque<>();
        next.add(new Place(0,0));
        square[0][0].access = 0;
        while (!next.isEmpty())
        {
            Place p = next.pollFirst();
            for (int k = 0;k < d.length;k++)
            {
                int nextH = p.h + d[k][0];
                int nextW = p.w + d[k][1];
                if (0 <= nextH && nextH < H && 0 <= nextW && nextW < W)
                {
                    if (square[nextH][nextW].access == -1 && square[nextH][nextW].mass == '.')
                    {
                        square[nextH][nextW].access = square[p.h][p.w].access + 1;
                        next.add(new Place(nextH, nextW));
                    }
                }
            }
        }
        if (square[H-1][W-1].access != -1)
        {
            System.out.println("Yes");
            return;
        }
        System.out.println("No");
    }
    public static void wait(int sec)
    {
        try {

            Thread.sleep(sec * 1000);
        } catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}
class Grid
{
    int access = -1;
    char mass;
    Grid(char mass)
    {
        this.mass = mass;
    }
}
class Place
{
    int h;
    int w;
    Place(int h, int w)
    {
        this.h = h;
        this.w = w;
    }
}